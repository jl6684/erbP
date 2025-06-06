from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, district_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'district_choices': district_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors ordered by hire date for the team section
    realtors = Realtor.objects.order_by('-hire_date')
    
    # Get the first MVP realtor for "Seller of the Month"
    mvp_realtor = Realtor.objects.filter(is_mvp=True).first()
    
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor,
    }
    return render(request, 'pages/about.html', context)

# def base(request):
#     return render(request, 'base.html')


