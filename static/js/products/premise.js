$(document).ready(function() {
    $('.slider-viewing').slick({
        vertical: true,
        verticalSwiping: true,
        slidesToShow: 6,
    });
    $('body').on('click', '.slide', function () {
        let type = $(this).children();
        if (type.is('img')) {
            let src = $(this).find('img').attr('src');
            $('.slider-preview').html('<div style="background: url(\'' + src + '\'); background-size: cover; background-position: center">');
        } else {
            let src = $(this).find('video').attr('src');
            $('.slider-preview').html('<video controls="false" src="' + src + '"></video><div class="tap"><i class="fas fa-hand-pointer"></i></div>');
        }
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