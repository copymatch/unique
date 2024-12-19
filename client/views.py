from django.shortcuts import render,HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from copywriter.models import Works,Profile
from client.models import Profilecl,Rating,Feedback,Message
from django.db.models import Q



#this is done
def index(request):
    return render(request,"client.html")

def about(request):
    return HttpResponse("this is about")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("http://127.0.0.1:8000/client/home") # Redirect to a success page (e.g., home)
        if user is None:
            return HttpResponseRedirect('http://127.0.0.1:8000/client/create-profile')
    
    return render(request, 'logincl.html')  # Render the login page



#this is done 
def profile(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        niche=request.POST.get("niche")
        email=request.POST.get("email")

        if User.objects.filter(username=username).exists():          
            return render(request, "profilecl.html")


        data=Profilecl(username=username,password=password,niche=niche,email=email)
        data.save()

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        login(request,user)
        return HttpResponseRedirect("http://127.0.0.1:8000/client/home") 
    
    return render(request,"profilecl.html")

#this is done
def home(request):
    return render(request,"clienthome.html")


#this is done 
def view_profile(request):
    username=request.user.username
    profile = get_object_or_404(Profilecl, username=username)
    return render(request,"view_profilecl.html",{'profile':profile})
    


#this is done  
def view_work(request,username): 
    profile = Profile.objects.get(username=username)  # Assuming there's a Profile model
    works = Works.objects.filter(username=username)  # Get all works for the user
    return render(request, "tpv.html", {'profile': profile, 'works': works})
    
   

def search(request):
    username=request.user.username
    pro=Profilecl.objects.get(username=username)
    niche=pro.niche
    profile =Profile.objects.filter(niche=niche)
    return render(request,"searchup.html",{'objects':profile})
    
    

def search_1(request,niche):
     profile =Profile.objects.filter(niche=niche,price__lt=3000)
     return render(request,"searchup.html",{'objects':profile})
    
def search_2(request,niche):
     profile =Profile.objects.filter(niche=niche,price__gt=4000)
     return render(request,"searchup.html",{'objects':profile})

def search_3(request,niche):
     profile =Profile.objects.filter(niche=niche,price__gt=3000,price__lt=4000)
     return render(request,"searchup.html",{'objects':profile})

def rate(request):
    if request.method=="POST":
        rate=request.POST.get("rating")
        username=request.POST.get("username")
        if User.objects.filter(username=username).exists():
            data=Rating(username=username,rate=rate)
            data.save()
            obj=get_object_or_404(Profile,username=username)  
            m=int(Rating.objects.filter(username=username,rate=5).count())
            n=int(Rating.objects.filter(username=username,rate=4).count())
            o=int(Rating.objects.filter(username=username,rate=3).count())
            p=int(Rating.objects.filter(username=username,rate=2).count())
            q=int(Rating.objects.filter(username=username,rate=1).count())
        
            tp= (5*m +4*n +3*o +2*p+q)/(m+n+o+p+q)
            tpx=round(tp*10)
            avg=tpx/10
            obj.rate=avg
            obj.save()
           
            return HttpResponseRedirect("/client/feedback")
    return render(request,"rate.html")

def feedback(request):
    if request.method=="POST":
        username=request.POST.get("username")
        feedback=request.POST.get("feedback")
        data=Feedback(username=username,feedback=feedback)
        data.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/client/home")
    return render(request,"feedback.html")

#template to be changed
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
        data=Message(user_sender=user_1,user_receiver=user_2,message=message)
        data.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/client/home")
   
    return render(request,"conversation_box.html",{'object1':message1}) 
#password-->2111_2010,username-->goat
# Create your views here.
