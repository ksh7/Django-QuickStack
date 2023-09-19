from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
 
class createorderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']
 
class createproductform(ModelForm):
    class Meta:
        model=Product
        fields='__all__'
 