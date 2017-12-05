function getJobs(){

    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    var email = document.getElementById("email");
    var span  = document.getElementById("email-span");
    var table = document.getElementById("job-list");
    var tableContent = document.getElementById("job-list-content");
    var xhttp = new XMLHttpRequest();

    if (!(email.value != "" &&  re.test(email.value))){

        table.style.visibility = 'hidden';
        return;

    }

    span.innerText = email.value;
    table.style.visibility = 'visible';

    xhttp.onreadystatechange = function(){

        if (this.readyState == 4 && this.status == 200) {

            document.getElementById("demo").innerHTML = this.responseText;

        }

    }

    xhttp.open("GET", "/", true);
    xhttp.send();

}

function getJobData(){

    

}