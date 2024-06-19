// DOM Selectors
const registrationForm = document.querySelector(".registration-form");
const openRegistrationBtns = document.querySelectorAll(".open-registration");
const closeRegistrationBtn = document.querySelector(".close-registration");

const loginForm = document.querySelector(".login-form");
const openLoginBtns = document.querySelectorAll(".open-login");
const closeLoginBtn = document.querySelector(".close-login");

/**
 * Shows a form by removing the "hidden" class and adding the "flex" class.
 */
function showForm(form) {
  form.classList.remove("hidden");
  form.classList.add("flex");
}

/**
 * Hides the specified form by adding the "hidden" class and removing the "flex" class.
 */
function hideForm(form) {
  form.classList.add("hidden");
  form.classList.remove("flex");
}

// Event listeners
openRegistrationBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    showForm(registrationForm);
    hideForm(loginForm);
  });
});
closeRegistrationBtn.addEventListener("click", () =>
  hideForm(registrationForm)
);

openLoginBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    showForm(loginForm);
    hideForm(registrationForm);
  });
});
closeLoginBtn.addEventListener("click", () => hideForm(loginForm));

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    hideForm(registrationForm);
    hideForm(loginForm);
  }
});
