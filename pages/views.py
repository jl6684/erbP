from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all MVP realtors ordered by hire date
    realtors = Realtor.objects.order_by('-hire_date').filter(is_mvp=True)
    
    # Get the first MVP realtor for "Seller of the Month"
    mvp_realtor = realtors.first() if realtors.exists() else None
    
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor,
    }
    return render(request, 'pages/about.html', context)

# def base(request):
#     return render(request, 'base.html')


