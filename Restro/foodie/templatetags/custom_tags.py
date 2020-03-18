from django import template
from foodie.models import RestroItem
register = template.Library()

@register.filter(name="getTotal")
def total1(order_items):
	total=0
	for order_item in order_items:
		total+=order_item.item.price*order_item.qty
	return total

@register.filter(name="getItemTotal")
def total2(price,qty):
	return price*qty

@register.filter(name="getItemCount")
def count(order_items):
	count=0
	for order_item in order_items:
		count+=order_item.qty
	return count

@register.filter(name="update_exists")
def check(order_updates,check_string):
	for update in order_updates:
		if update.status == check_string:
			return True
	return False