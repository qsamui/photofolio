from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings 
from .models import Photographer, Category 
from .forms import ContactForm 


def index(request):
    photographer = Photographer.objects.first()
    categories = Category.objects.all()
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        to = [photographer.email] if (photographer and photographer.email) else [settings.DEFAULT_FROM_EMAIL]
        send_mail(
            subject=f'application from {name}',
            message=f'Contact: {email}\n\nMessage:\n{message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=to,
        )
        return redirect('index')
    return render(request, 'portfolio/index.html',{
        'photographer': photographer,
        'categories': categories,
        'form': form,
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    photographer = Photographer.objects.first()
    return render(request, 'portfolio/category_detail.html', {
        'category': category,
        'photographer': photographer,
    })










