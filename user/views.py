from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registrations/register.html'
    success_url = reverse_lazy('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,('There was an error logging in!'))
            return redirect('login')
    else:
        return render(request, 'registrations/login.html',{})
    

def logout_user(request):
    logout(request)
    messages.success(request,('Logged Out! See ya'))
    return redirect('home')
    
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registrations/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user