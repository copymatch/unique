from django.contrib import admin
from django.urls import path,include
from client import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.index,name="index cl"),
    path("about/",views.about,name="about cl"),
    path("login/",views.user_login,name="login cl"),
    path("create-profile/",views.profile,name="profile cl"),
    path("home/",views.home,name="home cl"),
    path("profile/",views.view_profile,name="view profile cl"),
    path("view-work/<str:username>",views.view_work,name="view work"),
    path("search/",views.search,name="search"),
    path("rate/",views.rate,name="rate"),
    path("search_1/<str:niche>",views.search_1,name="filter 1"),
    path("search_2/<str:niche>",views.search_2,name="filter 2"),
    path("search_3/<str:niche>",views.search_3,name="filter 3"),
    path("feedback/",views.feedback,name="feedback"),
    path("view-messages/",views.view_messages,name="view messages"),   
    path("chat/<str:username>",views.conversation_box,name="chatbox"),
    path('logout/', LogoutView.as_view(), name='logout')
   


  
]