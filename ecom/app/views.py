from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .forms import CustomerProfileForm, CustomerRegistrationForm
from .models import Customer, product
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        products = product.objects.filter(category=val)
        title = product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        products = product.objects.filter(title=val)
        title = product.objects.filter(category=products[0].category).values('title')
        return render(request,"app/category.html",locals())
        
class ProductDetail(View):
    def get(self,request,pk):
        products = product.objects.get(pk=pk)
        return render(request,"app/product_detail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,"app/customer_registration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
             form.save()
             messages.success(request,"Congratulation! User Registration Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"app/customer_registration.html",locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"app/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state  = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation! Profile Saved Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"app/profile.html",locals())
        
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"app/address.html",locals())
class updateAddress(View):
    def get(self, request,pk):
        form = CustomerProfileForm()
        return render(request,"app/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        return render(request,"app/updateAddress.html",locals())