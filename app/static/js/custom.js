//Preloader background timeout
document.addEventListener("DOMContentLoaded", function () {
	$('.preloaderBackground').delay(1000).fadeOut('slow');

	$('.preloaderWrapper')
		.delay(1000)
		.fadeOut();
});
