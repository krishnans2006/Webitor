function makeRequest (method, url, body_name, body_params) {
  return new Promise(function (resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.onload = function () {
      if (this.status >= 200 && this.status < 300) {
        resolve(xhr.response);
      } else {
        reject({
          status: this.status,
          statusText: xhr.statusText
        });
      }
    };
    xhr.onerror = function () {
      reject({
        status: this.status,
        statusText: xhr.statusText
      });
    };
    xhr.send(body_name + body_params);
  });
}

function onSignIn(googleUser) {
  var id_token = googleUser.getAuthResponse().id_token;
  makeRequest("POST", "/google-auth", "idtoken=", id_token)
      .then(function (datums) {
          window.location.reload(true);
      });
}