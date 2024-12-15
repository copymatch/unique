from django.contrib import admin
from django.urls import path,include
from copywriter import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("login/",views.user_login,name="login"),
    path("create-profile/",views.profile,name="profile"),
    path("home/",views.home,name="home"),
    path("profile/",views.view_profile,name="view profile"),
    path("work/",views.upload_work,name="upload work"),
    path("view-work/<str:username>",views.view_work,name="view work"),
    path("edit_profile/",views.edit_profile,name="edit profile"),
    path("view-feedback/",views.view_feedbacks,name="view-feedback"),
    path("view-messages/",views.view_messages,name="view messages"),
    path("chat/<str:username>",views.conversation_box,name="chatboxcp"),
    path("analyze/",views.analyze_text_view,name="analyse"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("ai_rating/",views.AI_rating,name="ai_rating")
]