const logging_url = "http://127.0.0.1:8001/frontend/event";
logging_active = true;

function logButtonPress(buttonObj) {
    meta = {
        'lid': buttonObj.getAttribute("lid"),
        'html': buttonObj.outerHTML.split('>', 1)[0]
    };

    let data = new FormData();
    data.append('event_type', 'BUTTON_PRESS');
    data.append('current_url', window.location.href);
    data.append('event_meta', JSON.stringify(meta));

    sendLog(data)
}

function sendLog(payload) {
    if (!logging_active) {
        return;
    }

    let xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState === 4) {
            if (xmlHttp.status !== 200) {
                console.log(xmlHttp)
            }
        }
    };

    xmlHttp.open("POST", logging_url, true); // true for asynchronous
    xmlHttp.send(payload);
    console.log("Bye bye");
}

$("[lid]").click(function() {
    logButtonPress(this);
});