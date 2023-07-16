// Add an event listener to all elements with the product-container class
document.addEventListener('DOMContentLoaded', function() {
    var productContainers = document.getElementsByClassName('product-container');
    
    for (var i = 0; i < productContainers.length; i++) {
        productContainers[i].addEventListener('click', redirectToProductPage);
    }
});

function redirectToProductPage() {
    // Extract the product ID or other relevant information from the clicked element or its data attributes
    // Replace the placeholder with the actual URL of your product page, passing the necessary information
    var productId = this.dataset.productId;
    var productPageUrl = '/store/' + productId; // Replace with your product page URL
    
    // Redirect to the product page
    window.location.href = productPageUrl;
}