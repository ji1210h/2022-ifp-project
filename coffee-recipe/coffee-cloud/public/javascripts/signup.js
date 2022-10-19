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
      // console.log(res);

      // email
      if (!email) {
        alert("이메일을 입력해주세요.");
        return false;
      } else if (res.email == "user with this email already exists.") {
        alert("존재하는 이메일입니다.");
        return false;
      } else if (res.email == "Enter a valid email address.") {
        alert("이메일 형식을 지켜주세요.");
        return false;
      }

      // password
      else if (!password) {
        alert("패스워드를 입력해주세요.");
        return false;
      } else if (
        res.password == "Ensure this field has at least 8 characters."
      ) {
        alert("패스워드는 8자리 이상 적어주세요.");
        return false;
      }

      // name
      else if (!username) {
        alert("이름을 입력해주세요.");
        return false;
      } else if (res.username == "user with this username already exists.") {
        alert("존재하는 닉네임입니다.");
        return false;
      }

      // birth
      else if (
        res.date_of_birth ==
        "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
      ) {
        alert("생일을 입력해주세요.");
        return false;
      }

      // 성공시
      else {
        location.href = "/login.html";
      }
    });
});
