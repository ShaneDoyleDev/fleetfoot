const stripePublicKey = document
  .getElementById("stripe-public-key")
  .textContent.trim()
  .slice(1, -1);

const paymentIntentClientSecret = document
  .getElementById("payment-intent-client-secret")
  .textContent.trim()
  .slice(1, -1);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Add styling to stripe card element
const style = {
  base: {
    color: "#333333",
    fontFamily: `"Roboto", sans-serif`,
    fontSmoothing: "antialiased",
    fontSize: "1rem",
    "::placeholder": {
      color: "#9ca3af",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};

const cardElementContainer = document.getElementById("card-element");
cardElementContainer.style.border = "1px solid #cbd5e1";
cardElementContainer.style.borderRadius = "5px";
cardElementContainer.style.padding = "12px";
cardElementContainer.style.backgroundColor = "#f9fafb";

const card = elements.create("card", { style });
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", (event) => {
  const errorDiv = document.getElementById("card-errors");
  if (event.error) {
    const html = `
            <span style="color: #f87171;">${event.error.message}</span>
        `;
    errorDiv.innerHTML = html;
  } else {
    errorDiv.textContent = "";
  }
});

// Handle form submit
const form = document.getElementById("payment-form");

form.addEventListener("submit", (event) => {
  // Prevent the form from submitting and show the loading overlay
  event.preventDefault();
  card.update({ disabled: true });
  document.getElementById("submit-button").disabled = true;
  document.getElementById("loading-overlay").classList.remove("hidden");
  document.getElementById("loading-overlay").classList.add("flex");

  // Add additional meta data to the payment intent
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const url = "/checkout/cache-checkout-data/";
  const postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: paymentIntentClientSecret,
  };

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(postData),
  })
    .then(() => {
      // Confirm the card payment
      stripe
        .confirmCardPayment(paymentIntentClientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              name: form.full_name.value.trim(),
              phone: form.phone_number.value.trim(),
              email: form.email.value.trim(),
              address: {
                line1: form.street_address1.value.trim(),
                line2: form.street_address2.value.trim(),
                city: form.town_or_city.value.trim(),
                country: form.country.value.trim(),
                state: form.county.value.trim(),
              },
            },
          },
          shipping: {
            name: form.full_name.value.trim(),
            phone: form.phone_number.value.trim(),
            address: {
              line1: form.street_address1.value.trim(),
              line2: form.street_address2.value.trim(),
              city: form.town_or_city.value.trim(),
              country: form.country.value.trim(),
              postal_code: form.postcode.value.trim(),
              state: form.county.value.trim(),
            },
          },
        })
        .then((result) => {
          // Handle payment intent response
          if (result.error) {
            const errorDiv = document.getElementById("card-errors");
            const html = `
            <span style="color: #f87171;">${result.error.message}</span>`;
            errorDiv.innerHTML = html;
            card.update({ disabled: false });
            document.getElementById("loading-overlay").classList.add("hidden");
            document.getElementById("loading-overlay").classList.remove("flex");
            document.getElementById("submit-button").disabled = false;
          } else {
            if (result.paymentIntent.status === "succeeded") form.submit();
          }
        });
    })
    .catch((error) => {
      console.error("Fetch error:", error);
      location.reload();
    });
});
