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

function add_choices(data) {
    let unit_keys = Object.keys(data['units']);
    let exercise_keys = Object.keys(data['exercises']);
    exercise_keys.sort(function (a, b) {  return a - b;  });
    for (let i=0; i<exercise_keys.length; i++){
        let id = unit_keys[i]
        let value = data['exercises'][id];
        id = id.toString();
        $('#exercise-options').append("<li class='list-group-item'>" +
            "<button class='btn btn-light ex-option' id="+id+" onclick=ex_clicked("+id+")>"+value+"</button>"+"</li>")
    }
    for (let i=0; i<unit_keys.length; i++){
        let id = unit_keys[i]
        let value = data['units'][id];
        id = id.toString();
        console.log(data['units'][i]);
        $('#unit-options').append("<option "+ "value="+id + ">"+value+"</option>")
    }
}