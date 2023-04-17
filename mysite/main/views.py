from django.shortcuts import render
from .models import Product

# Create your views here.
def homepage(request):
    product = Product.objects.all()  # queryset containing all products
    return render(request=request, template_name="main/home.html", context={'product':product})

