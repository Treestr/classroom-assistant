
const statusLinks =document.querySelectorAll('a.status-link');
for (const statusLink of statusLinks) {
    statusLink.addEventListener('click', (evt) => {
        evt.preventDefault();

        const cardId = evt.target.getAttribute('data-card-id');
        const card = document.getElementById(cardId);

        card.classList.toggle('pink-background');
    })
}
