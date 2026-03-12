function getLocation() {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } 
    else {
        document.getElementById("result").innerHTML =
        "Geolocation is not supported.";
    }

}

function showPosition(position) {

    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    document.getElementById("result").innerHTML =
    "Latitude: " + lat + "<br>Longitude: " + lon;

}

function showError(error) {

    document.getElementById("result").innerHTML =
    "User denied location access.";

}