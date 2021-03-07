function check() {
    if (
        document.getElementById("password").value ==
        document.getElementById("cpassword").value
    ) {
        document.getElementById("matches").style.color = "green";
        document.getElementById("matches").innerHTML = "Matches!";
        document.getElementById("submit").disabled = false;
    } else {
        document.getElementById("matches").style.color = "red";
        document.getElementById("matches").innerHTML = "Does Not Match!";
        document.getElementById("submit").disabled = true;
    }
}