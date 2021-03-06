function onSignIn(googleUser) {
  console.log("Signing In...");
  var id_token = googleUser.getAuthResponse().id_token;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "https://algo-experts.herokuapp.com/google-auth");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("idtoken=" + id_token);
  console.log("ID token sent:");
  console.log(id_token);
}