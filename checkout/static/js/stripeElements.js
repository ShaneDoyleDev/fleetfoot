const stripePublicKey = document
  .getElementById("stripe-public-key")
  .textContent.trim();

const striptSecretKey = document
  .getElementById("stripe-secret-key")
  .textContent.trim();

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

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