from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from App.models import Flavor, Order

# Create your views here.

# Function to render home page
def home(request):
    flavours = Flavor.objects.all()

    return render(request, "App/pages/home.html", context={
        'flavours': flavours,
    })

def order(request, flavour_id):
    flavour = Flavor.objects.get(id=flavour_id)

    if request.method == "POST":

        order = Order()

        name = request.POST.get('nameInput')
        email = request.POST.get('emailInput')
        size = request.POST.get('tamanhoInput')
        obs_message = request.POST.get('obsInput')

        order.flavour = flavour
        order.name = name
        order.email = email
        order.size = size
        order.obs_message = obs_message

        order.save()
        messages.success(request, 'Pedido solicitado com sucesso!')
        return HttpResponseRedirect('/')
    else:
        return render(request, "App/pages/order.html", context={
            'flavour': flavour,
        })