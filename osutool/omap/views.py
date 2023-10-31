from django.shortcuts import render, get_object_or_404, redirect

from .models import oMap

# Create your views here.
def detail(request, pk):
    omap = get_object_or_404(oMap, pk=pk)
    related_maps = oMap.objects.filter(category=omap.category).exclude(pk=pk)[0:3]
    context = {'map' : omap, 'related_maps' : related_maps}
    return render(request, 'omap/detail.html', context)
