from django.shortcuts import render
def index(request):
        return render(request, 'web/index.html', {})
def tramites(request):
        return render(request, 'web/tramites.html', {})

# Create your views here.
