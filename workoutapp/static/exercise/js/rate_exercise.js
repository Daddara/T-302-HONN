rate_exercise_url = "/workout/rate_exercise"
login_url = "/accounts/login/"

function display_exercise_rating(exercise_id, new_status) {
    console.log("Exercise update " + exercise_id + " " + new_status)
}

function post_exercise_rating(exercise_id, rating) {
    let data = new FormData()
    data.append('exercise_id', exercise_id)
    data.append('rating', rating)
    
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState === 4) {
            if (xmlHttp.status !== 200) {
                if (xmlHttp.status === 401) {
                    redirect_to_login();
                } else {
                    logErrorMsg(document.currentScript, "The saving of a rating has failed")
                    alert("Your rating could not be saved")
                }
            }
        }
    };
    
    xmlHttp.open("POST", rate_exercise_url, true); // true for asynchronous
    xmlHttp.send(data);
}

function handle_exercise_rating(exercise_id, new_status) {
    display_exercise_rating(exercise_id, new_status)
    post_exercise_rating(exercise_id, new_status)
}

function redirect_to_login() {
    window.location.href = login_url;
    alert("Please login to rate a workout");
}

$( ".likes" ).each(function( index ) {
    this.onclick = function() {
        let like_icon = $(this).children('.like-idf');
        let likes_value_element = $(this).children('.social-span');
        let likes = Number(likes_value_element.text());
        let dislike_div = $(this).parent().children('.dislikes');
        let dislike_icon = dislike_div.children('.dislike-idf');
        let dislikes_value_element = dislike_div.children('.social-span');
        let dislikes = Number(dislikes_value_element.text());

        // If not already liked
        if(!(like_icon.hasClass('liked'))){
            like_icon.addClass('liked');
            likes_value_element.text((likes+1).toString());
            if(dislike_icon.hasClass('disliked')){
                dislikes_value_element.text((Number(dislikes-1)).toString());
            }
            exercise_id = Number(this.getAttribute("exercise-id"));
            handle_exercise_rating(exercise_id, "+1")
            dislike_icon.removeClass('disliked');
        }
    };
});
$( ".dislikes" ).each(function( index ) {
    this.onclick = function() {
        let dislike_icon = $(this).children('.dislike-idf');
        let dislikes_value_element = $(this).children('.social-span');
        let dislikes = Number(dislikes_value_element.text());

        let like_div = $(this).parent().children('.likes');
        let like_icon = like_div.children('.like-idf');
        let likes_value_element = like_div.children('.social-span');
        let likes = Number(likes_value_element.text());

        // If not already disliked
        if(!(dislike_icon.hasClass('disliked'))){
            dislike_icon.addClass('disliked');
            dislikes_value_element.text((dislikes+1).toString());
            if (like_icon.hasClass('liked')){
                likes_value_element.text((Number(likes-1)).toString());
            }
            exercise_id = Number(this.getAttribute("exercise-id"));
            handle_exercise_rating(exercise_id, "-1")
            like_icon.removeClass('liked');
        }
    };
});