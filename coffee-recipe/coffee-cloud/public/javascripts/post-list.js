let contents = document.querySelector("#contents");
let pages = document.querySelector("#page-cnt");

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
        res.PostList.forEach((post) => {
          html += `
        <div class="content" id="${post.id}">
          <div class = "coffee-img">
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
