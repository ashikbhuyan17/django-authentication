from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.forms import StudentRegistration, StudentLoginForm,StudentEditProfileForm
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.views import PasswordChangeForm

User = settings.AUTH_PROFILE_MODULE


def index(request):
    return render(request, 'index.html')


def student_reg_view(request):
    context = {}
    if request.POST:
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('student_reg')
        else:
            context['student_reg_form'] = form

    else:
        form = StudentRegistration()
        context['student_reg_form'] = form
    return render(request, 'student_reg.html', context)


def student_login_view(request):
    context = {}
    if request.POST:
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                next_url = request.GET.get('next', 'student_dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Wrong Credentials!!')
    else:
        form = StudentLoginForm()

    context['student_login_form'] = form
    return render(request, 'student_login.html', context)


def dashboard(request):
    return render(request, 'base.html')



def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Change Password Successful')
            return redirect('change_password')
        else:
            messages.error(request, 'The Password and  password confirmation does not match')
            return redirect('change_password')


    else:
        form = PasswordChangeForm(user=request.user)
        context={
            'form':form,
        }
    return render(request, 'partials/change_password.html', context)

def edit_profile_student(request):
    if request.method == 'POST':
        form = StudentEditProfileForm(request.POST, request.FILES, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successful')
            return HttpResponseRedirect(reverse('edit_profile'))
    else:
        form = StudentEditProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'partials/edit_profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')
