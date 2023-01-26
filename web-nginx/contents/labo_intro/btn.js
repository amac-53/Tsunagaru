const btn = document.querySelector('.btn-box button');

btn.addEventListener('click', () => {
    const more = document.querySelector('.more');
    more.classList.toggle('appear');

    if (btn.textContent == "もっと見る") {
        btn.textContent = "閉じる";
    } else {
        btn.textContent = "もっと見る";
    }
});