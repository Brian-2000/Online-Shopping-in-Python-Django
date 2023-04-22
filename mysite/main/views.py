from django.shortcuts import render, redirect
from .models import Product
from django.core.paginator import Paginator
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Article

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

# Login views
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in successfully as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid Username or Password.")

        else:
            messages.error(request, "Invalid Username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You are logged out")
    return redirect("main:login_request")

def blog(request):
    blog = Article.objects.all().order_by('-article_published')
    paginator = Paginator(blog, 5)
    page_number = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    return render(request=request, template_name="main/blog.html", context={"blog":blog_obj})

def article(request, article_page):
    article = Article.objects.get(article_slug=article_page)
    return render(request=request, template_name='main/article.html', context={"article": article})