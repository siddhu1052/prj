from django.shortcuts import render
from .form import *
from .models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views 
def home(request):
    y=category.objects.all()
    p=land.objects.all()
    q=built.objects.all()
    return render(request,'bricks/home.html',{"obj":p,"obj2":q,"y":y})

def land_details(request):
    if(request.method=='GET'):
        x=land_Form()
        return render(request,'bricks/land_details.html',{'form':x})
    else:
        x=land_Form(request.POST,request.FILES)
        if(x.is_valid()):
            x.save()
        return render(request,'bricks/land_details.html',{'form':x})

def built_details(request):
    if(request.method=='GET'):
        x=built_Form()
        return render(request,'bricks/built_details.html',{'form':x})
    else:
        x=built_Form(request.POST,request.FILES)
        if(x.is_valid()):
            x.save()
        return render(request,'bricks/built_details.html',{'form':x})

def properties(request):
    x=request.GET.get('category')
    obj=get_object_or_404(category, pk=x)
    # print (obj)
    p=land.objects.filter(cat__cat=obj.cat)
    q=built.objects.filter(cat__cat=obj.cat)
    y=category.objects.all()
    print(p.count())
    return render(request,'bricks/properties.html',{"obj":p,"obj2":q,"y":y,"current_cat":obj.cat})
    
def property_details(request,property_id):
    # property_id=request.GET.get('property_id')
    p_type=request.GET.get('p_type')
    is_land = True
    if p_type == "Built" :
        # print("Built")
        is_land=False
        obj=built.objects.filter(pk=property_id)
    else: 
        # print ("Unknown property")
        obj=land.objects.filter(pk=property_id)
    
    return render(request,'bricks/property_details.html',{"obj":obj[0],"is_land":is_land})