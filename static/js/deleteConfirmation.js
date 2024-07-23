const deleteConfirmation = document.querySelector(".delete-confirmation-modal");
const showConfirmationBtns = document.querySelectorAll(
  ".show-delete-confirmation"
);
const hideConfirmationBtn = document.querySelector(".hide-delete-confirmation");

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
hideConfirmationBtn?.addEventListener("click", hideDeleteConfirmation);
