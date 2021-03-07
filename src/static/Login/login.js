function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/google-auth");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.send("idtoken=" + id_token);
}