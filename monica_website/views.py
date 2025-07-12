from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def blog_list(request):
    return render(request, 'blog_list.html')

def blog_detail(request, slug):
    return render(request, 'blog_detail.html', {'slug': slug})

def events(request):
    return render(request, 'events.html')

def coaching(request):
    return render(request, 'coaching.html')

def mentorship(request):
    return render(request, 'mentorship.html')

def etiquette_training(request):
    return render(request, 'etiquette_training.html')

def counseling(request):
    return render(request, 'counseling.html')

def speaking(request):
    return render(request, 'speaking.html')
