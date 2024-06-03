document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button'); // Выберите все кнопки

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonId = button.id; // Получите ID кнопки
            console.log(`Вы нажали на кнопку с ID: ${buttonId}`);
            if (button.textContent === '+'){addToCart(buttonId)}
            if (button.textContent === '-'){minToCart(buttonId-100)}
        });
    });

});


function addToCart(productId) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получите CSRF-токен
    console.log(`Вы добавили товар с ID: ${productId} в корзину`);
    fetch(`/add_to_cart/${productId}/`, {
        method: 'PUT',
        headers: {
            'X-CSRFToken': csrfToken // Добавьте CSRF-токен в заголовок запроса
        }
    })
        .then(response => {
            if (response.ok) {
                kol = document.getElementById(Number(productId)+300)
                kol.textContent = Number(kol.textContent)+1

            } else {

            }
        });
}

function minToCart(productId) {
    kol = document.getElementById(Number(productId)+300)
    console.log(kol)
    kol.textContent = Number(kol.textContent)-1
    if (Number(kol.textContent) < 0){
        console.log((Number(kol.textContent === 1)), Number(kol.textContent));
        location.reload();}
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получите CSRF-токен
    console.log(`Вы добавили товар с ID: ${productId} в корзину`);
    fetch(`/min_to_cart/${productId}/`, {
        method: 'PUT',
        headers: {
            'X-CSRFToken': csrfToken // Добавьте CSRF-токен в заголовок запроса
        }
    })
        .then(response => {
            if (response.ok) {

            } else {
            }
        });
}