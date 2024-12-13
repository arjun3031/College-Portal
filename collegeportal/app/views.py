from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app.models import *
from django.contrib.auth import login
import os
from django.contrib.auth.decorators import login_required



# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def loginpage(request):
    return render(request,'login.html')

def signuppage(request):
    return render(request,'signup.html')

def usercreate(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        ages=request.POST['age']
        mobile=request.POST['phone']
        mail=request.POST['email']
        password=request.POST['pass']
        confirm=request.POST['cpass']
        img=request.FILES.get('img')
        cours=request.POST['course']
        if password==confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already exists')
                return redirect('signuppage')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=mail,password=password,username=username)
                user.save()
                u=User.objects.get(id=user.id)
                reg=Teacher(age=ages,phone=mobile,image=img,courses=cours,user=u)
                reg.save()
                return redirect('loginpage')
        else:
            messages.info(request,'Password is not matching')
            return redirect('signuppage')
    else:
        return render(request,'signuppage.html')


@login_required(login_url='homepage')
def adminhome(request):
    return render(request,'adminhome.html')

def userlog(request):
    if request.method=='POST':
        usname=request.POST['uname']
        passwrd=request.POST['password']
        user=auth.authenticate(username=usname,password=passwrd)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')
            else:
                auth.login(request,user)
                return redirect('teacherhome')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('loginpage')
    return render(request,'signuppage.html')

def logout(request):
    auth.logout(request)
    return redirect('homepage')

def courseadd(request):
    return render(request,'addcourse.html')

def addcourse(request):
    if request.method=='POST':
        courses=request.POST['cname']
        fee=request.POST['fees']
        c=Course(coursename=courses,fees=fee)
        c.save()
        return redirect('adminhome')
    
def showcourses(request):
    c=Course.objects.all()
    return render(request, 'managecourse.html', {'c1':c})

def editcourse(request,pc):
    crs=Course.objects.get(id=pc)
    return render(request,'editcourse.html',{'crs1':crs})

def updatecourse(request,uc):
    if request.method=='POST':
        c=Course.objects.get(id=uc)
        c.coursename=request.POST.get('cname')
        c.fees=request.POST.get('fees')
        c.save()
        return redirect('showcourses')
    return render(request,'editcourse.html') 

def deletecourse(request, cd):
    crs=Course.objects.get(id=cd)
    crs.delete()
    return redirect('showcourses')

def studentadd(request):
    c=Course.objects.all()
    return render(request,'addstudent.html',{'c1':c})

def addstudent(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        addrs=request.POST.get('address')
        ages=request.POST.get('age')
        dt=request.POST.get('date')
        image=request.FILES.get('img')
        course1=request.POST.get('cours')
        courses=Course.objects.get(id=course1)
        student=Student(studentname=name,address=addrs,age=ages,date=dt,image=image,course=courses)
        student.save()
        return redirect('adminhome') 

def managestudent(request):
    s=Student.objects.all()
    return render(request, 'managestudent.html', {'s1':s}) 

def editstdudent(request,es):
    std=Student.objects.get(id=es)
    crs=Course.objects.all()
    return render(request,'editstudent.html',{'std1':std,'crs1':crs})

def updatestudent(request,us):
    if request.method=='POST':
        s=Student.objects.get(id=us)
        s.studentname=request.POST.get('name')
        s.address=request.POST.get('address')
        s.age=request.POST.get('age')
        s.date=request.POST.get('date')
        crs=request.POST.get('cours')
        course1=Course.objects.get(id=crs)
        s.course=course1
        newimg=request.FILES.get('img')
        if newimg:
            if s.image:
                os.remove(s.image.path)
                s.image=newimg
        s.save()
        return redirect('managestudent')
    return render(request,'editstudent.html') 

def deletestudent(request, sd):
    std=Student.objects.get(id=sd)
    std.delete()
    return redirect('managestudent')

def manageteacher(request):
    t=Teacher.objects.all()
    return render(request, 'manageteacher.html', {'t1':t}) 

def deleteteacher(request, td):
    tchr=Teacher.objects.get(id=td)
    tchr.delete()
    return redirect('manageteacher')

@login_required(login_url='homepage')
def teacherhome(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request,'teacherhome.html',{'teacher': teacher})

def teacherprofile(request,tp):
    teacher=Teacher.objects.get(id=tp)
    return render(request,'teacherprofile.html',{'teacher1':teacher})

def editteacher(request, et):
    teacher=Teacher.objects.get(id=et)
    user=teacher.user 
    return render(request,'editteacher.html',{'th1': user,'tchr1':teacher})

def updateteacher(request, ut):
    t=Teacher.objects.get(id=ut)
    u=t.user
    if request.method=='POST':
        u.first_name=request.POST.get('fname')
        u.last_name=request.POST.get('lname')
        u.username=request.POST.get('uname')
        u.email=request.POST.get('email')
        u.save()
        t.age=request.POST.get('age')
        t.phone=request.POST.get('phone')
        selected_course = t.courses
        new_course = request.POST.get('course')
        if new_course:
            t.courses = new_course
        else:
            t.courses = selected_course        
        newimg=request.FILES.get('img')
        if newimg:
            if t.image:
                if os.path.isfile(t.image.path):
                    os.remove(t.image.path)
            t.image=newimg
        t.save()
        return redirect('teacherhome')
    return render(request, 'editteacher.html', {'th1': u, 'tchr1': t, 'selected_course': selected_course})


