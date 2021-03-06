function init() {
    let votingButtons = document.querySelectorAll('.voting-button');
    for (let votingButton of votingButtons) {
        votingButton.addEventListener('click', voteClick);
    }
}

function voteClick(event) {
    let voteButton = event.target;
    let voteDirection = voteButton.dataset.vote;
    let playerId = voteButton.dataset.id;

    fetch(`/player/${playerId}/vote/${voteDirection}`, {method: 'POST'})
        .then(() => {
            let voteCell = voteButton.closest('.player').querySelector('.vote-cell');
            voteCell.innerText = parseInt(voteCell.innerText) + (voteDirection === 'up' ? 1 : -1);
        });
}

init();