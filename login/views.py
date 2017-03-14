from django.shortcuts import render


# Create your views here.
def loginform(request):
    return render(request, 'login/login.html')