$( "#about-me-nav" ).on('click', function () {
    $(this).css('color', '#963211');
    $('#friends-nav').css('color', 'black');
    $('#exercises-nav').css('color', 'black');
    $('#workouts-nav').css('color', 'black');
    $('#follower-nav').css('color', 'black');

    $('#about-me').show();
    $('#exercises').hide();
    $('#workouts').hide();
    $('#friends-container').hide();
    $('#follower-list-container').hide();
});


$( "#friends-nav" ).on('click', function () {
    $(this).css('color', '#963211');
    $('#about-me-nav').css('color', 'black');
    $('#exercises-nav').css('color', 'black');
    $('#workouts-nav').css('color', 'black');
    $('#follower-nav').css('color', 'black');

    $('#about-me').hide();
    $('#exercises').hide();
    $('#workouts').hide();
    $('#friends-container').show();
    $('#follower-list-container').hide();
});

$( "#workouts-nav" ).on('click', function () {
    $(this).css('color', '#963211');
    $('#about-me-nav').css('color', 'black');
    $('#friends-nav').css('color', 'black');
    $('#exercises-nav').css('color', 'black');
    $('#follower-nav').css('color', 'black');

    $('#about-me').hide();
    $('#exercises').hide();
    $('#friends-container').hide();
    $('#workouts').show();
    $('#follower-list-container').hide();
});

$( "#exercises-nav" ).on('click', function () {
    $(this).css('color', '#963211');
    $('#follower-nav').css('color', 'black');
    $('#about-me-nav').css('color', 'black');
    $('#friends-nav').css('color', 'black');
    $('#workouts-nav').css('color', 'black');

    $('#about-me').hide();
    $('#exercises').show();
    $('#friends-container').hide();
    $('#workouts').hide();
    $('#follower-list-container').hide();
});

$('#follower-nav').on('click', function (){
    $(this).css('color', '#963211');
    $('#about-me-nav').css('color', 'black');
    $('#friends-nav').css('color', 'black');
    $('#exercises-nav').css('color', 'black');
    $('#workouts-nav').css('color', 'black');

    $('#about-me').hide();
    $('#exercises').hide();
    $('#friends-container').hide();
    $('#workouts').hide();
    $('#follower-list-container').show();
})


$( "#sent" ).on('click', function () {
    if ($('#sent-list').css('display')==="none"){
        $(this).css('color', '#963211');
        $('#incoming').css('color', 'black');

        $('#received-list').hide();
        $('#sent-list').show();
    }else{
        $('#sent-list').hide();
        $(this).css('color', 'black');
    }
});

$( "#incoming" ).on('click', function () {
    if ($('#received-list').css('display')==="none"){
        $(this).css('color', '#963211');
        $('#sent').css('color', 'black');

        $('#received-list').show();
        $('#sent-list').hide();
    }else{
        $('#received-list').hide();
        $(this).css('color', 'black');
    }
});
