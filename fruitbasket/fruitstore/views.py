from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request,'buyer.html',{'products':products})


from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    options = Category.objects.all()
    context = {
        'product': product,
        'options': options
    }
    if request.method == 'POST':
        product.product_name = request.POST.get('productname')
        product.product_price = request.POST.get('product_price')
        product.product_pic = request.FILES.get('product_pic')

        # Retrieve category_id from POST data
        category_id = request.POST.get('category_id')
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            # Handle case where category does not exist
            # You can add your own logic here, like showing an error message
            category = None
        
        product.category = category
        product.save()
        # Redirect to some page after saving the product
        # You might want to redirect to product detail page or somewhere else
        return redirect('product_detail', pk=pk)
    else:
        return render(request,'product_edit.html',context)

    
    


def seller_index(request):
    user = User.objects.get(email=request.session['email'])
    products = Product.objects.filter(user=user)
    return render(request,'index.html',{'products':products})

def vegetables(request,foo):

    user = User.objects.get(email= request.session['email'])
    category = Category.objects.get(category_name = foo)
    
    
    products = Product.objects.filter(category=category,user=user )

    return render(request,'index.html',{'products':products})


def Fruits(request,foo):

    user = User.objects.get(email= request.session['email'])
    category = Category.objects.get(category_name = foo)
    
    
    products = Product.objects.filter(category=category,user=user )

    return render(request,'index.html',{'products':products})


def Bread(request,foo):

    user = User.objects.get(email= request.session['email'])
    category = Category.objects.get(category_name = foo)
    
    
    products = Product.objects.filter(category=category,user=user )

    return render(request,'index.html',{'products':products})


def Meat(request,foo):

    user = User.objects.get(email= request.session['email'])
    category = Category.objects.get(category_name = foo)
    
    
    products = Product.objects.filter(category=category,user=user )
    return render(request,'index.html',{'products':products})


def all_products(request):

    return redirect('seller_index')




def product_detail(request,pk):
    user = User.objects.get(email=request.session['email'])
    products = Product.objects.get(pk=pk,user = user)

    
    return render(request,'product_detail.html',{'product':products})



    




def add_product(request):
    user=User.objects.get(email=request.session['email'])
    if request.method == "POST":
        # category_id = request.POST.get('category')
        product_name = request.POST.get('productname')
        product_price = request.POST.get('product_price')
        product_pic = request.FILES.get('product_pic')
        category_id = request.POST.get('category')



        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            # Handle the case where the category with the provided ID does not exist
            return redirect('error_page')  # Redirect to an error page or handle it accordingly

        Product.objects.create(
                user=user,
                product_name=product_name,
                product_price=product_price,
                product_pic=product_pic,
                category = category
                
            )
        msg = 'you product added successfully'
        option = Category.objects.all()
    
            
        return render(request,'add_product.html',{'option': option})
    else:
        # Fetch available categories for the user to choose from
        option = Category.objects.all()
        return render(request, 'add_product.html', {'option': option})
    







 # Import your profile model
def login(request):

    if request.method == 'POST':
        try:
            user=User.objects.get(email= request.POST['email'])
            
            
            if user.usertype =='buyer':
            
                
                if user.password == request.POST['pwd']:
                    request.session['email']= user.email
                    request.session['password']= user.password
                    
                    return redirect('index')
                else:
                    msg='Password does not mached'
                    
                    return render(request,'login.html',{'msg':msg})
            
            else: 
                
                if user.password == request.POST['pwd']:
                    request.session['email']= user.email
                    request.session['password']=user.password

                    return redirect('seller_index')
                
                else:
                    msg='Password does not mached'
                    
                    return render(request,'login.html',{'msg':msg})
                
                
                
        except:
            msg='User is not registerd'
            return render(request,'login.html',{'msg':msg})
        
    else:
        return render(request,'login.html')


    
    

        # If it's not a POST request, render the login page
        
                
                

        
       
    
def logout_profile(request):
   try:
       del request.session['email']
       del request.session['password']

       return render(request,'login.html')
   
   except:
       
       return render(request,'login.html')



def edit_details (request,pk):


    
    # Retrieve the logged-in user
    user = request.user
    
    # Determine if the user has a BuyerProfile or SellerProfile
    if hasattr(user, 'buyerprofile'):
        profile_instance = user.buyerprofile
        return render(request,'edit.html',{'profile_instance':profile_instance})
    elif hasattr(user, 'sellerprofile'):
        profile_instance = user.sellerprofile
        return
    else:
        # Handle case where user does not have any 
        return render(request,'login.html')
    


def register(request):
    if request.method == 'POST':

        try:
            User.objects.get(email= request.POST['email'])
            msg = 'email is already registerd'


            return render(request,'contact.html',{'msg':msg})
        
        except:
            if request.POST['pwd'] == request.POST['rpwd']:
                User.objects.create(

                    username = request.POST['username'],
                    email = request.POST['email'],
                    password = request.POST['pwd'],
                    usertype = request.POST['usertype'],

                )
                msg = 'User rigisterd successfully'


                return render(request,'contact.html',{'msg':msg})
            
            else :
                msg = "Password and comfirme Password does not mached."
                return render(request,'contact.html',{'msg':msg})
        
    else:
       return render(request,'contact.html')
    

# buyer code logics 

def buyer_product_detail(request,pk):
    flag =  False
    product = Product.objects.get(pk=pk)
    
    try:
        user=User.objects.get(email=request.session['email'])
        Whishlist.objects.get(user=user,product=product)
        flag = True
        return render(request,'buyer_product_detail.html',{'product':product,'flag':flag})
    except:
        flag= False
        return render(request,'buyer_product_detail.html',{'product':product,'flag':flag})


        
        

    


def add_to_whishlist(request,pk):

    try:
        user=User.objects.get(email=request.session['email'])
        product = Product.objects.get(pk=pk)
        Whishlist.objects.create(
            user = user,
            product=product
        )
        return redirect('index')
    
    except:
        return redirect('login')
    

def wishlist(request):
    try:
        user = User.objects.get(email=request.session.get('email'))
        wishlist = Whishlist.objects.filter(user=user)
        return render(request, 'wishlist.html', {'wishlist': wishlist})
    except User.DoesNotExist:
        return redirect('login')
    except ObjectDoesNotExist:
        # Handle the case where wishlist for the user does not exist
        return render(request, 'wishlist.html', {'wishlist': []})

def remove_wishlist(request,pk):
    user= User.objects.get(email=request.session['email'])
    product= Product.objects.get(pk=pk)

    Whishlist.objects.get(user=user,product=product).delete()
    return redirect('wishlist')

def wishlist_remove(request,pk):
    user= User.objects.get(email=request.session['email'])
    product= Product.objects.get(pk=pk)

    Whishlist.objects.get(user=user,product=product).delete()
    return redirect('wishlist')

def cart(request):
    net_price = 0
    user =  User.objects.get(email= request.session['email'])
    cart = Cart.objects.filter(user = user, payment_status= False)

    for i in cart:
        net_price = net_price + i.totol_price

    request.session['cart_count'] = len(cart)


    return render(request,'cart.html',{'net_price':net_price,'cart':cart})

def addcart(request,pk):
    user = User.objects.get(email = request.session['email'])
    product = Product.objects.get(pk=pk)

    Cart.objects.create(
        user = user,
        product= product,
        product_price = product.product_price,
        product_qty = 1,
        totol_price = product.product_price


    )
    return redirect('cart')


def change_qty(request):
    pk=int(request.POST['pk'])
    product_qty=int(request.POST['product_qty'])
    cart=Cart.objects.get(pk=pk)
    cart.totol_price = cart.product_price * product_qty
    cart.product_qty=product_qty
    cart.save()
    return redirect('cart')









    

 

    
            
        



