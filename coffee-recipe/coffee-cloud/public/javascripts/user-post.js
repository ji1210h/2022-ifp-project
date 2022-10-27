let contentList = document.querySelector("#content-list");

let myPostData = {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    Authorization: "token " + token,
  },
};

fetch("http://13.125.61.174:8000/post/my", myPostData)
  .then((response) => response.json())
  .then((res) => {
    console.log(res);
    let html = "";
    if (res.coffee) {
      res.coffee.forEach((post) => {
        html += `
                <form>
                <ul class="content-post" id="${post.id}">

                    <li class="item id" id="">${post.id}</li>
                    <li class="item title" id="post-title">${post.title}</li>
                    <li class="item category" id="post-category">${
                      post.category
                    }</li>
                    <li class="item date" id="post-date">
                    ${post.create_dt.substr(0, 10)}</li>
                    <li class="item liked" id="post-liked">${
                      post.bookmark_user
                    }</li>
                </ul>
                </form>
                `;
      });
    }
    contentList.innerHTML = html;
  });

contentList.addEventListener("click", moveToPage);
