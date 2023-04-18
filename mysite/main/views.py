from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def homepage(request):
    product = Product.objects.all()  # queryset containing all products
    return render(request=request, template_name="main/home.html", context={'product':product})

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="main/products.html", context={"page_obj":page_obj})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration.  Invalid info. ")
    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"form":form})