$(document).ready(function() {
    $(".quest_time").ionRangeSlider({
        skin: "round",
        type: "single",
        grid: true,
        min: 1,
        max: 10,
        from: 5,
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