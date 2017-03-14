from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content': ['If want to contact me, mail me', 'titu.nahak@maplelabs.com']})

