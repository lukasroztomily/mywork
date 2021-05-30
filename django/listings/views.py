from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.


def index (request):
    """def"""
    listings = Listing.objects.order_by('-list_date').filter(is_publish = True)
    paginator =  Paginator(listings, 1)
    page =  request.GET.get('page')
    page_list = paginator.get_page(page)
    context = {'listings': page_list}    
    return render(request, 'listings/listings.html', context)


def listing (request, listing_id):
    """def"""
    listing = get_object_or_404(Listing, pk = listing_id)
    context = {'listing': listing}   
    return render(request, 'listings/listing.html', context)



def search (request):
    """def"""
    


    context = {         
                'state_choices': state_choices,
                'bedroom_choices': bedroom_choices,
                'price_choices': price_choices,
                'listings': search_helper(request.GET),
                'values': request.GET
            }
    return render(request, 'listings/search.html', context)


def search_helper (_in):
    queryset_list = Listing.objects.order_by('-list_date')
        # Keywords 
    if 'keywords' in _in:
        keywords = _in['keywords']
        if keywords:
           queryset_list = queryset_list.filter(description__icontains = keywords) 

     # City 
    if 'city' in _in:
        city = _in['city']
        if city:
           queryset_list = queryset_list.filter(city__iexact = city)

      # State 
    if 'state' in _in:
        state = _in['state']
        if state:
           queryset_list = queryset_list.filter(state__iexact = state)

      # Bedrooms 
    if 'bedrooms' in _in:
        bedrooms = _in['bedrooms']
        if bedrooms:
           queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

      # Price 
    if 'price' in _in:
        price = _in['price']
        if price:
           queryset_list = queryset_list.filter(price__lte = price)   
    
    return queryset_list