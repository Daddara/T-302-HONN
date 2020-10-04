//let search_class = "set this class in your html";

$(document).ready(function(){
    $("#search-input").on("keyup", function() {
        let value = $(this).val().toLowerCase();
        let listingElements = document.getElementsByClassName(search_class);
        for (let i=0; i<listingElements.length; i++){
            let listing_element = listingElements[i];
            let text_content = listing_element.textContent;
            if (!(text_content.toLowerCase().includes(value))){
                listing_element.style.display = "none";
            }
            else {
                listing_element.style.display = "inline-block";
            }
        }
    });
});