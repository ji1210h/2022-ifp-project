const loginBtn = document.querySelector(".login");

loginBtn.addEventListener("click", (e) => {
  e.preventDefault();

  let email = document.querySelector(".email").value;
  let password = document.querySelector(".password").value;

  let loginData = {
    method: "POST",
    body: JSON.stringify({ email, password }),
    headers: {
      "Content-Type": "application/json",
      // Authorization: localStorage.getItem("jwt-token"),
    },
  };

  fetch("http://13.125.61.174:8000/user/login/", loginData)
    .then((response) => response.json())
    .then((res) => {
      // console.log(res);
      if (res.token) {
        localStorage.setItem("jwt-token", res.token);
        location.href = "/user.html";
      } else {
        alert("이메일 혹은 비밀번호를 확인해주세요.");
      }
    });
});
