from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    usuario = request.user.username
    return render(request, 'accesibilidad360/index.html', {'usuario': usuario})