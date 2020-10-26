$( "#preview" ).on('click', function () {
    console.log("preview clicked");
    let title = $('#id_Title').val();
    let description = $('#id_Description').val();
    let image = $('#id_Image').val();
    let equipment_option_val = $('#id_Equipment').val();
    let equipment = "None";
    if (!(equipment_option_val === "")){
        equipment = $("#id_Equipment option[value='"+equipment_option_val+"']").text();
    }
    let muscle_group_option_val = $('#id_muscle_group').val();
    let muscle_group = "None";
    if (!(muscle_group_option_val === "")){
        muscle_group = $("#id_muscle_group option[value='"+muscle_group_option_val+"']").text();
    }

    $('#exercise-title').text(title);
    $('#exercise-description').text(description);
    $('#img-exercise-image').attr('src', image);
    $('#exercise-equipment').text(equipment);
    $('#exercise-trains').text(muscle_group);
});