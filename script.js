let lat
let lon

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

    lat = position.coords.latitude;
    lon = position.coords.longitude;
    console.log(lat)
    console.log(lon)

    document.getElementById("result").innerHTML =
    "Latitude: " + lat + "<br>Longitude: " + lon;

}

function showError(error) {

    document.getElementById("result").innerHTML =
    "User denied location access.";

}