from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Сисидрайв'
    context = {
        'title': title,
        'text': 'Главная страница'
    }
    return render(request, template, context)