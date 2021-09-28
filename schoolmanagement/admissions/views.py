from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse

from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required,permission_required

from .filters import *

from django.contrib import messages
from django.contrib.auth.models import User,auth
from .helpers import send_forgot_password_mail




def register(request):

    if request.method == 'POST':

         username = request.POST['username']
         email = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']



         if password1 == password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username already exists')
               return redirect('register')

            elif  User.objects.filter(email=email).exists():
               messages.info(request,'Email id already exists')
               return redirect('register')

            else:
               user = User.objects.create_user(username=username,email=email,password=password1)
               user.save();

               profile_obj = Profile.objects.create(user = user)
               profile_obj.save()

               print('User Created')
               return redirect('/')

         else:
               messages.info(request,'password must match')
               return redirect('register')

    else:

       return render (request,'registration/register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

import uuid
def ForgotPassword(request):
    try:
        if request.method == 'POST' :
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username')
                return redirect('ForgotPassword')

            user = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user = user)
            profile_obj.forgot_password_token = token
            profile_obj.save()

            send_forgot_password_mail(user.email , token )
            messages.success(request, 'Reset link has sent to email address')
            return redirect('ForgotPassword')


    except Exception as e:
        print(e)
    return render (request, 'registration/forgot-password.html')



def ChangePassword(request , token ):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forgot_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')


            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')


            user = User.objects.get(id = user_id)
            user.set_password(new_password)
            user.save()
            return redirect('/')

    except Exception as e:
        print(e)
    return render (request, 'registration/change-password.html' , context)










#function based views
@login_required
def homepage(request):
    return render(request,'index.html')

@login_required
def addadmission(request):

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentModelForm()
            return redirect("/ad/newadm/")

    else:
        form = StudentModelForm()
        result = Student.objects.all()

        #filters
        myFilter = StudentFilter(request.GET , queryset=result)
        result = myFilter.qs


    return render(request,'admissions/add-admission.html', {'form':form , 'allstudents':result , 'myFilter':myFilter});

@login_required
def updatestudent(request,id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form':form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect("/ad/newadm/")


    return render(request,'admissions/update-student.html', dict);


@login_required
def deletestudent(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    messages.info(request,'Student details successfully deleted !')
    return redirect("/ad/newadm/")


@login_required
def addfee(request):

    if request.method == 'POST':
        form = FeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeeModelForm()
            return redirect("/ad/newfee/")

        else:
            messages.info(request,'Student fee details already exists !')
            return redirect("/ad/newfee/")


    else:
        form = FeeModelForm()
        result = Fee.objects.all()

        #filters
        myFilter = FeeFilter(request.GET , queryset=result)
        result = myFilter.qs


    return render(request,'admissions/fee-details.html', {'form':form , 'allfees':result , 'myFilter':myFilter});


@login_required
def updatefee(request,id):
    s = Fee.objects.get(id=id)
    form = FeeModelForm(instance=s)
    dict = {'form':form}

    if request.method == 'POST':
        form = FeeModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect("/ad/newfee/")

    return render(request,'admissions/update-fee.html', dict);

@login_required
def deletefee(request,id):
    s = Fee.objects.get(id=id)
    s.delete()
    return redirect("/ad/newfee/")



@login_required
def addteacher(request):

    if request.method == 'POST':
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = TeacherModelForm()
            return redirect("/ad/newteacher/")

    else:
        form = TeacherModelForm()
        result = Teacher.objects.all()


    return render(request,'admissions/add-teacher.html', {'form':form , 'allteachers':result});

@login_required
def updateteacher(request,id):
    s = Teacher.objects.get(id=id)
    form = TeacherModelForm(instance=s)
    dict = {'form':form}

    if request.method == 'POST':
        form = TeacherModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect("/ad/newteacher/")


    return render(request,'admissions/update-teacher.html', dict);


@login_required
def deleteteacher(request,id):
    s = Teacher.objects.get(id=id)
    s.delete()
    return redirect("/ad/newteacher/")



@login_required
def id_generator(request):
    form = Id_cardModelForm
    context = {'form':form}

    if request.method == 'POST':
        form = Id_cardModelForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        return id_card(request)
    return render (request , 'admissions/id_generator.html', context)


@login_required
def id_card(request):
    context = {
        'cards' : Id_card.objects.all()
    }
    return render (request , 'admissions/id_card.html' , context)


@login_required
def detail(request , id):
    context = {
        'card' : get_object_or_404(Id_card , pk=id)
    }

    return render (request , 'admissions/detail.html' , context)

@login_required
def deleteid_card(request,id):
    s = Id_card.objects.get(id=id)
    s.delete()
    return redirect("/ad/id_card/")


def Contact(request):
    return render(request,'contact.html')
