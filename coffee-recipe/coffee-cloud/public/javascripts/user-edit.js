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
  let editImg = document.querySelector("#edit-img").value;
  let editName = document.querySelector("#edit-name").value;
  let editPw = document.querySelector("#edit-pw").value;

  const formData = new FormData(form);
  // const payload = new URLSearchParams(prePayload);

  formData.append("profile_img", editImg);
  formData.append("username", editName);
  formData.append("password", editPw);
  console.log([...formData]);

  // let userData = {
  //   method: "PATCH",
  //   headers: {
  //     "Content-Type": "application/json",
  //     Authorization: "token " + token,
  //   },
  //   // data: payload,
  //   // body: JSON.stringify({
  //   //   profile_image: editImg,
  //   //   username: editName,
  //   //   password: editPw,
  //   // }),
  // };
  // fetch("http://13.125.61.174:8000/user/", userData)
  //   .then((response) => response.json())
  //   .then((res) => console.log(res))
  //   .catch((error) => console.log(error));
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
