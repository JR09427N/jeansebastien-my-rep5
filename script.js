function loadDoc(url, func) {
    let xhttp = new XMLHttpRequest();
    xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        if(xhttp.status != 200) {
            console.log("Error");
        } else {
            func(xhttp.response);
        }
    }
    xhttp.open("GET", url);
    xhttp.send();
}

function apartment_search() {
    let txtSearch = document.getElementById("txtSearch");
    let selRooms = document.getElementById("selRooms")
    let selSort = document.getElementById("selSort");

    let url = "https://jr09427n.pythonanywhere.com/apartment?search=" + txtSearch.value + "&rooms=" + selRooms.value + "&sort=" + selSort.value;

    loadDoc(url, apartment_search_response);
}

function apartment_search_response(response) {
    let data = JSON.parse(response);
    let result = data["result"];

    let temp = "<table><tr>";
    temp += "<th>Title</th>";
    temp += "<th>Description</th>";
    temp += "<th>Bedrooms</th>";
    temp += "<th>Monthly Rent</th>";
    temp += "</tr>";

    for (let i = 0; i < result.length; i++) {
        let row = result[i];
        temp += "<tr>";
        temp += "<td>" + row.title + "</td>";
        temp += "<td>" + row.description + "</td>";
        temp += "<td>" + row.bedrooms + "</td>";
        temp += "<td>$" + row.monthly_rent + "</td>";
        temp += "</tr>";
    }

    temp += "</table>";

    let divResults = document.getElementById("divResults");

    divResults.innerHTML = temp;
}

console.log("Script Loaded");