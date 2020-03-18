from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import RestroProfile,OrderReceived,Notification
from foodie.models import OrderItem,OrderUpdate,Order
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(req):
	if req.user.is_authenticated:
		return redirect("/restaurant/dashboard")
	if req.method=="POST":
		email_or_tel=req.POST['email_or_tel']
		pwd=req.POST['pwd']
		restro_id=req.POST['restro_id']
		user=auth.authenticate(restro_id=restro_id,username=email_or_tel,password=pwd)
		if user is not None:
			auth.login(req,user)
			return redirect("/restaurant/dashboard")
		else:messages.error(req,"User Not Found")
	return render(req,"restroadmin/login.html")

def logout(req):
	if req.user.is_authenticated:
		auth.logout(req)
		return redirect("/restaurant/login")

@login_required(login_url="/restaurant/login")
def dashboard(req):
	order_received=OrderReceived.objects.filter(restro_profile__user=req.user)
	total_order=0
	delivered_order=0
	cancelled_order=0
	order_being_prepared=0
	order_pickup=0
	order_confirmed=0
	for received_order in order_received:
		if received_order.order.ordered or received_order.order.cancelled:
			if received_order.order.ordered:
				delivered_order+=1
			if received_order.order.cancelled:
				cancelled_order+=1
		else:
			try:
				order_update=OrderUpdate.objects.filter(order=received_order.order).order_by("-id")[0]
				if order_update.status == "Order Being Prepared":
					order_being_prepared+=1
				elif order_update.status == "Order Pickup":
					order_pickup+=1
				elif order_update.status == "Order Confirmed":
					order_confirmed+=1
			except:
				pass
		total_order+=1
	data={
			"total_order":total_order,"delivered_order":delivered_order,
			"cancelled_order":cancelled_order,"order_confirmed":order_confirmed,
			"order_being_prepared":order_being_prepared,"order_pickup":order_pickup
		}
	return render(req,"restroadmin/dashboard.html",data)

def order_detail(req,id):	#id => order received id
	try:
		order_received=OrderReceived.objects.get(restro_profile__user=req.user,id=id)
		order_item=OrderItem.objects.filter(order=order_received.order)
		order_update=OrderUpdate.objects.filter(order=order_received.order).order_by("-id")
		print(order_received.order.ordered)
		#for insert order update
		if req.method == 'POST':
			desc=req.POST['desc']
			status=req.POST['status']
			print(status)
			if status=="Order Delivered":
				Order.objects.filter(id=order_received.order.id).update(ordered=True)
				order_received=OrderReceived.objects.get(restro_profile__user=req.user,id=id)
				print(order_received.order.ordered)
				OrderUpdate.objects.create(order=order_received.order,status=status,desc=desc)
			elif status=="Order Cancelled":
				Order.objects.filter(id=order_received.order.id).update(cancelled=True)
				order_received=OrderReceived.objects.get(restro_profile__user=req.user,id=id)
				print(order_received.order.cancelled)
				cancelled_desc=desc+" by restaurant"
				OrderUpdate.objects.create(order=order_received.order,status=status,desc=cancelled_desc)
			else:
				OrderUpdate.objects.create(order=order_received.order,status=status,desc=desc)
			return render(req,"restroadmin/order-detail.html",{"order_received":order_received,"order_items":order_item,"order_updates":order_update,"is_update":True})			
		return render(req,"restroadmin/order-detail.html",{"order_received":order_received,"order_items":order_item,"order_updates":order_update})
	except Exception as e:
		return HttpResponse(e)

def notification(req):
	notifications=Notification.objects.filter(order_received__restro_profile__user=req.user).order_by("-id")
	if notifications==[]:
		return HttpResponse("{}")
	notification={}
	count=0
	for noti in notifications:
		temp={}
		temp["name"]=noti.name
		temp["order_received_id"]=noti.order_received.id
		notification["notification{}".format(count)]=temp
		count+=1
	print(notification)
	return JsonResponse({"notification":notification})
def orders(req): #optimize here and also orders template
	if req.method == "POST":
		search_query=req.POST['search']
		try:
			order_received=OrderReceived.objects.get(restro_profile__user=req.user,order__id=int(search_query))
			data={}
			data[order_received]=OrderUpdate.objects.filter(order=order_received.order).order_by("-id")
			return render(req,"restroadmin/orders.html",{"data":data,"valid_search":True})
		except Exception as e:
			return render(req,"restroadmin/orders.html",{"invalid_search":True})
	order_received=OrderReceived.objects.filter(restro_profile__user=req.user).order_by("-id")
	data={}
	for received_order in order_received:
		data[received_order]=OrderUpdate.objects.filter(order=received_order.order).order_by("-id")
	return render(req,"restroadmin/orders.html",{"data":data})