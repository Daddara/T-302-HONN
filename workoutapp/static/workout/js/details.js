$( ".drop-down" ).on('click', function () {
    console.log("Clicked drop down")
    // Reveal hidden info
    $(this).siblings('.hidden-info').show();
    // Change the displayed icon to drop up
    $(this).hide();
    $(this).siblings('.drop-up').show();
});

$( ".drop-up" ).on('click', function () {
    console.log("Clicked drop up")
     // Reveal hidden info
    $(this).siblings('.hidden-info').hide();
    // Change the displayed icon to drop up
    $(this).hide();
    $(this).siblings('.drop-down').show();
});