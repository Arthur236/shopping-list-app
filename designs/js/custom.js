//Preloader background timeout
document.addEventListener("DOMContentLoaded", function () {
	$('.preloaderBackground').delay(1800).fadeOut('slow');

	$('.preloaderWrapper')
		.delay(1800)
		.fadeOut();
});

var counter = 0;

function addShoppingListItem(divId) {

	var newItem = document.createElement('div');
	newItem.className = "input-field col s10";
	newItem.innerHTML = "<label for='items[]'>Item " + (counter + 1) + "</label><input id='items[" + counter + "]' class='leftInputs' name='items[" + counter + "]' type='text' required='required'/><span class='rightIcons'><a href='#'><i class='material-icons'>delete</i></a><a href='#'><i class='material-icons'>edit</i></a></span class='clear'><span></span>";
	document.getElementById(divId).appendChild(newItem);
	counter++;

	/*To access each item
	$myInputs = $_POST["myInputs"];
	foreach ($items as $item) {
		 echo $eachInput . "<br>";
	}*/
}