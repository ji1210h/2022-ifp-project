let token = localStorage.getItem("jwt-token");

let profileImg = document.querySelector("#profile-img");
let username = document.querySelector("#username");
let email = document.querySelector("#email");
let birth = document.querySelector("#birth");

let doneBtn = document.querySelector("#done");
let logoutBtn = document.querySelector("#logout");
let deleteBtn = document.querySelector("#delete");

const form = document.querySelector("#form-data");

form.addEventListener("submit", changeUserData);

function changeUserData(e) {
  e.preventDefault();
  const formData = new FormData(form);
  console.log([...formData]);
  // const nameEdit = document.querySelector("#edit-name").value;
  // const pwEdit = document.querySelector("#edit-pw").value;

  let userData = {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Authorization: "token " + token,
    },
    body: JSON.stringify({
      // profile_image: "/media/profile/2022/10/" + formData.get("edit-img").name,
      username: formData.get("edit-name"),
      password: formData.get("edit-pw"),
    }),
    // body: JSON.stringify({ username: nameEdit, password: pwEdit }),
  };
  fetch("http://13.125.61.174:8000/user/", userData)
    .then((response) => response.json())
    .then((res) => {
      // for (let value of formData.values()) {
      //   console.log(value);
      // }

      console.log(res);

      if (res.email) {
        localStorage.clear();
        alert("변경되었습니다. 다시 로그인해주세요.");
        location.href = "index.html";
      } else {
        alert("모두 입력해주세요.");
      }
    });
}

// ------------------------------------------------------------
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
