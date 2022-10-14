let toolbarOptions = [
  [{ header: [1, 2, 3, 4, 5, false] }],
  ["bold", "italic", "underline"],
  [{ color: [] }, { background: [] }],
  [({ list: "ordered" }, { list: "bullet" })],
  [{ indent: "+1" }, { indent: "-1" }],
  [{ align: [] }],
  ["image", "link", "video"],
];

var quill = new Quill("#editor", {
  modules: {
    // toolbar: true,
    toolbar: toolbarOptions,
  },
  theme: "snow",
});
