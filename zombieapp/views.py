from email import message
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced,User
from .forms import CustomerRegistrationForm, CustomerProfile
from django.contrib import messages
from django.views.generic.edit import DeleteView

class HomeView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html',
        {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles, 'laptops':laptops})

class ProductDetailView(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
    address = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':address,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data==None:
        mobiles = Product.objects.filter(category='M')
    
    if data == 'Samsung' or data == 'MI' or data =='Iphone' or data=='Nokia' or data == 'OnePlus':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def laptop(request, data=None):
    if data==None:
        laptop = Product.objects.filter(category='L')
    
    if data == 'HP' or data == 'ACER' or data =='Apple' or data=='Lenovo' or data == 'MSI':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    
    return render(request, 'app/laptop.html',{'laptops':laptop})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')



def CustomerDeletView(request, id):
    if request.method == 'POST':
        dl = User.objects.get(id=id)
        dl.delete()
    return render(request, 'app/profile.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfile()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
    
    def post(self,request):
        form = CustomerProfile(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form ,'active':'btn-primary'})
