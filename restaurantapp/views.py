from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def admin_page(request):
    return render(request, 'admin_page.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')