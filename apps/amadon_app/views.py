from django.shortcuts import render, redirect
from .models import *

# Product.objects.create(name="Dojo Tshirt", price=19.99)
# Product.objects.create(name="Dojo Sweater", price= 29.99)
# Product.objects.create(name="Dojo Cup", price = 4.99)
# Product.objects.create(name="Algorithm Book", price = 49.99)

product_id = {
    "0":0,
    "1":19.99,
    "2":24.99,
    "3":4.99,
    "4":49.99
}
def index(request):
    return render(request, 'amadon_app/index.html')

def process(request):

    if 'quantity' not in request.session:
        request.session['quantity'] = 0
    if 'total_cost' not in request.session:
        request.session['total_cost'] =0
    if 'small_cost' in request.session:
        request.session['small_cost']=0
    else:
        request.session['small_cost']=0
    
    if request.POST['quantity1'] !=0:
        q1= int(request.POST['quantity1']) * 19.99
    else:
        q1=0

    if request.POST['quantity2']!=0:
        q2= int(request.POST['quantity2']) * 29.99
    else:q2=0

    if request.POST['quantity3'] !=0:
        q3= int(request.POST['quantity3']) * 4.99
    else:q3=0

    if request.POST['quantity4']!=0:
        q4= int(request.POST['quantity4']) * 49.99
    else:q4=0

    print('REQUEST.POST:', dict(request.POST))
    Total_Quantity= int(request.POST['quantity1'])+int(request.POST['quantity2'])+int(request.POST['quantity3'])+int(request.POST['quantity4'])
    Single_Cost= q1+q2+q3+q4
    Small_Cost= q1+q2+q3+q4
    print('SINGLE COST:', Single_Cost)
    request.session['quantity'] += Total_Quantity
    request.session['total_cost']+=Single_Cost
    request.session['small_cost']+=Small_Cost

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')