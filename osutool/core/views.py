from django.shortcuts import render
from omap.models import Category, oMap

# Create your views here.
def index(request):
    omaps = oMap.objects.filter()[0:6]
    categories = Category.objects.all()
    context = {'categories' : categories, 'omaps' : omaps}
    return render(request, 'core/index.html', context)