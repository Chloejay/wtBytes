from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Title
from django.template import loader
from django.shortcuts import get_object_or_404  
from django.urls import reverse
from django.views import generic

# use Django’s generic views instead
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'newsfeed'

    def get_queryset(self):
        return Title.objects.order_by('-pub_date')[:]

class DetailView(generic.DetailView):
    # model = Title
    # template_name = 'news/index.html'
    pass 