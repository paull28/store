from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from datetime import datetime
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
    sort_by = request.GET.get('sort_by', 'a-z')
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
            if sort_by == 'a-z':
                products.sort(key=lambda x: x.name)
            elif sort_by == 'z-a':
                products.sort(key=lambda x: x.name, reverse=True)
            elif sort_by == 'priceLTH':
                products.sort(key=lambda x: x.cost)
            elif sort_by == 'priceHTL':
                products.sort(key=lambda x: x.cost, reverse=True)

            context["products"] = products
        context["query"] = query
        context["sort_by"] = sort_by
    
    return render(request, 'storeapp/search.html', context)

class CustomLoginView(LoginView):

    def form_valid(self, form):
        # Custom logic here, if needed
        print("yes")
        messages.success(self.request, 'Login successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("no")
        # Custom logic here, if needed
        messages.error(self.request, 'Login failed. Please try again.')
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        # Display the logout message
        messages.success(request, 'Logout successful.')
        return super().dispatch(request, *args, **kwargs)

    def get_next_page(self):
        # Provide the URL to redirect after logout
        return reverse_lazy('/store/')  # Replace 'home' with the desired URL
    
#View to register a user
class RegisterUser(CreateView):
    #Setup form
    model = User
    form_class = UserCreationWithEmailForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def account(request):
    context={}
    return render(request, 'storeapp/account.html', context)

#View to update User record
@login_required
def update_user(request):
    context={}
    #Get user details
    user = request.user
    form = UserCreationWithEmailForm(request.POST or None, instance = user)
    if form.is_valid():
        #Overwrite existing record
        form.save()
        messages.success(request, "Details updated.")
        return redirect('/accounts/')
    else:
        messages.error(request, "Details not updated.")

    context["form"] = form
    return render(request, "registration/updateUser.html", context)

#View to delete User
@login_required
def delete_user(request):
    context={}
    user = request.user
    if request.method == "POST":
        #Delete record
        user.delete()
        return redirect('/store')
    return render(request, "registration/deleteUser.html", context)

@login_required
def orders(request):
    context={}
    user = request.user
    try:
        results = CustomerOrder.objects.filter(customer=user.id).order_by('-id')
        context["orders"] = results
    except:
        pass
    return render(request, 'storeapp/orders.html', context)

def basket(request):
    context = {}
    try:
        basket = CartItem.objects.filter(customer=request.user.id)
        context["basket"] = basket
        total = 0.0
        count = 0
        for item in basket:
            total += item.cost
            count += item.qty
        context["total_cost"] = round(total, 2)
        context["count"] = count
    except:
        pass
    return render(request, "storeapp/basket.html", context)

def add_to_basket(request, pid):
    context = {}
    product = get_object_or_404(Product, id=pid)
    qty = int(request.POST.get('quantity', 1))
    cost = round((float(product.cost) * qty), 2)

    cart_item, created = CartItem.objects.get_or_create(
        customer=request.user,
        product=product,
        defaults={'qty': qty, 'cost': cost}
    )

    if not created:
        cart_item.qty += qty
        cart_item.cost += cost
        cart_item.cost = round(cart_item.cost, 2)
        cart_item.save()
    messages.success(request, 'Added to basket.')
    return redirect("/store/"+str(pid))

def remove_from_basket(request, cid):
    item = get_object_or_404(CartItem, id=cid)
    item.delete()
    messages.success(request, 'Row removed from basket.')
    return redirect("/store/basket")

def clear_basket(request):
    context={}
    basket = CartItem.objects.filter(customer=request.user.id)
    basket.delete()
    messages.success(request, 'Basket cleared.')
    return redirect("/store/basket")

@login_required
def checkout(request):
    context = {}
    try:
        basket = CartItem.objects.filter(customer=request.user.id)
        context["basket"] = basket
        total = 0.0
        count = 0
        for item in basket:
            total += item.cost
            count += item.qty
        total = round(total, 2)
        context["total_cost"] = total
        context["count"] = count

        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            postcode = request.POST.get('postcode')
            line1 = request.POST.get('line1')
            line2 = request.POST.get('line2')
            line3 = request.POST.get('line3')
            phone_number = request.POST.get('phone_number')
            country = request.POST.get('country')
            delivery_instructions = request.POST.get('delivery_instructions')

            customer = request.user.id
            date = datetime.now()

            customer_order = CustomerOrder.objects.create(
            total=total,  # Replace with the actual total value, if available
            customer=request.user,
            date=datetime.now(),
            fname=fname,
            lname=lname,
            postcode=postcode,
            line1=line1,
            line2=line2,
            line3=line3,
            phone_number=phone_number,
            country=country,
            delivery_instructions=delivery_instructions
            )

            messages.success(request, ("Order placed."))
            return redirect("/store/checkout/order")

    except Exception as e:
        print(e)
    return render(request, "storeapp/checkout.html", context)

def order_confirmation(request):
    context = {}
    
    messages.info(request, 'processing')
    return render(request, 'storeapp/order_confirmation.html', context)