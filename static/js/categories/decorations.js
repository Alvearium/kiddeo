$(document).ready(function() {
    $(".cost").ionRangeSlider({
        skin: "round",
        type: "single",
        grid: true,
        min: 1000,
        max: 50000,
        from: 25000,
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