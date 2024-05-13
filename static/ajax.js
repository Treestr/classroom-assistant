
const statusLinks =document.querySelectorAll('a.status-link');
for (const statusLink of statusLinks) {
    statusLink.addEventListener('click', (evt) => {
        evt.preventDefault();

        const cardId = evt.target.getAttribute('data-card-id');
        const card = document.getElementById(cardId);

        card.classList.toggle('pink-background');
    })
}

const svgChangeButtons = document.querySelectorAll('svg-changer')
for (const svgChangeButton of svgChangeButtons) {
  svgChangeButton.addEventListener('click', (evt) => {
    evt.preventDefault();
    // the button ID contains the font we want to change to
    const svgElement = svgChangeButton.querySelector('svg');
    svgElement.style.fill = "#E54DC9"
  });
}
Further Study
