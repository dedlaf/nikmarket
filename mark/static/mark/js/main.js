document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button'); // Выберите все кнопки

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonId = button.id; // Получите ID кнопки
            console.log(`Вы нажали на кнопку с ID: ${buttonId}`);
            addToCart(buttonId);
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
                console.log('Товар успешно добавлен в корзину');
            } else {
                console.error('Ошибка при добавлении товара в корзину');
            }
        });
}