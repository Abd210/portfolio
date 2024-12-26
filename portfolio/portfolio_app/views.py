# portfolio/portfolio_app/views.py

from django.shortcuts import render, redirect
from .models import (
    SocialLink, AboutMe, Education, Experience,
    Project, Certification, Skill, ContactInfo
)
from .forms import ContactForm
from django.contrib import messages

def home(request):
    social_links = SocialLink.objects.all()
    about_me = AboutMe.objects.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    skills = Skill.objects.all()
    contact_info = ContactInfo.objects.first()
    context = {
        'social_links': social_links,
        'about_me': about_me,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
        'certifications': certifications,
        'skills': skills,
        'contact_info': contact_info,
    }
    return render(request, 'portfolio_app/home.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form})
