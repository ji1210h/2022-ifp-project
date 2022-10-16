// const signBtn = document.querySelector(".signup");
// const form = document.querySelector()

// signBtn.addEventListener("click", (e) => {
//   const email = document.querySelector(".email").value;
//   const username = document.querySelector(".name").value;
//   const password = document.querySelector(".password1").value;

//   const signData = {
//     method: "POST",
//     body: JSON.stringfy({
//       email,
//       //   profile_image,
//       username,
//       password,
//       //   date_of_birth,
//     }),
//     headers: {
//       "Content-Type": "application/json",
//     },
//   };

//   fetch("http://15.165.237.85:8080/user/create/", signData)
//     .then((data) => data.json())
//     .then((res) => console.log(res));
// });

// window.addEventListener("load", (e) => {
const signupBtn = document.querySelector(".signup");
// const form = document.querySelector('.form');

signupBtn.addEventListener("click", (e) => {
  e.preventDefault(); // 기본 폼 동작 막기

  let email = document.querySelector(".email").value;
  let username = document.querySelector(".name").value;
  let password = document.querySelector(".password").value;
  let date_of_birth = document.querySelector(".birth").value;

  let signupData = {
    method: "POST",
    body: JSON.stringify({ email, username, password, date_of_birth }),
    headers: {
      "Content-Type": "application/json",
    },
  };

  fetch("http://13.125.61.174:8000/user/create/", signupData)
    .then((response) => response.json())
    .then((res) => {
      console.log(res);
    });
});
