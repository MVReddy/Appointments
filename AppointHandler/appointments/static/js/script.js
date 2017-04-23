function getAppointments(search_str){

    var search_str = $("#search_box").val();
    $.get('/appointments/search/', {'search_str': search_str}, function(data){

    alert(data);
    $("#search-results").html(data[0].description);
    });
}

//$.when(getAppointments()).then($("#search-results").html("Hello World");)

function showForm() {
    var x = document.getElementById('new-form'),
        y = document.getElementById('show-hide');
    if (x.style.display === 'none') {
        x.style.display = 'block';
        y.value='Clear';
    } else {
        x.style.display = 'none';
        y.value='New';
    }
}
