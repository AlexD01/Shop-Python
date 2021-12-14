from django.shortcuts import render,redirect
from app.models import Section,Product,Storage


def index(request):
    products=Product.objects.order_by("?").all()[:5]
    sections=Section.objects.all()
    storages=Storage.objects.all()

    return render(request, 'app/index.html', {'products': products,'sections':sections,'storages':storages})


def section(request, name):
     try:
        sections=Section.objects.get(name=name)
        products=sections.product_set.all()
        return render(request, 'app/section.html', {'products': products})
     except Exception as e:
        return redirect('/')

def storage(request, name):
    try:
        storages=Storage.objects.get(name=name)
        products=storages.product.all()
        return render(request, 'app/storage.html', {'products': products})
    except Exception as e:
        return redirect('/')


def detail(request, id):
    product=Product.objects.filter(id=id)
    
    return render(request, 'app/detail.html', {'product': product})
