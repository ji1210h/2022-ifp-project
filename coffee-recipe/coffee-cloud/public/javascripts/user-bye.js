function doLogout(e) {
  e.preventDefault();

  let userData = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: "token " + token,
    },
  };
  fetch("http://13.125.61.174:8000/user/", userData)
    .then((response) => response.json())
    .then((res) => {
      localStorage.removeItem("jwt-token");
      location.href = "/index.html";
    });
}

function doDelete(e) {
  e.preventDefault();
  let userData = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: "token " + token,
    },
  };
  fetch("http://13.125.61.174:8000/user/", userData)
    .then((response) => response.json())
    .then((res) => {
      localStorage.removeItem("jwt-token");
      alert(res.message);
      location.href = "/index.html";
    });
}

logoutBtn.addEventListener("click", doLogout);
deleteBtn.addEventListener("click", doDelete);
