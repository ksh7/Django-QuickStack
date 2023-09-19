from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponse
 
# Create your views here.
 
def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'ecommerce/products.html',context)
 
@login_required
def placeOrder(request,i):
    form=createorderform(instance=request.user)
    if(request.method=='POST'):
        form=createorderform(request.POST,instance=request.user)
        if(form.is_valid()):
            form.save()
            return redirect('ecommerce:home')
    context={'form':form}
    return render(request,'ecommerce/placeOrder.html',context)
 
def addProduct(request):
    form=createproductform()
    if(request.method=='POST'):
        form=createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('ecommerce:home')
    context={'form':form}
    return render(request,'ecommerce/addProduct.html',context)
 