from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Рендерит твой index.html
