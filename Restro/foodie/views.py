from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import City,Restro,RestroItem,Order,OrderItem,OrderUpdate
from account.models import Address,Profile,Favourite
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from restroadmin.models import Notification,OrderReceived,RestroProfile

def index(req):
	city=City.objects.all()
	return render(req,"foodie/index.html",{"city":city})

def perfome_search(restro_item,search_query):
	count=0
	for query in search_query:
		if query in restro_item.name or query in restro_item.category or query in restro_item.restro.name or query in restro_item.restro.desc or query in restro_item.restro.location.name:
			count+=1
	return restro_item,count

def check_restro(restro_item,search_result):
			for item in search_result:
				if restro_item.restro == item.restro:
					return True
			return False

def error_404(req):
	return render(req,"foodie/404.html")

def search(req):
	if req.method=="POST":
		search_query=req.POST['search'].lower().split()
		city=req.POST['city']
		data=RestroItem.objects.filter(restro__location__city__name__icontains=city)
		search_result={}
		for r in data:
			restro_item,count=perfome_search(r,search_query)
			if count:
				if not check_restro(restro_item,search_result):
					search_result[restro_item]=count
		search_result=sorted(search_result.items(), key=lambda search_result: search_result[1], reverse=True)	
		search_result=dict(search_result)
		return render(req,"foodie/search.html",{"result":search_result,"query":req.POST['search'],"city":city})
	return HttpResponse("not get request!")

def restro_view(req,id):
	restro_item=RestroItem.objects.filter(restro__id=id)
	favourite=Favourite.objects.filter(profile__user__username=req.user.username) & Favourite.objects.filter(restro_id=id)
	if favourite:
		favourite=True
	else:
		favourite=False
	return render(req,"foodie/restro_view.html",{"restro_item":restro_item,"favourite":favourite})

@login_required(login_url="/account/login")
def checkout_step_1(req):
	if req.user.is_authenticated:
		address=Address.objects.filter(profile__user__username=req.user.username)
		return render(req,"foodie/checkout-step-1.html",{"address":address})
	return HttpResponse("user not login")

@login_required(login_url="/account/login")
def checkout_step_2(req,id):
	address=Address.objects.get(id=id)
	if req.method == "POST":
		cart_item_json=json.loads(req.POST['cart-item-json'])
		payment_mode=req.POST['payment-mode']
		card_name=req.POST['card-name']
		card_number=req.POST['card-number']
		card_exp_month=req.POST['card-exp-month']
		card_exp_year=req.POST['card-exp-year']
		card_cvv=req.POST['card-cvv']
		profile=Profile.objects.get(user__username=req.user.username)
		order=Order.objects.create(profile=profile,address=address)
		for item in cart_item_json:
			restroitem=RestroItem.objects.get(id=int(item[4:]))
			order_item=OrderItem.objects.create(orders_id=order.id,item=restroitem,qty=int(cart_item_json[item]["qty"]),order=order)
		restro_id=list(cart_item_json.values())[0]["restro_id"]
		restro_profile=RestroProfile.objects.get(restro__id=restro_id)
		order_received=OrderReceived.objects.create(restro_profile=restro_profile,order=order)
		Notification.objects.create(order_received=order_received,name="#{} order received from {}".format(order.id,order.profile.user.username))
		return render(req,"foodie/thanks.html",{"thanks":True})
	return render(req,"foodie/checkout-step-2.html",{"address":address})

@login_required(login_url="/account/login")
def add_address(req):
	if req.method == "POST":
		address=req.POST['address']
		area=req.POST['area']
		landmark=req.POST.get('landmark',"")
		tag=req.POST['tag']
		profile=Profile.objects.get(user__username=req.user.username)
		add=Address.objects.create(address=address,area=area,landmark=landmark,tag=tag,profile=profile)
		return redirect("/foodie/checkout-step-1")
	return render(req,"foodie/add_address.html")

@login_required(login_url="/account/login")
def orders(req):								#{ order1:[item1,item2], order2:[item3,item4] }
	orders=Order.objects.filter(profile__user__username=req.user.username).order_by('-id')
	order_data={}
	for order in orders:
		order_item=list(OrderItem.objects.filter(orders_id=order.id))
		order_update=OrderUpdate.objects.filter(order=order).order_by("-id")
		order_data[order]=[order_item,order_update]
	return render(req,"foodie/orders.html",{"order_data":order_data})

def check_update(req):
	data=json.loads(req.GET["data"])
	for order in data:
		new_update_length=len(OrderUpdate.objects.filter(order=order))
		if data[order]!=new_update_length:
			return JsonResponse({"update_exists":1})
	return JsonResponse({"update_exists":0})
@login_required(login_url="/account/login")
def addresses(req):
	addresses=Address.objects.filter(profile__user__username=req.user.username)
	return render(req,"foodie/addresses.html",{"addresses":addresses})

@login_required(login_url="/account/login")
def delete_address(req,id):
	Address.objects.filter(id=id).delete()
	return redirect("/foodie/addresses")

@login_required(login_url="/account/login")
def add_favourite(req,id):
	profile=Profile.objects.get(user__username=req.user.username)
	Favourite.objects.create(restro_id=id,profile=profile)
	return redirect('/foodie/restro-view/{}'.format(id))

@login_required(login_url="/account/login")
def delete_favourite(req,id):
	Favourite.objects.filter(restro_id=id).delete()
	return redirect('/foodie/restro-view/{}'.format(id))

@login_required(login_url="/account/login")
def favourites(req):
	favourites=Favourite.objects.filter(profile__user__username=req.user.username)
	favourite_restro=[]
	for favourite in favourites:
		favourite_restro.append(Restro.objects.get(id=favourite.restro_id))
	print(favourite_restro)
	return render(req,"foodie/favourites.html",{"favourite_restro":favourite_restro})
def cancel_order(req,id):
	order=Order.objects.get(id=id)
	order.cancelled=True
	order.save()
	OrderUpdate.objects.create(order=order,status="Order Cancelled",desc="order cancelled by customer")
	return redirect("/foodie/orders")	

@login_required(login_url="/account/login")
def payments(req):
	return redirect('/foodie/404')

@login_required(login_url="/account/login")
def track_order(req):
	return render(req,"foodie/track-order.html")