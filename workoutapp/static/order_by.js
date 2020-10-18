//let target_order_element = "workout-background-shadow"; // Should be the class name of the element wanting to order
//let render_inside_element = "center-page-content"; // Make sure only one of this instance exists. Should be a class name

$("#rating").on('click', function () {
    order_by_rating(target_order_element);
});

// Rating is likes/(likes+dislikes)
function order_by_rating(target){
    let dict = {};
    let elements = document.getElementsByClassName(target)
    for (let i=0; i<elements.length; i++){
        let current = elements[i];
        // Getting the rating stats on each element
        let likes_element = current.querySelector('.likes'); // Select likes parent div
        let likes = parseInt(likes_element.querySelector('.social-span').textContent);
        let dislikes_element = current.querySelector('.dislikes'); // Select dislikes parent div
        let dislikes = parseInt(dislikes_element.querySelector('.social-span').textContent);

        let rating = 0;

        if(dislikes===0 && likes===0){
                rating = 0;
            }
        else{
            if (dislikes!==0 && likes===0){
                rating = -dislikes
            }
            else {
                rating = (likes + 1) / (likes + dislikes + 1);
            }
        }

        console.log(rating);
        // If the rating is not already in dict -> Create key and value
        let test_exists = dict[rating]
        if (test_exists===undefined || test_exists===null){
            dict[rating] = [current]
        }
        // If the rating exists -> Append current element to the dict value
        else {
            dict[rating].push(current);
        }
    }
    // Sorting keys according to rating high -> low
    let dict_ratings = Object.keys(dict);
    dict_ratings.sort(function (a, b) {  return b - a;  });
    remove_and_insert(dict, dict_ratings);
}

$("#popularity").on('click', function () {
    order_by_popularity(target_order_element);
});


// Popularity is just likes + dislikes
function order_by_popularity(target){
    let dict = {};
    let elements = document.getElementsByClassName(target)
    for (let i=0; i<elements.length; i++){
        let current = elements[i];
        // Getting the rating stats on each element
        let likes_element = current.querySelector('.likes'); // Select likes parent div
        let likes = parseInt(likes_element.querySelector('.social-span').textContent);
        let dislikes_element = current.querySelector('.dislikes'); // Select dislikes parent div
        let dislikes = parseInt(dislikes_element.querySelector('.social-span').textContent);

        let popularity = likes+dislikes;
        console.log(popularity);
        // If the rating is not already in dict -> Create key and value
        let test_exists = dict[popularity]
        if (test_exists===undefined || test_exists===null){
            dict[popularity] = [current]
        }
        // If the rating exists -> Append current element to the dict value
        else {
            dict[popularity].push(current);
        }
    }
    // Sorting keys according to rating high -> low
    let dict_popularity = Object.keys(dict);
    dict_popularity.sort(function (a, b) {  return b - a;  });
    remove_and_insert(dict, dict_popularity);
}

$("#publish-date").on('click', function () {
    order_by_date(target_order_element);
});


function order_by_date(target){
    let dict = {};
    let elements = document.getElementsByClassName(target)
    for (let i=0; i<elements.length; i++){
        let current = elements[i];

        // Retrieving date as string from hidden div element
        let timestamp = parseFloat(current.querySelector('.created-at').textContent)*1000; // in ms
        console.log(timestamp);
        let test_exists = dict[timestamp]
        if (test_exists===undefined || test_exists===null){
            dict[timestamp] = [current]
        }
        // If the rating exists -> Append current element to the dict value
        else {
            dict[timestamp].push(current);
        }
    }
    let dict_timestamps = Object.keys(dict);
    // sorting from most recent -> oldest
    dict_timestamps.sort(function (a, b) {  return b - a;  });
    remove_and_insert(dict, dict_timestamps);
}

function remove_and_insert(dict, dict_ratings){
    // Getting the parent of the target ordering elements
    let parent_element = document.getElementsByClassName(render_inside_element)[0];
    // Emptying it's content
    parent_element.innerHTML = "";
    // Reinserting according to the sorted dict_ratings array
    for (let i=0; i<dict_ratings.length; i++){
        let elements = dict[dict_ratings[i]];
        for(let y=0; y<elements.length; y++){
            parent_element.appendChild(elements[y])
        }
    }
}