from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Form_products
from django.contrib.auth.decorators import login_required

@login_required
def create_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form=Form_products(request.POST,request.FILES)

            if form.is_valid():
                Products.objects.create(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    stock=form.cleaned_data['stock'],
                    image=form.cleaned_data['image'],
                )
                return redirect(list_products)
        
        elif request.method == 'GET':
            form= Form_products()
            context={'form':form}
            return render(request,"products/new_product.html",context=context)
    else: return redirect ('login-super')

def list_products(request):
    all_products= Products.objects.all()
    context={
        'all_products':all_products
    }
    return render(request,"products/all_products.html",context=context)

def search_products(request):
    search=request.GET['search']
    products= Products.objects.filter(name__icontains=search)
    context={'products':products}
    return render(request, 'products/search-products.html', context=context)

def delete_products(request,pk):
    if request.method == 'GET':
        products= Products.objects.get(pk=pk)
        context={'products':products}
        return render (request, 'products/delete_products.html',context=context)
    elif request.method == 'POST':
        products= Products.objects.get(pk=pk)
        products.delete()
        return redirect (list_products)

def update_products(request,pk):
    if request.method == 'POST':
        form=Form_products(request.POST,request.FILES)

        if form.is_valid():
            product=Products.objects.get(id=pk)
            product.name=form.cleaned_data['name']
            product.price=form.cleaned_data['price']
            product.stock=form.cleaned_data['stock']
            product.image=form.cleaned_data['image']
            product.save()

            return redirect (list_products)
    
    elif request.method == 'GET':
        product=Products.objects.get(id=pk)
        form=Form_products(initial={'name':product.name,
                                    'price':product.price,
                                    'stock':product.stock,
                                    })
        context={'form':form, 'product':product}
        return render (request, 'products/update_products.html',context=context)