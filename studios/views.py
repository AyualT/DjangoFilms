from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from .models import Studio
from films.models import Film
from .forms import StudioForm

from django.views.generic import ListView

from hitcount.views import HitCountDetailView

class AllStudiosView(ListView):
    model = Studio
    paginate_by = 3
    template_name = 'studios/studios_list.html'
    queryset = Studio.objects.filter(is_active = True).order_by('-founded')

# def studios_list(request):
#     studios = Studio.objects.all()
#     for i in range(len(studios)):
#         studios[i].films_list = Film.objects.filter(studio = studios[i].pk)
#     return render(request, 'studios/studios_list.html', {'studios':studios})

class StudioView(HitCountDetailView):
    model = Studio
    template_name = 'studios/studio_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        films_list = Film.objects.filter(studio = context['studio'].pk, is_active=True)
        context['films_list'] = films_list
        context.update({
            'recommended': Studio.objects.filter(is_active = True).exclude(pk = context['studio'].pk).order_by('-hit_count_generic__hits')[:3]
        })
        return context

# def studio_detail(request, pk):
#     studio = get_object_or_404(Studio, pk=pk)
#     films_list = Film.objects.filter(studio = studio.pk)
#     return render(request, 'studios/studio_detail.html', {'studio':studio, 'films_list':films_list})

def studio_new(request):
    if request.method == 'POST':
        form = StudioForm(request.POST, request.FILES)
        if form.is_valid():
            studio = form.save(commit=False)
            studio.save()
            return redirect('studio_detail', pk=studio.pk)
    else:
        form = StudioForm()
    return render(request, 'studios/studio_new.html', {'form':form})

def studio_edit(request, pk):
    studio = Studio.objects.get(pk=pk)
    if request.method == "POST":
        form = StudioForm(request.POST, request.FILES, instance=studio)
        if form.is_valid():
            studio = form.save(commit=False)
            studio.save()
            return redirect('studio_detail', pk=studio.pk)
    else:
        form = StudioForm(instance=studio)
    return render(request, 'studios/studio_new.html', {'form':form})