//Preloader background timeout
document.addEventListener("DOMContentLoaded", function () {
	$('.preloaderBackground').delay(1800).fadeOut('slow');

	$('.preloaderWrapper')
		.delay(1800)
		.fadeOut();
});
