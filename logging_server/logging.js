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

function logErrorMsg(src, msg) {
    meta = {
        'src': src,
        'message': msg.substr(0, 512)
    };

    let data = new FormData();
    data.append('event_type', 'JS_ERROR');
    data.append('current_url', window.location.href);
    data.append('event_meta', JSON.stringify(meta));

    sendLog(data)
}

function logException(src, exception) {
    meta = {
        'src': src,
        'name': exception.name,
        'message': exception.message.substr(0, 512)
    };

    let data = new FormData();
    data.append('event_type', 'JS_ERROR');
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
            if (xmlHttp.status === 404) {
                // Just disable the service if it is offline
                // We're tracking here this means we want to be sneaky ;P
                logging_active = false;
            }
            else if (xmlHttp.status !== 200) {
                // Do you see a `Logging failed: 0` message in the console?
                // This means you added a lid to an element that reloads the site. This doesn't work sorry
                // Just remove it and forget that you where ever here. This script doesn't exist...
                console.log("Logging failed:", xmlHttp.status)
            }
        }
    };

    xmlHttp.open("POST", logging_url, true); // true for asynchronous
    xmlHttp.send(payload);
}

$("[lid]").click(function() {
    logButtonPress(this);
});