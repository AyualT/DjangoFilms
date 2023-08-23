from django.shortcuts import render, get_object_or_404, redirect
from .models import Actor
from films.models import Film
from .forms import ActorForm

from django.views.generic import ListView

from hitcount.views import HitCountDetailView

class AllActorsView(ListView):
    model = Actor
    paginate_by = 3
    context_object_name = 'actors'
    template_name = 'actors/actors_list.html'
    queryset = Actor.objects.filter(is_active = True).order_by('-born')

# def actors_list(request):
#     actors = Actor.objects.all()
#     return render(request, 'actors/actors_list.html', {'actors':actors})

class ActorView(HitCountDetailView):
    model = Actor
    template_name = 'actors/actor_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actors_list = Film.objects.filter(stars = context['actor'].pk)
        context['actors_list'] = actors_list
        context.update({
            'recommended': Actor.objects.filter(is_active = True).exclude(pk=context['actor'].pk).order_by('-hit_count_generic__hits')[:3]
        })
        return context

# def actor_detail(request, pk):
#     actor = get_object_or_404(Actor, pk=pk)
#     return render(request,'actors/actor_detail.html',{'actor':actor})

def actor_new(request):
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return redirect('actor_detail', pk=actor.pk)
    else:
        form = ActorForm()
    return render(request, 'actors/actor_new.html', {'form':form})

def actor_edit(request, pk):
    actor = Actor.objects.get(pk=pk)
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES, instance=actor)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return redirect('actor_detail', pk=actor.pk)
    else:
        form = ActorForm(instance=actor)
    return render(request, 'actors/actor_new.html', {'form':form})