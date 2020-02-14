from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'Construction/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'Construction/about.html', {'title': 'About'})


def services(request):
    return render(request, 'Construction/services.html')


def contact(request):
    return render(request, 'Construction/contact.html', {'title': 'Contact'})


def faq(request):
    return render(request, 'Construction/faq.html', {'title': 'FAQ'})


def pricing(request):
    return render(request, 'Construction/pricing.html', {'title': 'Pricing'})


def testimonials(request):
    return render(request, 'Construction/testimonials.html', {'title': 'Testimonials'})


def projects(request):
    return render(request, 'Construction/projects.html', {'title': 'Projects'})


def project(request):
    return render(request, 'Construction/projects-single.html', {'title': 'Projects-Single'})


def news(request):
    return render(request, 'Construction/news-single.html', {'title': 'News'})


def news2(request):
    return render(request, 'Construction/news-left-sidebar.html', {'title': 'News2'})


def gallery(request):
    return render(request, 'Construction/comm_gallery.html', {'title': 'Commercial Gallery'})


def gallery2(request):
    return render(request, 'Construction/private_gallery.html', {'title': 'Private-Dwellings Gallery'})