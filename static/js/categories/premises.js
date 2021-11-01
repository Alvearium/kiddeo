$(document).ready(function() {
    $(".rental_price").ionRangeSlider({
        skin: "round",
        type: "single",
        grid: true,
        min: 1600,
        max: 3200,
        from: 2400,
        step: 1,
        drag_interval: true,
        from_shadow: true,
        grid_num: 1,
        hide_min_max: true,
        onStart: function(data) {
            console.log(data.from);
        },
        onFinish: function(data) {
            console.log(data.from);
        },
    });
    $(".square").ionRangeSlider({
        skin: "round",
        type: "single",
        grid: true,
        min: 30,
        max: 225,
        from: 123,
        step: 1,
        drag_interval: true,
        from_shadow: true,
        grid_num: 1,
        hide_min_max: true,
        onStart: function(data) {
            console.log(data.from);
        },
        onFinish: function(data) {
            console.log(data.from);
        },
    });
});