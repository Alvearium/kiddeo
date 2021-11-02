$(document).ready(function() {
    let products = $('.products-slider');

    while(products.children('div:not(.slide)').length)
        products.children('div:not(.slide):lt(6)').wrapAll('<div class="slide">');


    $('.products-slider').slick({
        infinite: false,
    });

    if ($(window).width() >= 1801) {
        $('.purchases-slider').slick({
            slidesToShow: 6,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 2000,
        });
    }else if ($(window).width() >= 1301) {
        $('.purchases-slider').slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 2000,
        });
    } else {
        $('.purchases-slider').slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 2000,
        });
    }
});