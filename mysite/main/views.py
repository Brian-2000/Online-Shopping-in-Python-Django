from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
    product = Product.objects.all()  # queryset containing all products
    return render(request=request, template_name="main/home.html", context={'product':product})

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="main/products.html", context={"page_obj":page_obj})