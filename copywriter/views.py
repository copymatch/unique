from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from copywriter.models import Profile,Works
from client.models import Feedback,Message
from django.db.models import Q
from .forms import TextAnalysisForm
from django.urls import reverse


def index(request):
    return render(request,"copy.html")

def about(request):
    return HttpResponse("this is about copywriter wala")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("http://copymatch.in/copywriter/home/") # Redirect to a success page (e.g., home)
        if user is None:
            return HttpResponseRedirect('http://copymatch.in/copywriter/create-profile')
    
    return render(request, 'logincp.html')  # Render the login page


def profile(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        niche=request.POST.get("niche")
        email=request.POST.get("email")
        price=request.POST.get("price")

        if User.objects.filter(username=username).exists():
            return render(request, "profile.html")


        data=Profile(username=username,password=password,niche=niche,email=email,price=price)
        data.save()

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        login(request,user)

        
        return HttpResponseRedirect("http://copymatch.in/copywriter/ai_rating") 
    
    return render(request,"profile.html")
@login_required
def home(request):
    return render(request,"copyhome.html")

@login_required   
def view_profile(request):
        username=request.user.username
        profile = get_object_or_404(Profile, username=username)
        return render(request,"view_profile.html",{'profile':profile})
@login_required
def upload_work(request):
    username=request.user.username
    if request.method == "POST":
        works=request.POST.get("works")
        work=Works(username=username,works=works)
        work.save()
        return HttpResponseRedirect("http://copymatch.in/copywriter/home")

    return render(request,"works.html")
#to complete!!!

    
@login_required
def view_work(request, username):
    profile = Profile.objects.get(username=username)  # Assuming there's a Profile model
    works = Works.objects.filter(username=username)  # Get all works for the user
    return render(request, "tp.html", {'profile': profile, 'works': works})

@login_required
def edit_profile(request):
    username=request.user.username
    user=request.user
    obj=get_object_or_404(Profile,username=username)
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        niche=request.POST.get("niche")
        email=request.POST.get("email")
        price=request.POST.get("price")

        obj.username=username
        obj.niche=niche
        obj.password=password
        obj.email=email
        obj.price=price
        obj.save()
        return HttpResponseRedirect("http://copymatch.in/copywriter/home")
    
    return render(request,"edit_profile.html")
 
@login_required
def view_feedbacks(request):
    user = request.user
    username=request.user.username  
    feedbacks = Feedback.objects.filter(username=username)

    return render(request, 'view-feedbacks.html', {'objects': feedbacks})

@login_required
def view_messages(request):
    empty=[]
    uniques=[]
    user = request.user
    username=request.user.username 
    messages1=Message.objects.filter(user_sender=username)
    messages2=Message.objects.filter(user_receiver=username)
    for obj in messages1:
        empty.append(obj.user_receiver)

    for obj in messages2:
        empty.append(obj.user_sender)
    #remove repetition
    for obj in empty:
        if obj not in uniques:
            uniques.append(obj)
        
    return render(request,"view_messages.html",{"objects":uniques})
def conversation_box(request,username):
    user_1=request.user.username
    user_2=username
    message1 =Message.objects.filter(Q(user_receiver=user_1) | Q(user_receiver=user_2),Q(user_sender=user_1) | Q(user_sender=user_2))
    if request.method=="POST":
        message=request.POST.get("message")
        data=Message(user_sender=user_1,user_receiver=user_2,message=message,unread=True)
        data.save()
        url=reverse("chatboxcp",args=[username])
        return HttpResponseRedirect(url)
   
    return render(request,"chatboxup.html",{'object1':message1}) 


#to be done later
