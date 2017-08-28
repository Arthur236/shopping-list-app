//Preloader background timeout
document.addEventListener("DOMContentLoaded", function () {
	$('.preloaderBackground').delay(1800).fadeOut('slow');

	$('.preloaderWrapper')
		.delay(1800)
		.fadeOut();
});

var counter = 0;

function addShoppingListItem(divId) {

	let newItem = document.createElement('div');

	newItem.className = "input-field col s8";
	newItem.innerHTML = "<label for='items[]'>Item " + (counter + 1) + "</label><input id='items[" + counter + "]' name='items[" + counter + "]' type='text' required='required'/>";

	let icons = document.createElement('div');
	icons.className = "input-field col s4";
	icons.innerHTML = "<span><a href='#' class='btn-floating'><i class='material-icons'>delete</i></a><a href='#' class='btn-floating'><i class='material-icons'>edit</i></a></span>";

	document.getElementById(divId).appendChild(newItem);
	document.getElementById(divId).appendChild(icons);
	counter++;

	/*To access each item
	$myInputs = $_POST["myInputs"];
	foreach ($items as $item) {
		 echo $eachInput . "<br>";
	}*/
}