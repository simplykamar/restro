										
				// Get cart if available otherwise initialize empty cart

if (localStorage.getItem('cart')==null){
	var cart={};
	localStorage.setItem('cart',JSON.stringify(cart));
}else{
	cart=JSON.parse(localStorage.getItem('cart'));
	updateCart(cart);
	let restro_id=$('#get-restro-id').val();
	if (!restroCheck(restro_id)) {
		let restr_id = cart[Object.keys(cart)[0]]["restro_id"];
		let restr_name = cart[Object.keys(cart)[0]]["restro_name"];
		$('#cart-from-diff-restro').html(`<p class="text-danger">Your cart from
			<br><small><a href="/foodie/restro-view/${restr_id}" class="text-capitalize">${restr_name}</a></small><span class="clear-cart float-right text-danger cursor-pointer"><i class="far fa-trash-alt"></i>Clear cart</span></p>`)
	}
}
				//If someone click cart class then fetch click Item ID, Name,Price...and append in to cart 
				//If fetch Item ID available in cart then Increament Item qty by one
$(document).on('click','.clear-cart',function(){
	localStorage.clear();
	location.reload();
});
function restroCheck(restro_id){
	console.log("in rsechk");
	console.log(cart);
	if (Object.keys(cart).length<1) {
		return true;
	}
	for (item in cart){
		if (cart[item]["restro_id"]==restro_id){
			return true;
		}
	}
	return false;
}
$(document).on('click','.cart',function(){
		let restro_id=$('#get-restro-id').val();
		if (restroCheck(restro_id)){
			let id=this.id.toString();
			if (id in cart){
					cart[id]["qty"]+=1
				}
			else{
				let name=$('#'+id+'name').html().toLowerCase();
				let price=parseInt($('#'+id+'price').html().slice(2,));
				let restro_name=$('#get-restro-name').html().toLowerCase();
				let restro_location=$('#get-restro-location').html().toLowerCase();
				let restro_img=$('.restro-img').attr('src');
				let qty=1;
				cart[id]={
					"name":name,"price":price,"qty":qty,"restro_name":restro_name,
					"restro_id":restro_id,"restro_location":restro_location,"restro_img":restro_img
					};
			}
		updateCart(cart);
		}else{
			alert("Your cart contains items from other restaurant. Clear your cart for adding fresh items from this restaurant?")
		}	
});
					//If quantity of item is 0 then show ADD btn other show plus, minus btn

function updateCart(cart){
		for(item in cart){
			$('#added'+item).html(`
			<button class="btn text-success font-weight-bolder border minus" id=${item}>-</button>${cart[item]["qty"]}
			<button class="btn text-success font-weight-bolder border plus" id=${item}>+</button>
			`);
			if(cart[item]["qty"]==0){
				delete cart[item];
				$('#added'+item).html(`
				<button class="btn border px-4 cart" id=${item}>
				<span class="text-success font-weight-bolder">ADD</span></button>
				`);
			}
		}	sidebarCart(cart);
			localStorage.setItem("cart",JSON.stringify(cart));
	}
					//If someone click plus btn then increase item quantity by one

$(document).on('click','.plus',function (){
	let id=this.id;
	cart[id]["qty"]+=1;
	console.log(cart);
	updateCart(cart);
});
					//If someone click minus btn then decrease item quantity by one

$(document).on('click','.minus',function (){
	let id=this.id;
	cart[id]["qty"]-=1;
	cart[id]["qty"]=Math.max(0,cart[id]["qty"])
		console.log(cart);
		updateCart(cart);
});
						//cart Sidebar used in restro-view and checkout page
						//display cart items in sidebar and total amount of cart item

function sidebarCart(cart){
	//if cart length == 0 then show empty cart otherwise show cart
	$('#navbar-cart').html(countItem(cart));
	if (Object.keys(cart).length==0) {
		//if cart not exist then hide .cart-availbale class, this class used in both restro_view and checkout page 		
		$('.cart-available').hide();
		$('#checkout-cart-available').hide();
		$('#checkout-cart-empty').show();
		$('#checkout-cart-empty').html(`
				<img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto/2xempty_cart_yfxml0" class="img-fluid" style="width:300px;height:300px;">
				<h4 class="mt-3">Your cart is empty</h4>
				<p class="my-3">You can go to home page to view more restaurants</p>
				<a href="" class="btn btn-danger px-3 py-2">SEE RESTAURANTS NEAR YOU</a>
			`)
		console.log("cart work 1");
		console.log(Object.keys(cart).length+" "+cart);
		$('#sidebarcart').empty();
		$('#sidebarcart').html(`
			<h4 class='text-secondary font-weight-bolder'>Cart Empty</h4>
			<div class='text-center mt-3'><img src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_480/Cart_empty_-_menu_2x_ejjkf2" class="img-fluid">
			</div>
			<p class='text-secondary my-3'>Good food is always cooking! Go ahead, order some yummy items from the menu.</p>
			`);
		console.log("cart work 2");
	}else{

		$('#checkout-cart-empty').hide();
		//if cart available then show .cart-availbale class, this class used in both restro_view and checkout page 
		//if cart available then only show and set item restro img and location in checkout sidebar cart 
		$('.cart-available').show();
		$('#set-restro-name').html(cart[Object.keys(cart)[0]]["restro_name"]);
		$('#set-restro-location').html(cart[Object.keys(cart)[0]]["restro_location"]);
		$('#set-checkout-cart-link').attr( 'href', '/foodie/restro-view/' + cart[Object.keys(cart)[0]]["restro_id"]);	
		$('.checkout-cart-img').attr('src',cart[Object.keys(cart)[0]]["restro_img"]);
		
		console.log("cart not work");
		console.log(Object.keys(cart).length+" "+cart);
		let carttotal=0;
		$('#sidebarcart').empty();
		for(let item in cart){
			$('#sidebarcart').append(`
			<div  class="row no-gutters mb-3 text-capitalize">
			<div class="col-lg-4 col-md-4 col-sm-4 col-4">
				<span>${cart[item]["name"]}</span>
			</div>
			<div class="col-lg-4 col-md-4 col-sm-4 col-4">
				<span class="d-flex">
					<button class="btn px-2 text-success font-weight-bolder border minus" id=${item}>-</button>
					<span>${cart[item]["qty"]}</span>
					<button class="btn px-2 text-success font-weight-bolder border plus" id=${item}>+</button>
				</span>
			</div>
			<div class="col-lg-4 col-md-4 col-sm-4 col-4">
					<span>₹ ${cart[item]["price"]*cart[item]["qty"]}</span>
				</div></div>
				`);
				carttotal+=cart[item]["price"]*cart[item]["qty"];
	}
	$('#carttotal').html(carttotal);
	$('#cartitem').html(countItem(cart)+" Items");
}
 }
 function countItem(cart) {
 	let countItem=0
 	for(let item in cart){
 		countItem+=cart[item]["qty"];
 	}
 	return countItem;
 }
