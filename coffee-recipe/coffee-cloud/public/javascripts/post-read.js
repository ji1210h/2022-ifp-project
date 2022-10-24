let categoryRead = document.getElementById("category-read");
let titleRead = document.getElementById("title-read");
let contentRead = document.getElementById("content-read");
let author = document.getElementById("author");
let postDate = document.getElementById("post-date");

let postAboutData = {
  method: "GET",
};

function moveToPage(e) {
  e.preventDefault();
  const id = e.target.parentElement.id;
  let url = `http://13.125.61.174:8000/post/${id}`;
  fetch(url, postAboutData)
    .then((response) => response.json())
    .then((res) => {
      console.log(res);

      author.innerText = res.user;
      postDate.innerText = res.create_dt.substr(0, 10);
      categoryRead.innerText = res.category;
      titleRead.innerText = res.title;
      contentRead.innerText = res.content;
    });
}

postHtml();
contents.addEventListener("click", moveToPage);
