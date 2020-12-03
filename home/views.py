from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from home import form_user
from django.contrib import auth
from django.contrib.auth.models import User
from .models import info

def Home(request):
    f=open('textfile/mob1.txt','r')
    img1=f.read()
    f.close()
    z=open('textfile/mob2.txt','r')
    ha1=z.read()
    z.close()
    f2=open('textfile/lap1.txt','r')
    img2=f2.read()
    f2.close()
    z2=open('textfile/lap2.txt','r')
    ha2=z2.read()
    z2.close()
    f3=open('textfile/smw1.txt','r')
    img3=f3.read()
    f3.close()
    z3=open('textfile/smw2.txt','r')
    ha3=z3.read()
    z3.close()
    f4=open('textfile/cam1.txt','r')
    img4=f4.read()
    f4.close()
    z4=open('textfile/cam2.txt','r')
    ha4=z4.read()
    z4.close()
    f5=open('textfile/other1.txt','r')
    img5=f5.read()
    f5.close()
    z5=open('textfile/other2.txt','r')
    ha5=z5.read()
    z5.close()
    f6=open('textfile/other4.txt','r')
    img6=f6.read()
    f6.close()
    z6=open('textfile/other5.txt','r')
    ha6=z6.read()
    z6.close()
    f7=open('textfile/cam4.txt','r')
    img7=f7.read()
    f7.close()
    z7=open('textfile/cam5.txt','r')
    ha7=z7.read()
    z7.close()
    f8=open('textfile/mob4.txt','r')
    img8=f8.read()
    f8.close()
    z8=open('textfile/mob5.txt','r')
    ha8=z8.read()
    z8.close()
    f9=open('textfile/smw4.txt','r')
    img9=f9.read()
    f9.close()
    z9=open('textfile/smw5.txt','r')
    ha9=z9.read()
    z9.close()
    f10=open('textfile/lap4.txt','r')
    img10=f10.read()
    f10.close()
    z10=open('textfile/lap5.txt','r')
    ha10=z10.read()
    z10.close()
    return render(request,'home.html',{'x':img1,'z':ha1,'x2':img2,'z2':ha2,'x3':img3,'z3':ha3,'x4':img4,'x5':img5,'z4':ha4,'z5':ha5,'x6':img6,'z6':ha6,'x7':img7,'z7':ha7,
    'x9':img9,'z9':ha9,'x8':img8,'z8':ha8,'x10':img10,'z10':ha10})

def login(request):
    if request.method=='POST':
        user_fm=form_user.logindata(data=request.POST)
        if user_fm.is_valid():
            uname=user_fm.cleaned_data['username']
            upass=user_fm.cleaned_data['password']
            user=auth.forms.authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                return render(request,'account.html')
    else:
            user_fm=form_user.logindata()
    return render(request,'login.html',{'fm':user_fm})

def signup(request):
    if request.method=="POST":
        fm=form_user.data(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'account.html')
    else:
        fm=form_user.data()
        return render(request,'signup.html',{'fm':fm})

def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            user_acc=form_user.datauser(request.POST,instance=request.user)
            if user_acc.is_valid():
                user_acc.save()
                return render(request,'editprofile.html',{'data':user_acc})   
        else:
            user_acc=form_user.datauser(instance=request.user)
            return render(request,'editprofile.html',{'data':user_acc}) 
    else:
        return HttpResponseRedirect('login')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

def password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=form_user.passform(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('profile')
        else:
            fm=form_user.passform(request.user)
            return render(request,'password.html',{'fm':fm})
    else:
        return HttpResponseRedirect('profile')

def super(request):
    if request.method=="POST":
        fm=form_user.newform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            x=fm.cleaned_data['usertext']
            return render(request,'article.html',{'x':x})
    else:
        fm=form_user.newform()
        return render(request,'article.html',{'fm':fm})

def lap(request):
    f=open('textfile/lap1.txt','r')
    x=f.read()
    h=open('textfile/lap2.txt','r')
    y=h.read()
    u=open('textfile/lap3.txt','r')
    z=u.read()
    u.close()
    f.close()
    h.close()
    return render(request,'mob.html',{'x':x,'y':y,'z':z})

def mob(request):
    f=open('textfile/mob1.txt','r')
    x=f.read()
    h=open('textfile/mob2.txt','r')
    y=h.read()
    u=open('textfile/mob3.txt','r')
    z=u.read()
    u.close()
    f.close()
    h.close()
    return render(request,'mob.html',{'x':x,'y':y,'z':z})

def camera(request):
    f=open('textfile/cam1.txt','r')
    x=f.read()
    h=open('textfile/cam2.txt','r')
    y=h.read()
    u=open('textfile/cam3.txt','r')
    z=u.read()
    u.close()
    f.close()
    h.close()
    return render(request,'mob.html',{'x':x,'y':y,'z':z})

def smartwatch(request):
    f=open('textfile/smw1.txt','r')
    x=f.read()
    h=open('textfile/smw2.txt','r')
    y=h.read()
    u=open('textfile/smw3.txt','r')
    z=u.read()
    u.close()
    f.close()
    h.close()
    return render(request,'mob.html',{'x':x,'y':y,'z':z})

def others(request):
    f=open('textfile/mob4.txt','r')
    x=f.read()
    h=open('textfile/mob5.txt','r')
    y=h.read()
    u=open('textfile/mob6.txt','r')
    z=u.read()
    u.close()
    f.close()
    h.close()
    return render(request,'mob.html',{'x':x,'y':y,'z':z})

def save_data(request):
    if request.user.is_superuser:
        if request.method=="POST":
            fm=form_user.newform(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                x=int(fm.cleaned_data['article_no'])
                x1=fm.cleaned_data['image_name']
                x2=fm.cleaned_data['catgory']
                x3=fm.cleaned_data['heading']
                x4=fm.cleaned_data['article']
                if x2=="laptop":
                    if x==1:
                        f=open('textfile/lap1.txt','w')
                        f.write(x1)
                        g=open('textfile/lap2.txt','w')
                        g.write(x3)
                        h=open('textfile/lap3.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                    else:
                        f=open('textfile/lap4.txt','w')
                        f.write(x1)
                        g=open('textfile/lap5.txt','w')
                        g.write(x3)
                        h=open('textfile/lap6.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                elif x2=="mobile":
                    if x==1:
                        f=open('textfile/mob1.txt','w')
                        f.write(x1)
                        g=open('textfile/mob2.txt','w')
                        g.write(x3)
                        h=open('textfile/mob3.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                    else:
                        f=open('textfile/mob4.txt','w')
                        f.write(x1)
                        g=open('textfile/mob5.txt','w')
                        g.write(x3)
                        h=open('textfile/mob6.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                elif x2=="camera":
                    if x==1:
                        f=open('textfile/cam1.txt','w')
                        f.write(x1)
                        g=open('textfile/cam2.txt','w')
                        g.write(x3)
                        h=open('textfile/cam3.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                    else:
                        f=open('textfile/cam4.txt','w')
                        f.write(x1)
                        g=open('textfile/cam5.txt','w')
                        g.write(x3)
                        h=open('textfile/cam6.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                elif x2=="smartwatch":
                    if x==1:
                        f=open('textfile/smw1.txt','w')
                        f.write(x1)
                        g=open('textfile/smw2.txt','w')
                        g.write(x3)
                        h=open('textfile/smw3.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                    else:
                        f=open('textfile/smw4.txt','w')
                        f.write(x1)
                        g=open('textfile/smw5.txt','w')
                        g.write(x3)
                        h=open('textfile/smw6.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                else:
                    if x==1:
                        f=open('textfile/other1.txt','w')
                        f.write(x1)
                        g=open('textfile/other2.txt','w')
                        g.write(x3)
                        h=open('textfile/other3.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
                    else:
                        f=open('textfile/other4.txt','w')
                        f.write(x1)
                        g=open('textfile/other5.txt','w')
                        g.write(x3)
                        h=open('textfile/other6.txt','w')
                        h.write(x4)
                        g.close()
                        f.close()
                        h.close()
            return render(request,'ok.html')
    else:
        return render(request,'notok.html')

def news1(request):
    f=open('textfile/cam1.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/cam2.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/cam3.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news2(request):
    f=open('textfile/other1.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/other2.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/other3.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news3(request):
    f=open('textfile/other4.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/other5.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/other6.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news4(request):
    f=open('textfile/cam4.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/cam5.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/cam6.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news5(request):
    f=open('textfile/mob1.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/mob2.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/mob3.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news6(request):
    f=open('textfile/lap1.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/lap2.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/lap3.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news7(request):
    f=open('textfile/smw1.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/smw2.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/smw3.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news8(request):
    f=open('textfile/mob4.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/mob5.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/mob6.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news9(request):
    f=open('textfile/smw4.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/smw5.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/smw6.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})

def news10(request):
    f=open('textfile/lap4.txt','r')
    img=f.read()
    f.close()
    z=open('textfile/lap5.txt','r')
    ha=z.read()
    z.close()
    g=open('textfile/lap6.txt','r')
    fa=g.read()
    g.close()
    return render(request,'news.html',{'x':img,'y':ha,'z':fa})