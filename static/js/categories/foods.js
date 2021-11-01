$(document).ready(function() {
    $(".people_coast").ionRangeSlider({
        skin: "round",
        type: "single",
        grid: true,
        min: 1600,
        max: 3800,
        from: 2700,
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