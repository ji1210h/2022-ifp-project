let token = localStorage.getItem("jwt-token");

let profileImg = document.querySelector("#profile-img");
let username = document.querySelector("#username");
let email = document.querySelector("#email");
let birth = document.querySelector("#birth");

let doneBtn = document.querySelector("#done");
let logoutBtn = document.querySelector("#logout");
let deleteBtn = document.querySelector("#delete");

function changeUserData(e) {
  e.preventDefault();

  let editImg = document.querySelector("#edit-img").value;
  let editName = document.querySelector("#edit-name").value;
  let editPw = document.querySelector("#edit-pw").value;

  let userData = {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Authorization: "token " + token,
    },
    body: JSON.stringify({
      profile_image: editImg,
      // username: editName,
      // password: editPw,
    }),
  };
  fetch("http://13.125.61.174:8000/user/", userData)
    .then((response) => response.json())
    .then((res) => {
      console.log(res);
      console.log(editImg.files[0].name);

      // // name
      // if (res.username == "user with this username already exists.") {
      //   alert("존재하는 닉네임입니다.");
      //   return false;
      // } else if (res.username == "This field may not be blank.") {
      //   alert("닉네임을 입력해주세요.");
      //   return false;
      // }
      // //password
      // else if (res.password == "Ensure this field has at least 8 characters.") {
      //   alert("패스워드는 8자리 이상 적어주세요.");
      //   return false;
      // } else if (res.password == "This field may not be blank.") {
      //   alert("패스워드를 입력해주세요.");
      //   return res.password;
      // }
      // // 성공
      // else {
      //   // localStorage.removeItem(token);
      //   alert("성공했습니다! 다시 로그인해주세요.");
      //   location.href = "/login.html";
      // }
    });
}

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
    profileImg.innerHTML = `<img src="http://13.125.61.174:8000${res.profile_image}"/>`;
    username.innerText = res.username;
    email.innerText = res.email;
    birth.innerText = res.date_of_birth;
  });

doneBtn.addEventListener("click", changeUserData);
