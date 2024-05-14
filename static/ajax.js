const statusLinks = document.querySelectorAll("a.status-link");
for (const statusLink of statusLinks) {
  statusLink.addEventListener("click", (evt) => {
    evt.preventDefault();
    console.log(evt.target.style.fill);
    // const cardId = evt.target.getAttribute('data-card-id');
    // const card = document.getElementById(cardId);

    // card.classList.toggle('pink-background');
    if (evt.target.style.fill === "rgb(229, 77, 201)") {
      evt.target.style.fill = "rgb(45,51,235)";
    } else {
      evt.target.style.fill = "rgb(229, 77, 201)";
    }
  });
}

// const svgChangeButtons = document.querySelectorAll("svg-changer");
// for (const svgChangeButton of svgChangeButtons) {
//   svgChangeButton.addEventListener("click", (evt) => {
// evt.preventDefault();
//
// const svgElement = svgChangeButton.querySelector("svg");
// svgElement.style.fill = "#E54DC9";
//   });
// }

{
  /* drag & drop future draft */
}
// Function to handle drag start
function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

// Function to allow dropping
function allowDrop(ev) {
  ev.preventDefault();
}

// Function to handle drop
function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
