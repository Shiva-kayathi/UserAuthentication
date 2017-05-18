from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views.generic import View
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def index(request):
    template_name = 'login/index.html'
    return render(request, template_name)

def UserLogoutView(request):
    logout(request)
    return redirect('login:index')

# Create your views here.
class UserFormView(View):
    form_class = UserForm
    template_name = 'login/registration_form.html'

    #display blank data
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #display form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #saving user dat, not updating database record
            user = form.save(commit=False)

            #clean (normalized) data
            #unify data like oonsistent date across

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                #user is not disabled or abnned
                if user.is_active:
                    login(request, user)
                    return redirect('/app')

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = LoginForm
    template_name = 'login/login.html'

    # display blank data
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # display form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
               # form.errors = "User not found"
            # if not user.check_password(password):
            #     form.password.error = "Incorrect Password"

                # user is not disabled or abanned
                if user.is_active:
                    login(request, user)
                    return redirect('/app')
            # else:
            #     raise forms.ValidationError("User not found")

        return render(request, self.template_name, {'form': form})


