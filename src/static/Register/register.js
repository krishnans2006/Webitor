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
