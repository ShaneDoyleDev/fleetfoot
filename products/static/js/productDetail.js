// DOM Selectors
const qtyInput = document.querySelector(".qty-input");
const incrementQtyBtn = document.querySelector(".increment-qty-btn");
const decrementQtyBtn = document.querySelector(".decrement-qty-btn");
const addToCartBtn = document.querySelector(".add-to-cart-btn");
const sizes = document.querySelectorAll(".size");
const sizeInput = document.querySelector(".size-input");

addToCartBtn.classList.add("disabled");

sizes.forEach((size) => {
  size.addEventListener("click", () => {
    sizes.forEach((size) => {
      size.classList.remove("selected");
    });

    size.classList.add("selected");
    sizeInput.value = size.innerText;
    addToCartBtn.classList.remove("disabled");
    addToCartBtn.innerText = "Add to Cart";
  });
});

// Event Listeners

// Increment cart quantity
incrementQtyBtn.addEventListener("click", () => {
  qtyInput.value = parseInt(qtyInput.value) + 1;
});

// Decrement cart quantity
decrementQtyBtn.addEventListener("click", () => {
  if (parseInt(qtyInput.value) > 1) {
    // Ensure qty cannot go below 1
    qtyInput.value = parseInt(qtyInput.value) - 1;
  }
});
