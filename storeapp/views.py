from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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

#View to register a user
class RegisterUser(CreateView):
    #Setup form
    model = User
    form_class = UserCreationWithEmailForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

#View to update User record
@login_required
def updateUser(request):
    context={}
    #Get user details
    user = request.user
    form = UserCreationWithEmailForm(request.POST or None, instance = user)
    if form.is_valid():
        #Overwrite existing record
        form.save()
        return redirect('/store')
    context["form"] = form
    return render(request, "registration/updateUser.html", context)

#View to delete User
@login_required
def deleteUser(request):
    context={}
    user = request.user
    if request.method == "POST":
        #Delete record
        user.delete()
        return redirect('/store')
    return render(request, "registration/deleteUser.html", context)
