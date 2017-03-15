from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm


# Create your views here.
def index(request):
    return render(request, 'login/login.html')



class UserLogin(View):
    pass


class UserFormView(View):
    form_class = UserForm
    template_name = 'login/registration.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # Process from Data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #email = form.cleaned_data['email']
            user.set_password(password)
            #user.set_email(email)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active():
                    login(request, user)

                    return redirect('personal:index')

        return render(request, self.template_name, {'form': form})
