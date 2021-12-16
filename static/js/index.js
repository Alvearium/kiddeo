$(document).ready(function() {
    $('.main-slider').slick({
        infinite: true,
        autoplay: true,
        autoplaySpeed: 4000,
    });
    $('.service-box').on('click', function () {
        let link = $(this).attr('data-href');

        window.location.href = link;
    });
    $('.choose-container .image-block').on('click', function () {
        let link = $(this).attr('data-href');

        window.location.href = link;
    });
});