// Function to initialize the cart
function initializeCart() {
    // Check if the cart exists in localStorage
    let cart = localStorage.getItem('cart');
    if (!cart) {
        // If cart doesn't exist, initialize it as an empty array
        cart = [];
        localStorage.setItem('cart', JSON.stringify(cart));
    }
}

// Function to update the cart display
function updateCartDisplay() {
    // Get the cart from localStorage
    let cart = JSON.parse(localStorage.getItem('cart'));
    // Display total items and total price in the cart
    let totalItems = cart.length;
    let totalPrice = cart.reduce((total, item) => total + item.price, 0).toFixed(2);
    document.getElementById('cart-total-items').innerText = totalItems;
    document.getElementById('cart-total-price').innerText = `$${totalPrice}`;
}

// Function to add an item to the cart
function addToCart(name, price) {
    // Get the cart from localStorage
    let cart = JSON.parse(localStorage.getItem('cart'));
    // Add the item to the cart
    cart.push({ name: name, price: price });
    // Save the updated cart to localStorage
    localStorage.setItem('cart', JSON.stringify(cart));
    // Update the cart display
    updateCartDisplay();
}

// Function to display item details modal
function displayItemDetails(name, description, price) {
    // Display modal with provided information
    document.getElementById('item-details-modal').style.display = 'block';
    document.getElementById('item-name').innerText = name;
    document.getElementById('item-description').innerText = description;
    document.getElementById('item-price').innerText = `$${price}`;
}

// Function to close item details modal
function closeItemDetailsModal() {
    // Close modal
    document.getElementById('item-details-modal').style.display = 'none';
}

// Function to submit the form data (e.g., make AJAX request to backend)
function submitFormData(formData) {
    // Submit form data (e.g., make AJAX request)
}

// Event listener for Add to Cart buttons
document.querySelectorAll('.add-to-cart-btn').forEach(button => {
    button.addEventListener('click', () => {
        let productDiv = button.closest('.product');
        let itemName = productDiv.querySelector('h3').innerText;
        let itemPrice = parseFloat(productDiv.querySelector('p').innerText.substring(1));
        addToCart(itemName, itemPrice);
        alert(`Added ${itemName} to cart!`);
    });
});

// Event listener for View Details buttons
document.querySelectorAll('.item-details-btn').forEach(button => {
    button.addEventListener('click', () => {
        let productDiv = button.closest('.product');
        let itemName = productDiv.querySelector('h3').innerText;
        let itemDescription = productDiv.querySelector('p:nth-child(3)').innerText;
        let itemPrice = parseFloat(productDiv.querySelector('p:nth-child(4)').innerText.substring(1));
        displayItemDetails(itemName, itemDescription, itemPrice);
    });
});

// Event listener for Close modal button
document.getElementById('close-modal-btn').addEventListener('click', () => {
    closeItemDetailsModal();
});

// Event listener for Submit form button
document.getElementById('submit-form-btn').addEventListener('click', () => {
    let formData = {
        // Retrieve form data here
    };
    submitFormData(formData);
});

// Initialize the cart and update cart display when the page loads
window.addEventListener('load', () => {
    initializeCart();
    updateCartDisplay();
});
