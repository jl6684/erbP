from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)  # Show 3 listings per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'listings': page_obj,
        'name': 'Real Estate'
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html', {'query': request.GET.get('q', '')})