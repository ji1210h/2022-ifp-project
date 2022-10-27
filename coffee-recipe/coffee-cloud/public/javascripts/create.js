let token = localStorage.getItem("jwt-token");

const submitBtn = document.querySelector(".post-btn");

submitBtn.addEventListener("click", (e) => {
  e.preventDefault();

  var options = document.getElementById("material").selectedOptions;

  let category = document.querySelector("#category").value;
  let material = Array.from(options).map(({ value }) => value);
  // let image = document.querySelector("#upload-image").files[0].name;
  let title = document.querySelector("#title").value;
  let content = document.querySelector("#content").value;

  let postCreateData = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: "token " + token,
    },
    body: JSON.stringify({ title, content, category, material }),
  };

  fetch("http://13.125.61.174:8000/post/create/", postCreateData)
    .then((response) => response.json())
    .then((res) => {
      // console.log(image);
      // console.log(material);
      if (res.user) {
        // console.log("success");
        alert("글을 작성했습니다.");
        location.href = "index.html";
      } else {
        alert("모든 항목을 작성해주세요.");
      }
    });
});
