from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("products", views.products, name = "products"),
    path("register", views.register, name="register"),
    path("login_request", views.login_request, name="login_request"),
    path("logout", views.logout_request, name="logout"),
    path("blog", views.blog, name="blog"),
    path("<article_page>", views.article, name="article"),
    path("blog/<tag_page>", views.blog, name="blog"),
]