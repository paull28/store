$(document).ready(function () {
    $('.add-to-basket-button').click(function () {
        var quantity = $('#qty-select').val(); // Get the selected quantity
        var notification = 'Added ' + quantity + ' item(s) to basket. ';
        var successContainer = $('.basket-success-container'); // Get the success container element
        successContainer.text(notification)
        successContainer.show()
    });
});