var bcart = document.querySelector('#bcart');
var ptotal = document.querySelector('#total');

//ajouter pizza

function addItem(id){
    //nom burger

    ItemId = 'item' + id;
    var name = document.getElementById(ItemId).innerHTML;
    console.log(name);
    //prix burger
    var radio = 'item' + id;
    var pri = document.getElementsByName(radio);
    var size, price;
    if(pri[0].checked){
        price = pri[0].value;
        size = 'M';
    }
    else{
        price = pri[1].value;
        size = 'L';
    }

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    //sauvegard produit localstorage
    orders[cartSize] = [name, size, price, id];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    //mise a jour panier
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    
    butt = '<div class="del" onclick="removeItem(' + cartSize + ')">x</div>';
    
    btotal.innerHTML =  'Total : ' + total + '€';
    bcart.innerHTML += '<li>' + name + ' ' + size + ': ' + price +' €' + butt + ' </li>';

}

function shoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    bcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        butt = '<div class="del" onclick="removeItem(' + i + ')">x</div>';
        bcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ': ' + orders[i][2] +' €' + butt + '</li>';
    }
    btotal.innerHTML =  'Total : ' + Number(total) + '€';

}

shoppingCart();

function removeItem(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);

    //mise a jour panier
    var cart = document.querySelector("#cart");
    //cart.innerHTML = orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    
    shoppingCart();

}