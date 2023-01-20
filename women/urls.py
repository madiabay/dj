from django.views.decorators.cache import cache_page

from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='home'), # using func
    path('', WomenHome.as_view(), name='home'), # using class
    path('about/', about, name='about'), # using func
    # path('addpost/', addpost, name='add_post'), # using func
    path('addpost/', AddPost.as_view(), name='add_post'), # using class
    path('contact/', contact, name='contact'), # using func
    path('register/', RegisterUser.as_view(), name='register'), # using class
    path('login/', LoginUser.as_view(), name='login'), # using class

    path('logout/', logout_user, name='logout'), # using class

    # path('post/<slug:post_slug>/', show_post, name='post'), # using func
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'), # using class
    # path('category/<int:cat_id>/', show_category, name='category'), # using func
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'), # using class
]


