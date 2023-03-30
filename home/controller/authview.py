from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.shortcuts import render , redirect
from home.forms import CustomUserForm

# Create your views here.      
def registerr(request):
    form = CustomUserForm()
    if request.method =='POST':
         form = CustomUserForm(request.POST)
         if form.is_valid():
              form.save()
              messages.success(request, "Registered Successfully! Login to Continue")
              return redirect('/loginpage')
    context = {'form': form}
    return render(request , 'page/regiser.html', context)

def loginpagee(request):
    if  request.user.is_authenticated:
         messages.warning(request, "You are already logged in")
         return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username') 
            passwd = request.POST.get('password') 

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request, "Invalid Username or Passwrod")
                return redirect('/loginpage')      
        return render(request, "page/login.html")
def logoutpagee(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect("/")
# def ShowAllProduct(request):
#     ShowAllProduct = Product.objects.order_by('-price')
#     return render(request, 'page/productall.html', {'ShowAllProduct':ShowAllProduct}  )