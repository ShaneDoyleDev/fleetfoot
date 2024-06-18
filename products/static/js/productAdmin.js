// DOM Selectors
const addProductForm = document.querySelector(".product-form");
const toggleProductForm = document.querySelector(".toggle-product-form");
const stockForm = document.querySelector(".stock-form");
const toggleStockForm = document.querySelector(".toggle-stock-form");
const productDropdown = document.querySelector(".stock-product-dropdown");
const sizeSelect = document.querySelector("#size");

// Set toggleProductForm to active by default
toggleProductForm.classList.add("bg-black", "text-white");

/**
 * Toggles the visibility of a form based on the selected toggle button.
 */
function toggleFormVisibility(toggleButton, formToShow, formToHide) {
  [toggleProductForm, toggleStockForm].forEach((button) => {
    button.classList.remove("bg-black", "text-white");
  });

  toggleButton.classList.add("bg-black", "text-white");

  formToShow.classList.add("flex");
  formToShow.classList.remove("hidden");
  formToHide.classList.add("hidden");
  formToHide.classList.remove("flex");
}

/**
 * Updates the available sizes for a product.
 */
function updateSizes(productId) {
  const sizeSelect = document.getElementById("size");
  sizeSelect.classList.add("disabled");
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  fetch("/products/get-product-sizes/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ product_id: productId }),
  })
    .then((response) => response.json())
    .then((data) => {
      sizeSelect.innerHTML = "";
      data.sizes.forEach((size) => {
        const option = new Option(
          `${size.department_name} Size ${size.size}`,
          size.id
        );
        sizeSelect.add(option);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    })
    .finally(() => {
      sizeSelect.classList.remove("disabled");
    });
}

// Event Listeners
toggleProductForm.addEventListener("click", () => {
  toggleFormVisibility(toggleProductForm, addProductForm, stockForm);
});

toggleStockForm.addEventListener("click", () => {
  toggleFormVisibility(toggleStockForm, stockForm, addProductForm);
});

productDropdown.addEventListener("change", (e) => {
  const productId = e.target.value;
  updateSizes(productId);
});
