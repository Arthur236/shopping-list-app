//Preloader background timeout
document.addEventListener("DOMContentLoaded", function () {
	$('.preloaderBackground').delay(1800).fadeOut('slow');

	$('.preloaderWrapper')
		.delay(1800)
		.fadeOut();
});

let counter = 0;
let items = new Array;

function addShoppingListItem(divId) {

	let newItem = document.createElement('div');

	newItem.className = "input-field col s8";
	newItem.innerHTML = "<label for='items[" + counter + "]'>Item</label><input id='items[" + counter + "]' name='items[" + counter + "]' type='text' required='required'/>";

	let icons = document.createElement('div');
	let fxn = "enableInput('items[" + counter + "]')";
	icons.className = "input-field col s4";
	icons.innerHTML = '<span><a href="#" class="btn-floating"><i class="material-icons">delete</i></a><a href="#" class="btn-floating" onclick="'+ fxn +'"><i class="material-icons">edit</i></a></span>';

	document.getElementById(divId).appendChild(newItem);
	document.getElementById(divId).appendChild(icons);
	counter++;

	/*To access each item
	$myInputs = $_POST["myInputs"];
	foreach ($items as $item) {
		 echo $eachInput . "<br>";
	}*/
}

function deleteShoppingListItem(divId) {
	var elem = document.getElementById('#'+divId);

    elem.remove();
    return false;
}

function enableInput(inputId) {
	if ($("#"+inputId).attr("disabled")) {
		$("#"+inputId).removeAttr("disabled");
	} else {
		$("#"+inputId).attr("disabled","disabled");
	}
}