// DOM Selectors
const qtyInput = document.querySelector(".qty-input");
const hiddenQtyInput = document.querySelector(".hidden-qty-input");
const incrementQtyBtn = document.querySelector(".increment-qty-btn");
const decrementQtyBtn = document.querySelector(".decrement-qty-btn");

// Event Listeners

// Increment cart quantity
incrementQtyBtn?.addEventListener("click", () => {
  qtyInput.value = parseInt(qtyInput.value) + 1;
  hiddenQtyInput.value = parseInt(qtyInput.value);
});

// Decrement cart quantity
decrementQtyBtn?.addEventListener("click", () => {
  if (parseInt(qtyInput.value) > 1) {
    // Ensure qty cannot go below 1
    qtyInput.value = parseInt(qtyInput.value) - 1;
    hiddenQtyInput.value = parseInt(qtyInput.value);
  }
});
