let token = localStorage.getItem("jwt-token");

let userData = {
  method: "GET",
  headers: {
    Authorization: token,
  },
};
// console.log(token);
fetch("http://13.125.61.174:8000/user/", {})
  .then((response) => response.json())
  .then((response) => {
    // console.log(response);
  });
