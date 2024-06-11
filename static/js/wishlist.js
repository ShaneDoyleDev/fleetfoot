/**
 * Retrieves the value of a cookie by its name.
 * Taken from https://docs.djangoproject.com/en/4.2/howto/csrf/
 */
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie("csrftoken");

// This JavaScript code toggles the wishlist status of a product by and updates
// the wishlist icon based on the server's response.
document.querySelectorAll("#wishlist-toggle").forEach(function (button) {
  button.addEventListener("click", function () {
    var productId = this.getAttribute("data-product-id");
    var icon = this.querySelector("img");

    fetch(`/profiles/toggle-wishlist-item/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": csrftoken,
      },
      body: new URLSearchParams({
        product_id: productId,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "ok") {
          const wishlistIconUrl = icon.getAttribute("data-wishlist-icon-url");
          const heartOutlineIconUrl = icon.getAttribute(
            "data-heart-outline-icon-url"
          );

          if (data.action === "added") {
            icon.src = wishlistIconUrl;
          } else {
            icon.src = heartOutlineIconUrl;
          }
        }
      });
  });
});
