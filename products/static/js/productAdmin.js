// DOM Selectors
const addProductForm = document.querySelector(".product-form");
const toggleProductForm = document.querySelector(".toggle-product-form");
const stockForm = document.querySelector(".stock-form");
const toggleStockForm = document.querySelector(".toggle-stock-form");

// Set toggleProductForm to active by default
toggleProductForm.classList.add("bg-black", "text-white");

/**
 * Toggles the visibility of a form based on the selected toggle button.
 */
function toggleFormVisibility(toggleButton, formToShow, formToHide) {
  [toggleProductForm, toggleStockForm].forEach((button) => {
    button.classList.remove("bg-black", "text-white");
  });

  // Set the active toggle button style
  toggleButton.classList.add("bg-black", "text-white");

  // Show the target form and hide the other
  formToShow.classList.add("flex");
  formToShow.classList.remove("hidden");
  formToHide.classList.add("hidden");
  formToHide.classList.remove("flex");
}

// Event Listeners
toggleProductForm.addEventListener("click", () => {
  toggleFormVisibility(toggleProductForm, addProductForm, stockForm);
});

toggleStockForm.addEventListener("click", () => {
  toggleFormVisibility(toggleStockForm, stockForm, addProductForm);
});
