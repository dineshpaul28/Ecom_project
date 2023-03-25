from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import os
from .models import Product, Complained
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.

def error_404(request, exception):
    return render(request, 'nothing.html')


def home(request):
    prod = Product.objects.all()
    params = {
        'prod': prod
    }
    return render(request, 'home.html', params)


def contact(request):
    return render(request, 'contact-us.html')


def show(request, pk):
    prod = Product.objects.get(id=pk)
    params = {
        'prod': prod
    }
    return render(request, 'show.html', params)


def search(request):
    if request.method == 'GET':
        prod_name = request.GET['query']
        product = Product.objects.filter(prod_name__icontains=prod_name)
        context = {
            'product': product,
            'prod_name': prod_name,
        }

        return render(request, 'search.html', context)
    return render(request, 'home.html')


def customer_service(request):
    return render(request, 'customer-service.html')


def store_locator(request):
    return render(request, 'store-locator.html')


def led_bulb(request, slug):
    prod = Product.objects.filter(slug=slug)
    params = {
        'prod': prod
    }

    return render(request, 'led-bulb.html', params)


def sunlight_fans(request, slug):
    prod = Product.objects.filter(slug=slug)
    params = {
        'prod': prod
    }
    return render(request, 'fans.html', params)


def sunlight_inverter(request, slug):
    prod = Product.objects.filter(slug=slug)
    params = {
        'prod': prod
    }
    return render(request, 'sunlight_inverter.html', params)


def sunlight_cooler(request, slug):
    prod = Product.objects.filter(slug=slug)
    params = {
        'prod': prod
    }
    return render(request, 'sunlight_cooler.html', params)


def query_form(request):
    if request.method == 'POST':
        name = request.POST['name'].capitalize()
        email = request.POST['email']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        product = request.POST['product']
        mobile = request.POST['mobile']
        phone = request.POST['phone']
        complaint = request.POST['complaint']
        comp = Complained(name=name, email=email, address1=address1, address2=address2, city=city, product=product,
                          mobile=mobile, phone=phone, complaint=complaint)
        comp.save()
        html = render_to_string('contact-template.html',
                                {
                                    'name': name,
                                    'email': email,
                                    'address1': address1,
                                    'address2': address2,
                                    'product': product,
                                    'mobile': mobile,
                                    'complaint': complaint

                                })
        send_mail(
            'message from' + " " + name,
            complaint,
            'cartoonart28@gmai.com',
            ['dineshpaul28@gmail.com'],
            fail_silently=False,
            html_message=html
        )
        messages.success(request, 'Your request successfully submitted. We will get back to you soon.')
        return redirect('query-form')

    return render(request, 'query-form.html')


def products(request):
    prod = Product.objects.all()

    return render(request, 'products.html', {'prod': prod})


