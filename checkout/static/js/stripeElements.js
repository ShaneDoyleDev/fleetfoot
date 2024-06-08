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

let cardElementContainer = document.getElementById("card-element");
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
  event.preventDefault();
  card.update({ disabled: true });
  document.getElementById("submit-button").disabled = true;
  stripe
    .confirmCardPayment(paymentIntentClientSecret, {
      payment_method: {
        card: card,
      },
    })
    .then((result) => {
      if (result.error) {
        const errorDiv = document.getElementById("card-errors");
        const html = `
                <span style="color: #f87171;">${result.error.message}</span>`;
        errorDiv.innerHTML = html;
        card.update({ disabled: false });
        document.getElementById("submit-button").disabled = false;
      } else {
        if (result.paymentIntent.status === "succeeded") {
          form.submit();
        }
      }
    });
});
