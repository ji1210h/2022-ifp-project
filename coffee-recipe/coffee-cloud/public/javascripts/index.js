let token = localStorage.getItem("jwt-token");

let userLoginText = document.querySelector("#index-login");

let profileImg = document.querySelector("#profile-img");
let username = document.querySelector("#username");
let email = document.querySelector("#email");
let birth = document.querySelector("#birth");

let userData = {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    Authorization: "token " + token,
  },
};

// console.log(token);
fetch("http://13.125.61.174:8000/user/", userData)
  .then((response) => response.json())
  .then((res) => {
    console.log(res);
    if (!token) {
    } else {
      userLoginText.innerText = res.username + "님";
      userLoginText.href = "/user.html";
    }
  });
