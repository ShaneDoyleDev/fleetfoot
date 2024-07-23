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
  deleteConfirmation.classList.remove("hidden");
  deleteConfirmation.classList.add("flex");
}

/**
 * Hides a delete confirmation modal for a product by removing the "hidden" class and adding the "flex" class.
 */
  deleteConfirmation.classList.add("hidden");
  deleteConfirmation.classList.remove("flex");
}

showConfirmationBtns.forEach((btn) => {
  btn.addEventListener("click", showDeleteConfirmation);
});

hideConfirmationBtns?.forEach((btn) => {
  btn.addEventListener("click", hideDeleteConfirmation);
});
