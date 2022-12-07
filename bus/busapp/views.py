from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import BusListItem 
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    return render(request, 'index.html')



def appView(request):
    all_bus_items = BusListItem.objects.all()
    return render(request, 'app.html',  {'all_items':all_bus_items})


def addView(request):
    # x = request.POST.get('todotext')
    new_item = BusListItem()
    new_item.content = request.POST.get('content')
    new_item.last_name=request.POST.get('last_name')
    new_item.date=request.POST.get('date')
    new_item.city=request.POST.get('city')
    new_item.save()
    
    
    return HttpResponseRedirect('/end/') 

