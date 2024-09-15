from django.shortcuts import render
from .forms import LoginForm, RegistrationForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

        if user is not None:
            login(request, user)
            return render(request, 'notes/home.html')
        else:
            return HttpResponse('Invalid login')

    else:
        form=LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'notes/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            login(request, new_user)
            return render(request, 'notes/home.html')
    else:
        form=RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})