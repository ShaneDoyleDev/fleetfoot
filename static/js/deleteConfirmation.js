const deleteConfirmation = document.querySelector(".delete-confirmation-modal");
const showConfirmationBtns = document.querySelectorAll(
  ".show-delete-confirmation"
);
const hideConfirmationBtn = document.querySelector(".hide-delete-confirmation");

function showDeleteConfirmation() {
  deleteConfirmation.classList.remove("hidden");
  deleteConfirmation.classList.add("flex");
}

function hideDeleteConfirmation() {
  deleteConfirmation.classList.add("hidden");
  deleteConfirmation.classList.remove("flex");
}

showConfirmationBtns.forEach((btn) => {
  btn.addEventListener("click", showDeleteConfirmation);
});
hideConfirmationBtn?.addEventListener("click", hideDeleteConfirmation);
