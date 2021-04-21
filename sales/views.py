from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm

# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    hello = 'Hello world from the view.'
    context = {
        'hello': hello,
        'form':form
    }
    return render(request, 'sales/home.html', context)

class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'