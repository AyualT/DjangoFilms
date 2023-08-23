from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Review, ReviewLike
from .forms import FilmForm, FilmSearch, ReviewForm
from django.db.models import Avg
from studios.models import Studio

from django.views.generic import ListView
# from django.core.paginator import Paginator

from hitcount.views import HitCountDetailView

class AllFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/films_list.html'
    queryset = Film.objects.filter(is_active = True).order_by('-release_date')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('title')
        context['form'] = FilmSearch()
        if query is not None:
            context['page_obj'] = Film.objects.filter(title__icontains = query, is_active = True)
        for film in context['page_obj']:
            revs = Review.objects.filter(film_id = film.pk)
            if revs.count() != 0:
                film.revs = revs.aggregate(Sum('rating'))['rating__sum']/revs.count()
            else:
                film.revs = 'No reviews'
        return context

class NewFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/new_films_list.html'
    queryset = Film.objects.filter(is_active = True).order_by('-release_date')

class PopularFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/popular_films_list.html'
    queryset = Film.objects.filter(is_active = True).order_by('-hit_count_generic__hits')

class RatingFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/films_by_rating_list.html'
    queryset = Film.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')

class ActionFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/action_films_list.html'
    queryset = Film.objects.filter(genre = "1", is_active = True).order_by('-release_date')

class ComedyFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/comedy_films_list.html'
    queryset = Film.objects.filter(genre = "7", is_active = True).order_by('-release_date')

class HorrorFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/horror_films_list.html'
    queryset = Film.objects.filter(genre = "11", is_active = True).order_by('-release_date')

class ThrillerFilmsView(ListView):
    model = Film
    paginate_by = 3
    template_name = 'films/thriller_films_list.html'
    queryset = Film.objects.filter(genre = "6", is_active = True).order_by('-release_date')

# def films_list(request):
#     films = Film.objects.filter(is_active = True).all()
#     paginator = Paginator(films, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'films/films_list.html', {'films':page_obj})

def create_review(request,fid,uid):
    film = Film.objects.get(pk=fid)
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author_id = uid
            review.film_id = fid
            review.save()
            return redirect('film_detail', pk=fid)
    return render(request, 'films/film_review.html', {'form':form, 'film':film})

def like_review(request, fid, rid, uid):
    try:
        like = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 1).delete()
    except:
        like = ReviewLike.objects.create(user_id=uid, review_id = rid, value = 1)
        try:
            dislike = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 0).delete()
        except:
            pass
    return redirect('film_detail', pk=fid)
        
def dislike_review(request, fid, rid, uid):
    try:
        dislike = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 0).delete()
    except:
        dislike = ReviewLike.objects.create(user_id=uid, review_id = rid, value = 0)
        try:
            like = ReviewLike.objects.get(user_id=uid, review_id = rid, value = 1).delete()
        except:
            pass
    return redirect('film_detail', pk=fid)

from django.db.models import Sum

class FilmView(HitCountDetailView):
    model = Film
    count_hit = True

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        if context['film'].trailer_url is not None:
            context['film'].trailer_url = context['film'].trailer_url[context['film'].trailer_url.rfind('/'):]
        revs = Review.objects.filter(film_id = context['film'].pk)
        context.update({
            'recommended': Film.objects.filter(is_active = True).exclude(pk=context['film'].pk).order_by('-hit_count_generic__hits')[:3],
            'reviews': revs,
            'review_count': revs.count(),
            'studio': Studio.objects.get(pk=context['film'].studio_id)
        })
        if revs.count() != 0:
            context.update({
                'average_rating': revs.aggregate(Sum('rating'))['rating__sum']/revs.count(),
            })
        else:
            context.update({
                'average_rating': 'No reviews'
            })
        
        for review in context['reviews']:
            review.likes = ReviewLike.objects.filter(review_id = review.pk, value = 1).count()
            review.dislikes = ReviewLike.objects.filter(review_id = review.pk, value = 0).count()
            try:
                review.is_liked = ReviewLike.objects.get(user_id = self.request.user.pk, review_id = review.pk, value = 1)
                review.is_liked = True
            except:
                review.is_liked = False

            try:
                review.is_disliked = ReviewLike.objects.get(user_id = self.request.user.pk, review_id = review.pk, value = 0)
                review.is_disliked = True
            except:
                review.is_disliked = False

        return context

# def film_detail(request, pk):
#     film = get_object_or_404(Film, pk=pk)
#     if film.trailer_url is not None:
#         film.trailer_url = film.trailer_url[film.trailer_url.rfind('/'):]
#     return render(request,'films/film_detail.html',{'film':film})

# def review_like(request, rid, uid):

# def review_dislike(request, rid, uid):

def film_new(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect('film_detail', pk=film.pk)
    else:
        form = FilmForm()
    return render(request, 'films/film_new.html', {'form':form})

def film_edit(request, pk):
    film = Film.objects.get(pk=pk)
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect('film_detail', pk=film.pk)
    else:
        form = FilmForm(instance=film)
    return render(request, 'films/film_new.html', {'form':form})