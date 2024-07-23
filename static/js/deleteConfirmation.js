// DOM Selectors
const showConfirmationBtns = document.querySelectorAll(
  ".show-delete-confirmation"
);
const hideConfirmationBtns = document.querySelectorAll(
  ".hide-delete-confirmation"
);

/**
 * Shows a delete confirmation modal for a product by removing the "hidden" class and adding the "flex" class.
 */
function showDeleteConfirmation(event) {
  const productId = event.currentTarget.dataset.productId;
  const deleteConfirmation = document.querySelector(
    `.delete-confirmation-modal[data-product-id="${productId}"]`
  );
  deleteConfirmation.classList.remove("hidden");
  deleteConfirmation.classList.add("flex");
}

/**
 * Hides a delete confirmation modal for a product by removing the "hidden" class and adding the "flex" class.
 */
function hideDeleteConfirmation(event) {
  const deleteConfirmation = event.currentTarget.closest(
    ".delete-confirmation-modal"
  );
  deleteConfirmation.classList.add("hidden");
  deleteConfirmation.classList.remove("flex");
}

showConfirmationBtns.forEach((btn) => {
  btn.addEventListener("click", showDeleteConfirmation);
});

hideConfirmationBtns?.forEach((btn) => {
  btn.addEventListener("click", hideDeleteConfirmation);
});
