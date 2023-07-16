from django.shortcuts import render
from django.db.models import Q
from .models import *

# Create your views here.
def browse(request):
    context = {}
    context["products"] = Product.objects.all()
    return render(request, 'storeapp/browse.html', context)

def product(request, pid):
    context = {}
    try: 
        context["product"] = Product.objects.get(id=pid)
    except:
        pass
    return render(request, 'storeapp/product.html', context)

def search(request):
    context = {}
    query = request.GET.get('query')
    if query:
        try:
            query_words = query.split()
            products = []

            for word in query_words:
                results = Product.objects.filter(
                    Q(name__icontains=word) | Q(description__icontains=word)
                )
                products.extend(results)
        except:
            pass
        if products:
            products=list(set(products))
            context["products"] = products
        context["query"] = query
    
    return render(request, 'storeapp/search.html', context)