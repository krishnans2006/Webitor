function onSignIn(googleUser) {
  var id_token = googleUser.getAuthResponse().id_token;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/google-auth");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("idtoken=" + id_token);
}

function required() {
  let email = document.login_form.email.value;
  let password = document.login_form.password.value;

  if (email !== "" && password !== "") {
    return true;
  } else {
    alert("Please input a value!");
    return false;
  }
}
