let contents = document.querySelector("#contents");
let content = document.querySelector(".content");
let pages = document.querySelector("#page-cnt");
let body = document.querySelector("#body");

let postData = {
  method: "GET",
};

function postHtml() {
  return fetch("http://13.125.61.174:8000/post/", postData)
    .then((response) => response.json())
    .then((res) => {
      console.log(res);
      let html = "";
      if (res.PostList) {
        console.log(res.curPage);
        res.PostList.forEach((post) => {
          html += `
        <div class="content" id="${post.id}">
          <div class = "coffee-img" >
            <img src="http://13.125.61.174:8000${post.image}" alt="default"/>
          </div>
          <div class="text-box" >
            <div class="coffee-text" id="${post.id}">
              <h3 class="title">${post.title}</h3>
              <p class="author">${post.user}</p>
            </div>
            <div class="liked" id="${post.id}">
              <i class="fa-regular fa-heart"></i>
            </div>
          </div>
        </div>
          `;
        });
      }
      contents.innerHTML = html;

      let html2 = "";
      if (res.PageCnt) {
        // console.log(res.PageCnt);
        for (let i = 1; i < res.PageCnt + 1; i++) {
          // console.log(i);
          html2 = `<li>${i}</li>`;
          pages.innerHTML += html2;
        }
      }
    });
}

postHtml();
// --------------------------------------------------

let postAboutData = {
  method: "GET",
};

let categoryRead = document.getElementById("category-read");
let titleRead = document.getElementById("title-read");
let materialRead = document.getElementById("material-read");
let contentRead = document.getElementById("content-read");
let author = document.getElementById("author");
let postDate = document.getElementById("post-date");

let section = document.querySelector("section");
let wrapper = document.querySelector(".post-read");

contents.addEventListener("click", moveToPage);

function moveToPage(e) {
  e.preventDefault();
  const id = e.target.parentElement.id;

  fetch(`http://13.125.61.174:8000/post/${id}`, postAboutData)
    .then((response) => response.json())
    .then((res) => {
      console.log(res);
      author.innerText = res.user;
      postDate.innerText = res.create_dt.substr(0, 10);
      categoryRead.innerText = res.category;
      titleRead.innerText = res.title;
      materialRead.innerText = `[재료] ${res.material}`;
      contentRead.innerText = res.content;

      section.classList.add("hidden");
      wrapper.classList.remove("hidden");
    });
}
