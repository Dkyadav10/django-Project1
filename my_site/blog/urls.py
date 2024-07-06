from django.urls import path
from . import views

urlpatterns = [     #these are the variable 
    path("", views.starting_page, name = "starting-page"), #also use the path function provided by django.
    #those names are on the basis of you means you can  give any name you want.
    path("posts", views.posts, name = "posts-page"),  #post path 
    path("posts/<slug:slug>", views.post_detail, name = "post-detail-page")  #Dynamic path, path segement that is look like this(this-is-path-like)  called as slug
]


