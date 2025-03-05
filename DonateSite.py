from django.shortcuts import render
from django.urls import path

# Views

def home(request):
    return render(request, 'home.html', {
        'title': 'Welcome to Simon Carter's Mission',
        'bio': "Simon Carter, also known as the Workout Minister, is a transformational fitness coach and motivational speaker. With a background in Golden Gloves boxing and years of experience training at-risk youth, celebrities, and military personnel, Simon has dedicated his life to helping others achieve physical, mental, and spiritual growth. His unique approach combines fitness, psychology, and personal development to create lasting change."
    })

def donate(request):
    return render(request, 'donate.html', {
        'title': 'Support the Mission',
        'visuals': 'bold donation banners, impact stories, and a secure payment portal'
    })

def ebook(request):
    return render(request, 'ebook.html', {
        'title': 'Free Motivational eBook',
        'visuals': 'high-quality cover images, testimonials, and a direct download button'
    })

def community(request):
    return render(request, 'community.html', {
        'title': 'Join Our Community',
        'visuals': 'interactive message board, recent donor highlights, and engagement features'
    })

def contact(request):
    return render(request, 'contact.html', {
        'title': 'Get in Touch',
        'visuals': 'clean contact form, direct social media links, and a warm call-to-action'
    })

# URL Patterns
urlpatterns = [
    path('', home, name='home'),
    path('donate/', donate, name='donate'),
    path('ebook/', ebook, name='ebook'),
    path('community/', community, name='community'),
    path('contact/', contact, name='contact'),
]
