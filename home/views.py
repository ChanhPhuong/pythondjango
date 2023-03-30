from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.shortcuts import render , redirect
from django.http import HttpResponse
from category.models import Category
from home.forms import CustomUserForm

from product.models import Product
# Create your views here.
def cart (request):
     return render(request , 'page/cart.html')
def index (request):
    product = Product.objects.all()
    listcategory = Category.objects.all()
    return render(request, 'page/home.html', {'product':product , 'category':listcategory}  )

def category (request):
    listcategory = Category.objects.all()
    return render(request, 'page/base.html', { 'category':listcategory}  )

def productdetails(request, id ):
    productdetails = Product.objects.get(id=id)
    listcategory = Category.objects.all()
    categoryall = Product.objects.filter( categoryId = productdetails.categoryId).exclude(id = productdetails.id)[:4]
    return render(request, 'page/productdetails.html' , {'productdetails': productdetails , 'category':listcategory , 'categoryall' :categoryall})

def categoryId(request, id):
    productall = Product.objects.filter(categoryId = id)
    categorall = Category.objects.get(id = id)
    listcategory = Category.objects.all()
    return render(request, 'page/productcategory.html' , {'productcategory': productall , 'categorys':categorall , 'category':listcategory})

# def productall (request):
#     if request.method=='GET':
#         sortby = request.GET.get('sortby')
#         if sortby:
#             listcategory = Category.objects.all()
#             ShowAllProduct = Product.objects.filter().order_by('price')
#             return render(request, 'page/productall.html', {'ShowAllProduct':ShowAllProduct , 'category':listcategory}  ) 
#         else:

#             productall = Product.objects.all()
#             listcategory = Category.objects.all()
#             return render(request, 'page/productall.html', {'productall':productall ,'ShowAllProduct':ShowAllProduct , 'category':listcategory}  ) 

def productall (request):
            
            ShowAllProduct = Product.objects.filter().order_by('-price')
            productall = Product.objects.all()
            listcategory = Category.objects.all()
            return render(request, 'page/productall.html', {'productall':productall ,'ShowAllProduct':ShowAllProduct , 'category':listcategory}  ) 

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            product = Product.objects.filter(name__contains=query)
            listcategory = Category.objects.all()
            return render(request , 'page/search.html', {'product': product, 'category':listcategory})
        else:
            print("No information to show")
            return request(request, 'page/search.html', {})
        

# def regiser(request):
#     form = CustomUserForm()
#     if request.method =='POST':
#          form = CustomUserForm(request.POST)
#          if form.is_valid():
#               form.save()
#               messages.success(request, "Registered Successfully! Login to Continue")
#               return redirect('/login')
#     context = {'form': form}
#     return render(request , 'page/regiser.html', context)

# def loginpage(request):
#     if  request.user.is_authenticated:
#          messages.warning(request, "You are already logged in")
#          return redirect('/')
#     else:
#         if request.method == 'POST':
#             name = request.POST.get('username') 
#             passwd = request.POST.get('password') 

#             user = authenticate(request, username=name, passwrod=passwd)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Logged in Successfully")
#                 return redirect('/regiser')
#             else:
#                 messages.error(request, "Invalid Username or Passwrod")
#                 return redirect('/login')      
#         return render(request, "page/login.html")
# def logoutpage(request):
#     if request.user.is_authenticated:
#         logout(request)
#         messages.success(request, "Logged out Successfully")
#     return redirect("/")
# def ShowAllProduct(request):
#     ShowAllProduct = Product.objects.order_by('-price')
#     return render(request, 'page/productall.html', {'ShowAllProduct':ShowAllProduct}  )