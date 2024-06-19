// DOM Selectors
const countrySelect = document.querySelector("#id_default_country");

let countrySelected = "countrySelect.value";

if (!countrySelected) countrySelect.style.color = "#aab7c4";

// Event listeners
countrySelect.addEventListener("change", () => {
  countrySelected = countrySelect.value;
  if (!countrySelected) countrySelect.style.color = "#aab7c4";
  else countrySelect.style.color = "#333333";
});
