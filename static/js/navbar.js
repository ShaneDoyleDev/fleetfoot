// DOM Selectors
const mobileNav = document.querySelector(".mobile-nav");
const openMobileNavbtn = document.querySelector(".open-mobile-nav");
const closeMobileNavBtn = document.querySelector(".close-mobile-nav");

/**
 * Shows the mobile nav menu.
 */
function showMobileNav() {
  mobileNav.classList.remove("hidden");
  mobileNav.classList.add("flex");
}

/**
 * Hides the mobile nav menu.
 */
function hideMobileNav() {
  mobileNav.classList.add("hidden");
  mobileNav.classList.remove("flex");
}

// Event listeners
openMobileNavbtn.addEventListener("click", showMobileNav);
closeMobileNavBtn.addEventListener("click", hideMobileNav);

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") hideMobileNav();
});
