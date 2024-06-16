# Testing Documentation

Visit the deployed site: [Fleetfoot](https://fleetfoot-df010c0d8dc8.herokuapp.com/)

## Table of Contents

- [Validator Testing](#validator-testing)

  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Javascript Validation](#javascript-validation)
  - [Python Validation](#python-validation)
  - [Accessibility](#accessibility)

- [Lighthouse Testing](#lighthouse-testing)

- [Device Testing](#device-testing)

  - [Devices](#devices)
  - [Browsers](#browsers)
  - [Responsiveness](#responsiveness)

- [Manual Testing](#manual-testing)

  - [User Stories Testing](#user-stories-testing)
  - [Feature Testing](#feature-testing)

- [Bugs](#bugs)

## Validator Testing

### HTML Validation

[W3C HTML Validation Service](https://validator.w3.org/)

During initial testing of my templates through the W3C HTML Validation Service, I noticed that there were several repeated warnings or errors encountered across multiple pages. These were all due to the usage of the [Alpine JS](https://alpinejs.dev/) framework in this project, which requires special attributes and directives on the HTML elements to work. In order to ensure my code would pass validation, I refactored it by removing Alpine JS from my project and refactoring the code to just use vanilla JavaScript. I am happy to say that my code **passed all validations**.

- [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2F) - pass

- [Products List Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fproducts%2Fdepartment%2Fmens) - pass

- [Product Detail Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fproducts%2Fproduct-detail%2F12%2F) - pass

- [Shopping Cart Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fcart%2F) - pass

- [Checkout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fcheckout%2F) - pass

- [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fprofiles%2F) - pass

- [Wishlist Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fprofiles%2Fwishlist%2F) - pass

- [Product Admin Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffleetfoot-df010c0d8dc8.herokuapp.com%2Fproducts%2Fproduct-admin%2F) - pass

- 404 Page (Validator would not recognize URL for 404, so uploaded the html manually)

404 page results:

<img src="./readme-images/testing/validation/html/html-404-validation.png" alt="html validation results for 404 page">

</br>

### CSS Validation

All of the CSS was generated from the build process of the [Tailwind](https://tailwindcss.com) framework in the project using the [Django Tailwind](https://github.com/timonweb/django-tailwind) package, so there was not much to test here. I did write some of my own global CSS styles, which I uploaded to check through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fnews-bytes-f757f042ac64.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - pass

Stylesheet results:

<img src="./readme-images/testing/validation/css/validated-css.png" alt="validated css results">

### Javascript Validation

[JSHint](https://jshint.com/) - Was used to validate my Javascript code.

#### navbar.js results

<img src="./readme-images/testing/validation/js/js-validate-navbar.webp" alt="navbar.js validation results">

#### productDetail.js results

<img src="./readme-images/testing/validation/js/js-validate-product-detail.webp" alt="productDetail.js validation results">

#### cart.js results

<img src="./readme-images/testing/validation/js/js-validate-cart.webp" alt="cart.js validation results">

#### wishlist.js results

<img src="./readme-images/testing/validation/js/js-validate-wishlist.webp" alt="wishlist.js validation results">

#### productAdmin.js results

<img src="./readme-images/testing/validation/js/js-validate-product-admin.webp" alt="productAdmin.js validation results">

#### modals.js results

<img src="./readme-images/testing/validation/js/js-validate-modals.webp" alt="modals.js validation results">

#### stripeElements.js results

<img src="./readme-images/testing/validation/js/js-validate-stripeElements.webp" alt="stripeElements.js validation results">

#### countryField.js results

<img src="./readme-images/testing/validation/js/js-validate-countryField.webp" alt="countryField.js validation results">

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to review and validate each Python script, ensuring they met coding standards without errors. Initially, it highlighted that some lines in the scripts exceeded the character limit. This prompted a refactoring of the code to resolve these issues. As a result, all scripts have been revised and are now error-free.

#### manage.py results

<img src="./readme-images/testing/validation/python/manage.png" alt="manage.py validation results">

#### utils.py results

<img src="./readme-images/testing/validation/python/utils.png" alt="utils.py validation results">

#### fleetfoot/asgi.py results

<img src="./readme-images/testing/validation/python/asgi.png" alt="commit/asgi.py validation results">

#### fleetfoot/settings.py results

<img src="./readme-images/testing/validation/python/fleetfoot-settings.png" alt="fleetfoot/settings.py validation results">

#### fleetfoot/urls.py results

<img src="./readme-images/testing/validation/python/fleetfoot-urls.png" alt="fleetfoot/urls.py validation results">

#### fleetfoot/wsgi.py results

<img src="./readme-images/testing/validation/python/fleetfoot-wsgi.png" alt="fleetfoot/wsgi.py validation results">

#### home/admin.py results

<img src="./readme-images/testing/validation/python/home-admin.webp" alt="home/admin.py validation results">

#### home/apps.py results

<img src="./readme-images/testing/validation/python/home-apps.webp" alt="home/apps.py validation results">

#### home/context_processors.py results

<img src="./readme-images/testing/validation/python/home-context_processors.webp" alt="home/context_processors.py validation results">

#### home/forms.py results

<img src="./readme-images/testing/validation/python/home-forms.py.webp" alt="home/forms.py validation results">

#### home/models.py results

<img src="./readme-images/testing/validation/python/home-models.webp" alt="home/models.py validation results">

#### home/urls.py results

<img src="./readme-images/testing/validation/python/home-urls.webp" alt="home/urls.py validation results">

#### home/views.py results

<img src="./readme-images/testing/validation/python/home-views.webp" alt="home/views.py validation results">

#### products/admin.py results

<img src="./readme-images/testing/validation/python/products-admin.webp" alt="products/admin.py validation results">

#### products/apps.py results

<img src="./readme-images/testing/validation/python/products-apps.webp" alt="products/apps.py validation results">

#### products/forms.py results

<img src="./readme-images/testing/validation/python/products-forms.webp" alt="products/forms.py validation results">

#### products/models.py results

<img src="./readme-images/testing/validation/python/products-models.webp" alt="products/models.py validation results">

#### products/tests.py results

<img src="./readme-images/testing/validation/python/products-tests.webp" alt="products/tests.py validation results">

#### products/urls.py results

<img src="./readme-images/testing/validation/python/products-urls.webp" alt="products/urls.py validation results">

#### products/validators.py results

<img src="./readme-images/testing/validation/python/products-validators.webp" alt="products/validators.py validation results">

#### products/views.py results

<img src="./readme-images/testing/validation/python/products-views.webp" alt="products/views.py validation results">

#### products/initialise_store_data.py results

<img src="./readme-images/testing/validation/python/products-initialise_store_data.webp" alt="products/initialise_store_data.py validation results">

#### products/range_filter.py results

<img src="./readme-images/testing/validation/python/products-range_filter.webp" alt="products/range_filter.py validation results">

#### cart/admin.py results

<img src="./readme-images/testing/validation/python/cart-admin.webp" alt="cart/admin.py validation results">

#### cart/apps.py results

<img src="./readme-images/testing/validation/python/cart-apps.webp" alt="cart/apps.py validation results">

#### cart/context-processors.py results

<img src="./readme-images/testing/validation/python/cart-context_processors.webp" alt="cart/forms.py validation results">

#### cart/models.py results

<img src="./readme-images/testing/validation/python/cart-models.webp" alt="cart/models.py validation results">

#### cart/tests.py results

<img src="./readme-images/testing/validation/python/cart-tests.webp" alt="cart/tests.py validation results">

#### cart/urls.py results

<img src="./readme-images/testing/validation/python/cart-urls.webp" alt="cart/urls.py validation results">

#### cart/views.py results

<img src="./readme-images/testing/validation/python/cart-views.webp" alt="cart/views.py validation results">

#### cart/cart_tools.py results

<img src="./readme-images/testing/validation/python/cart-cart_tools.webp" alt="cart/cart_tools.py validation results">

#### checkout/admin.py results

<img src="./readme-images/testing/validation/python/checkout-admin.webp" alt="checkout/admin.py validation results">

#### checkout/apps.py results

<img src="./readme-images/testing/validation/python/checkout-apps.webp" alt="checkout/apps.py validation results">

#### checkout/forms.py results

<img src="./readme-images/testing/validation/python/checkout-forms.webp" alt="checkout/forms.py validation results">

#### checkout/models.py results

<img src="./readme-images/testing/validation/python/checkout-models.webp" alt="checkout/models.py validation results">

#### checkout/signals.py results

<img src="./readme-images/testing/validation/python/checkout-signals.webp" alt="checkout/signals.py validation results">

#### checkout/tests.py results

<img src="./readme-images/testing/validation/python/checkout-tests.webp" alt="checkout/tests.py validation results">

#### checkout/urls.py results

<img src="./readme-images/testing/validation/python/checkout-urls.webp" alt="checkout/urls.py validation results">

#### checkout/views.py results

<img src="./readme-images/testing/validation/python/checkout-views.webp" alt="checkout/views.py validation results">

#### checkout/webhooks_handler.py results

<img src="./readme-images/testing/validation/python/checkout-webhook_handler.webp" alt="cart/webhooks_handler.py validation results">

#### checkout/webhooks.py results

<img src="./readme-images/testing/validation/python/checkout-webhooks.webp" alt="cart/webhooks.py validation results">

#### profiles/admin.py results

<img src="./readme-images/testing/validation/python/profiles-admin.webp" alt="profiles/admin.py validation results">

#### profiles/apps.py results

<img src="./readme-images/testing/validation/python/profiles-apps.webp" alt="profiles/apps.py validation results">

#### profiles/forms.py results

<img src="./readme-images/testing/validation/python/profiles-forms.webp" alt="profiles/forms.py validation results">

#### profiles/models.py results

<img src="./readme-images/testing/validation/python/profiles-models.webp" alt="profiles/models.py validation results">

#### profiles/tests.py results

<img src="./readme-images/testing/validation/python/profiles-tests.webp" alt="profiles/tests.py validation results">

#### profiles/urls.py results

<img src="./readme-images/testing/validation/python/profiles-urls.webp" alt="profiles/urls.py validation results">

#### profiles/views.py results

<img src="./readme-images/testing/validation/python/profiles-views.webp" alt="profiles/views.py validation results">

</br>

### Accessibility

I ensured that my site followed good accessibility practices by using alt attributes across all image tags and including aria labels on all necessary elements for screen readers. As a result, my initial accessibility testing using Google Lighthouse revealed very good scores across all pages as shown in the [Lighthouse Testing](#lighthouse-testing) section of the readme.

- **Wave testing**

  <img width="200" src="./readme-images/testing/accessability/wave-testing.webp" alt="wave validation results">

  Using the [WAVE accessibility tool](https://wave.webaim.org/), as an additional fomr of testing, I found the results to be good, save for a few small errors. I attempted to go through them and address what I could.

- **Alt attribute issue**

  <img src="./readme-images/testing/accessability/alt-attributes.webp" alt="alt attributes">

  WAVE would seemingly flag certain img elements as false positives, saying that there was no alt attribute present on the element even though there was.

</br>

- **Mailchimp form issue**

  <img src="./readme-images/testing/accessability/mailchimp-form.webp" alt="mailchimp">

  When integrating the Mailchimp newsletter form generated from Mailchimp, WAVE seemed to have issues with how the form was structured. I didn't want to change anything here as I did not want to potentially break the premade HTML structure in how it was set up.

</br>

- **Low Contrast on certian elements**

  <img width="400" src="./readme-images/testing/accessability/low-contrast.webp" alt="low contrast">

  There were a handful of elements on the website flagged as low contrast. Some of these were due to the default settings of Tailwind, such as the placeholder text of inputs, and I left them as they were because changing them would compromise the intended visual design. I made changes to some visual elements of the site where necessary, ensuring they did not compromise the integrity and consistency of the theming and overall design choices.

## Lighthouse Testing

When testing initially, my performance scores needed improvement. One main issue was Cumulative Layout Shift (CLS). This was caused by not having explicit widths and heights on my img elements, which caused some jumping around of content on initial page loads. Adding the width and height attributes helped mitigate this issue.

Another thing I did was ensure that my images were all compressed and saved as webp images to make serving them as efficient as possible and reduce download speeds.

After making these changes, another issue impacting the performance metric was the Time to First Byte (TTFB), which is a measurement used as an indication of the responsiveness of a web server or other network resource. This could possibly be an issue with Heroku or possibly AWS. Nonetheless, having tested the website across multiple devices and on 3G wireless connection speeds, I found the performance to be perfectly acceptable.

### Homepage

- Desktop
  <img src="./readme-images/testing/lighthouse/homepage-desktop.webp" alt="Homepage Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/homepage-mobile.webp" alt="Homepage Mobile">

### Products List Page

- Desktop
  <img src="./readme-images/testing/lighthouse/products-list-desktop.webp" alt="Products List Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/products-list-mobile.webp" alt="Products List Mobile">

### Product Detail Page

- Desktop
  <img src="./readme-images/testing/lighthouse/product-detail-desktop.webp" alt="Product Detail Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/product-detail-mobile.webp" alt="Product Detail Mobile">

### Shopping Cart Page

- Desktop
  <img src="./readme-images/testing/lighthouse/cart-desktop.webp" alt="Shopping Cart Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/cart-mobile.webp" alt="Shopping Cart Page Mobile">

### Checkout Page

- Desktop
  <img src="./readme-images/testing/lighthouse/checkout-desktop.webp" alt="Checkout Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/checkout-mobile.webp" alt="Checkout Page Mobile">

### Order Confirmation Page

- Desktop
  <img src="./readme-images/testing/lighthouse/order-confirmation-desktop.webp" alt="Order Confirmation Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/order-confirmation-mobile.webp" alt="Order Confirmation Page Mobile">

### Profile Page

- Desktop
  <img src="./readme-images/testing/lighthouse/profile-desktop.webp" alt="Profile Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/profile-mobile.webp" alt="Profile Page Mobile">

### Wishlist Page

- Desktop
  <img src="./readme-images/testing/lighthouse/wishlist-desktop.webp" alt="Wishlist Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/wishlist-mobile.webp" alt="Wishlist Page Mobile">

### Product Admin Page

- Desktop
  <img src="./readme-images/testing/lighthouse/product-admin-desktop.webp" alt="Product Admin Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/product-admin-mobile.webp" alt="Product Admin Page Mobile">

### 404 Page

- Desktop
  <img src="./readme-images/testing/lighthouse/404-page-desktop.webp" alt="404 Page Desktop">

- Mobile
  <img src="./readme-images/testing/lighthouse/404-page-mobile.webp" alt="404 Page Mobile">

## Device Testing

#### Devices

These are the different devices I have tested my site on after deployment.
| Device | iPhone SE | iPhone X | iPhone 12 Pro | iPhone 13 Pro Max | iPhone 14 Pro Max | iPad | iPad Air | iPad Pro | Macbook Pro M1 |
| ------------------ | ----------- | ----------- | ------------- | ----------------- | ----------------- | ------------ | ------------ | ------------- | -------------- |
| **Resolution** | **375x667** | **375x812** | **390x844** | **414x76** | **414x896** | **768x1024** | **820x1180** | **1024x1366** | **1440x900** |
| Render | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Layout | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Functionality | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Links | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Images | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| Portrait/Landscape | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |

#### Browsers

These are the different browsers I have tested my site on after deployment.

- Google Chrome
- Firefox
- Safari
- Samsung Internet

#### Responsiveness

- Responsiveness testing was performed using Chrome Developer Tools and [ResponsivelyApp](https://responsively.app/).

- Comprehensive testing of the website was carried out across various emulated devices including mobiles, tablets, and large-format screens, in both portrait and landscape modes.

### Homepage

<img src="./readme-images/testing/responsivness/1-homepage.webp" alt="Homepage top">
<img src="./readme-images/testing/responsivness/2-homepage.webp" alt="Homepage middle">
<img src="./readme-images/testing/responsivness/3-homepage.webp" alt="Homepage bottom">

### Registration Page

<img src="./readme-images/testing/responsivness/registration.webp" alt="Signup modal">

### Login Page

<img src="./readme-images/testing/responsivness/login.webp" alt="Login modal">

### Product Detail Page

<img src="./readme-images/testing/responsivness/1-product-detail.webp" alt="Product detail page">
<img src="./readme-images/testing/responsivness/2-product-detail.webp" alt="Product detail page">

### Products list Page

<img src="./readme-images/testing/responsivness/1-products-list.webp" alt="Products list page">
<img src="./readme-images/testing/responsivness/2-products-list.webp" alt="Products list page">
<img src="./readme-images/testing/responsivness/3-products-list.webp" alt="Products list page">

### Shopping Cart Page

<img src="./readme-images/testing/responsivness/1-shopping-cart.webp" alt="Shopping cart page">
<img src="./readme-images/testing/responsivness/2-shopping-cart.webp" alt="Shopping cart page">

### Checkout Page

<img src="./readme-images/testing/responsivness/1-checkout.webp" alt="Checkout page">
<img src="./readme-images/testing/responsivness/2-checkout.webp" alt="Checkout page">

### Order Confirmation Page

<img src="./readme-images/testing/responsivness/order-confirmation.webp" alt="Order confirmation page">

### Profile Page

<img src="./readme-images/testing/responsivness/1-profile.webp" alt="profile page">
<img src="./readme-images/testing/responsivness/2-profile.webp" alt="profile page">

### Wishlist Page

<img src="./readme-images/testing/responsivness/1-wishlist.webp" alt="Wishlist page">
<img src="./readme-images/testing/responsivness/2-wishlist.webp" alt="Wishlist page">

### Product Admin Page

<img src="./readme-images/testing/responsivness/1-product-admin.webp" alt="Product admin page">
<img src="./readme-images/testing/responsivness/2-product-admin.webp" alt="Product admin page">

### 404 Page

<img src="./readme-images/testing/responsivness/404-page.webp" alt="404 page">

## Manual testing

#### User Stories Testing

`Site Owner Goals`
| User Goals | How are they achieved? |
| --- | --- |
| 1. As the **site owner**, I want to have an admin account that gives me special privileges for managing store inventory. | The site owner has a superuser account that allows them access to the admin panel provided by Django. In addition, they also have access to full CRUD functionality within the app for managing inventory when they log in as an admin with superuser privileges. |
| 2. As the **site owner**, I want to be able to add new products to the database to update the store's inventory. | From the Django admin panel, the site owner can add a product to the store, or do it within the product admin section of the app if they are logged in as an administrator. |
| 3. As the **site owner**, I want to be able to increase the stock levels of an existing item if its stock is low or about to be sold out. | From the Django admin panel, the site owner can increase the stock levels of a product in the store, or do it within the product admin app if they are logged in as an administrator. |
| 4. As the **site owner**, I want to be able to update the information of an existing product, if for example I need to change its sale price or apply a sale discount to it. | From the Django admin panel, the site owner can change any detail of a product in the store or do so by clicking an edit icon on the product when they are logged in as an administrator. |
| 5. As the **site owner**, I want to be able to remove an existing product, if for example it is discontinued and I no longer want to sell it. | From the Django admin panel, the site owner can delete a product from the store or do so by clicking a delete icon on the product and confirming their action when they are logged in as an administrator. |
| 6. As the **site owner**, I want to have a newsletter section encouraging users to provide their emails for marketing purposes. | There is a call-to-action section on the homepage enticing users to sign up for the newsletter. When users enter their emails, Mailchimp is used to manage the subscription of users for the newsletter. |
| 7. As the **site owner**, I want users to be aware of how much they need to spend to qualify for free shipping so that they are motivated to spend a little more. | There is a notification banner on the products list page informing users that if they spend over €50, they will qualify for free shipping. Additionally, they will also be notified of how much more they need to spend on the shopping cart page if they are below the free delivery threshold. |
| 8. As the **site owner**, I want to show related products next to a shoe a user is viewing so that they are encouraged to further browse the products for sale and remain on the store for a long period. | On the product detail page, a randomly selected shoe from a matching brand will be shown to the user on wider desktop screens, which, when clicked, will take them to the corresponding product detail page for that item. |
| 9. As the **site owner**, I want the website design to have a modern look and be aesthetically pleasing and professional to make a good impression on visitors. | The website uses a modern, responsive design with a clean layout, attractive fonts, and high-quality images to create a professional and visually appealing appearance that fits the brand and appeals to the target demographic. |
| 10. As the **site owner**, I want to have a section showing links to the various social media channels associated with the brand. | A footer section is included on the website with icons and links to the brand's social media profiles on platforms like Facebook, Twitter, and Instagram. (Note that these links only take the user to the homepage for each social media platform respectively, as this is a fictional business. The Facebook link shows a screenshot of the create business Facebook page.) |
| 11. As the **site owner**, I want to have a section showing legal copyright information along with the privacy policy for the business. | The footer of the website includes legal information such as copyright notices and the business privacy policy. |

</br>

`User Goals`
| User Goals | How are they achieved? |
| :----------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. As a **user**, I want to be able to easily register with a unique username and password to create an account. | By clicking on the register button in the navigation, an interactive modal will be displayed allowing the user to register for an account with a username and password. |
| 2. As a **user**, I want to be able to easily log in to the site with my username and password to view my account. | By clicking on the login button in the navigation, an interactive modal will be displayed allowing the user to log in using their username and password as credentials. |
| 3. As a **user**, I want to persist my login session for a longer period of time by clicking a "remember me" box. | Clicking on the remember me checkbox on the login form will set the cookie duration for two weeks, prolonging the time for the login session between client and server. |
| 4. As a **user**, I want to be able to easily sign out of the site to keep my account secure. | Clicking on the logout button in the navigation will securely log the user out of their account, and a notification will inform them of successful logout. |
| 5. As a **user**, I want to receive notifications as feedback confirmation for important actions I perform on the site, including registration, login, logout, and any updates or deletions of store products. | When the user performs any of these actions from within the app, a toast notification popup will notify them with the appropriate message. Users can close this popup through an interactive close icon. |
| 6. As a **user**, I want to have a profile section so that I can save and edit my delivery information for future purchases. | When users successfully register for an account and log in to the site, they can access a profile section from the navigation bar. Here they can enter and save their information. |
| 7. As a **user**, I want to be able to keep track of my order history so that I can check my previous orders at a later time if I need to. | All order history is accessible through the user's profile section. Each order in their history will be shown with a summary of information, and clicking the order number will take the user to the full order detail page. |
| 8. As a **user**, I want to be able to see at a glance some of the latest shoe releases in season. | The latest shoes added to the store will be featured prominently on the main homepage just below the hero image. Here users can quickly see at a glance what some of the new store products are for sale. |
| 9. As a **user**, I want to be able to see at a glance items in the store that are on sale so that I could potentially find and get a good deal. | The sale section is also featured prominently on the main homepage and is just below the newsletter section. Here users can quickly see at a glance a selection of shoes that are currently on sale in the store. If the user refreshes the page, this section will be populated by a freshly chosen selection of sale items for variety. |
| 10. As a **user** who is potentially a brand loyalist, I want to be able to see at a glance the types of brands that are on offer without having to browse through different items in the store. | There is a section featured on the homepage just before the footer that outlines some of the brands that the store offers at a glance. |
| 11. As a **user**, I want to be able to search for shoes only for my gender. | Shoes are divided among three separate departments in the store: one for men, women, and kids respectively. The user can access the products for a given department through the navigation menu. |
| 12. As a **user**, I want to be able to filter shoes by different types (sneakers, trainers, high tops, boots, slides). | On the products list page, there is a menu allowing the user to select which specific shoe type they would like to filter from in the store catalog. |
| 13. As a **user**, I want to be able to search for shoes based on a descriptive keyword like a brand name. | There is a search bar on the product list page that allows the user to type in a descriptive keyword like a brand name, and then have the results filtered and returned for them. |
| 14. As a **user**, I want to be able to sort by price and name in both ascending and descending order to ease my browsing experience. | There is a dropdown box that when clicked allows the user to sort by name alphabetically or rating score in either ascending or descending order. |
| 15. As a **user**, I want to avoid excessive scrolling when looking through the different store products by having a pagination component to organize them. | A pagination component is used on the products list page to limit the number of shoes displayed from the catalog at any one time. Users can cycle through the list using the pagination buttons at the bottom of the page just above the footer. |
| 16. As a **user**, I want to add shoes I would like to buy at a future date to my wishlist with the click of an icon so I can keep track of them in a central location. | Clicking the heart icon next to the corresponding shoe in the product list page will trigger an AJAX request to the server to dynamically update the user's wishlist page and also change the heart icon to indicate that it has been added to the user. This is all done without triggering a page refresh. |
| 17. As a **user**, I want to see reviews other customers have written on a shoe to help inform my purchasing decision. | Users can see reviews of a particular shoe just below the product detail section for that shoe if there are any written. |
| 18. As a **user**, I want to write my own review and rate a shoe I have purchased to share my opinion and give feedback. | If users have an account and are signed in, then they will have access to a form allowing them to submit their own review along with a rating in the range of 1 to 5. |
| 19. As a **user**, I want to see if a product is on sale and how much I could save on my purchase. | If a product is on sale, then there will be a percentage off shown next to the list price of the particular shoe along with the updated current price with the percentage discount applied so the user can see exactly how much they are saving. |
| 21. As a **user**, I want to be able to see my cart content before checkout and make adjustments to it before I go to the checkout page. | Users can see a summary of their cart in the cart section of the application. The list of cart items is shown along with the total and any delivery costs if applicable. |
| 22. As a **user**, I want the store to remember my delivery details and add them to my profile if I have not already done so for future purchases. | Users can add their address to the profile page and the checkout form will be populated with their data for any subsequent future purchases. In addition, if the user makes a purchase, then info in the checkout form will be used to update the user's details. |
| 23. As a **user**, I want to see delivery confirmation after a successful purchase has been made so that I see a summary of all my order details. | If a payment is successful, then the user will be taken to an order confirmation page where they can see a detailed summary of their order. |
| 24. As a **user**, I want to be able to check back on my previous order history so that I can see previous orders that I have made with the store. | All order details will be stored in the user's order history section of their profile page. Clicking on the order number for each order will take the user to the order's corresponding detail page for them to view. |

---

<br/>

#### Feature Testing

<br/>

`Navigation Bar`

Desktop
<img src="./readme-images/features/navigation-desktop.webp" alt="navigation bar on desktop">
Tablet
<img src="./readme-images/features/navigation-tablet.webp" alt="navigation bar on tablet">
Hamburger
<img src="./readme-images/features/navber-hamburger.webp" alt="navigation bar on mobile">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------------------------------------------------- | --------- |
| Navbar | Navbar is visible on all pages of the website | Load all website pages | All navbar is shown on all pages | Pass ✅ |
| Navbar | Navbar left menu and right menu are displayed to the user | Load website | All navbar elements are shown | Pass ✅ |
| Navbar | The left and right menu switch to column layout on smaller screen sizes | Resize viewport | Left and right menus correctly switch layout to column | Pass ✅ |
| Navbar | The navbar reflects the logged-in state appropriately | Log into the site | Navbar updates to show the "Profile" link, "Wishlist" link, and logout link | Pass ✅ |
| Navbar | The navbar shows the link for the product admin section if logged in as a store admin | Log into the site as admin | Navbar updates to show the "Product admin" link | Pass ✅ |
| Navbar Logo | Clicking the logo image directs the user to the homepage | Click logo image | User is taken to homepage | Pass ✅ |
| Men's department menu link | Clicking the men's department link takes the user to the products list page for men's shoes | Click the men's department link | User is taken to the men's shoe product list section | Pass ✅ |
| Women's department menu link | Clicking the women's department link takes the user to the products list page for women's shoes | Click the women's department link | User is taken to the women's shoe product list section | Pass ✅ |
| Kids' department menu link | Clicking the kids' department link takes the user to the products list page for kids' shoes | Click the kids' department link | User is taken to the kids' shoe product list section | Pass ✅ |
| Register menu link | Clicking register link opens a popup modal for the registration form | Click register link | Registration modal form is correctly shown to the user | Pass ✅ |
| Login menu link | Clicking login link opens a popup modal for the login form | Click login link | Login modal form is correctly shown to the user | Pass ✅ |
| Cart menu link | Clicking the cart menu link takes the user to their shopping cart page | Click cart link | User is correctly taken to their shopping cart page | Pass ✅ |
| Cart menu link | Adding an item to the cart causes the cart total to be updated | Add item to cart | Cart total is correctly updated to reflect the total in the shopping cart | Pass ✅ |
| Profile menu link | Clicking the profile menu link takes the user to their profile page | Click profile menu link | User is correctly taken to their profile page | Pass ✅ |
| Wishlist menu link | Clicking the wishlist menu link takes the user to their wishlist page | Click wishlist menu link | User is correctly taken to their wishlist page | Pass ✅ |
| Admin link | Clicking the admin menu link takes the user to their product admin page | Click admin menu link | User is correctly taken to their product admin page | Pass ✅ |
| Signout link | Clicking the signout menu link signs the user out of their account | Click signout link | User is successfully signed out of their account | Pass ✅ |

<br />

`Mobile Navigation`
<img src="./readme-images/features//mobile-menu.webp" alt="mobile navigation">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------- | -------------------------------------------------------------------------------- | --------- |
| Hamburger Icon | Clicking on the hamburger icon opens the mobile navigation | Click on hamburger icon | Mobile nav appears as intended | Pass ✅ |
| Close Icon | Clicking on the close icon in the top right closes the mobile nav | Click on close icon | Mobile nav closes as intended | Pass ✅ |
| Esc Key | Pressing the Esc key closes the mobile nav when it's already open | Press Esc key | Mobile nav closes as intended | Pass ✅ |
| Fleetfoot title | Clicking on Fleetfoot title takes the user back to the homepage | Click on Fleetfoot title | User is taken back to the homepage | Pass ✅ |
| Bottom Image | When loading the mobile navigation, the bottom image is displayed to the user | Open mobile navigation | Image is shown to the user | Pass ✅ |
| Fleetfoot title | Clicking on Fleetfoot title takes the user back to the homepage | Click on Fleetfoot title | User is taken back to the homepage | Pass ✅ |
| Navbar | The mobile navigation reflects the logged-in state appropriately | Log into the site | Navbar menu updates to show the "Profile" link, "Wishlist" link, and logout link | Pass ✅ |
| Navbar | The mobile navigation shows the link for the product admin section if logged in as a store admin | Log into the site as admin | Navbar updates to show the "Product admin" link | Pass ✅ |
| Fleetfoot title | Clicking on Fleetfoot title takes the user back to the homepage | Click on Fleetfoot title | User is taken back to the homepage | Pass ✅ |
| Men's department menu link | Clicking the men's department link takes the user to the products list page for men's shoes | Click the men's department link | User is taken to the men's shoe product list section | Pass ✅ |
| Women's department menu link | Clicking the women's department link takes the user to the products list page for women's shoes | Click the women's department link | User is taken to the women's shoe product list section | Pass ✅ |
| Kids' department menu link | Clicking the kids' department link takes the user to the products list page for kids' shoes | Click the kids' department link | User is taken to the kids' shoe product list section | Pass ✅ |
| Register menu link | Clicking register link opens a popup modal for the registration form | Click register link | Registration modal form is correctly shown to the user | Pass ✅ |
| Login menu link | Clicking login link opens a popup modal for the login form | Click login link | Login modal form is correctly shown to the user | Pass ✅ |
| Cart menu link | Clicking the cart menu link takes the user to their shopping cart page | Click cart link | User is correctly taken to their shopping cart page | Pass ✅ |
| Cart menu link | Adding an item to the cart causes the cart total to be updated | Add item to cart | Cart total is correctly updated to reflect the total in the shopping cart | Pass ✅ |
| Profile menu link | Clicking the profile menu link takes the user to their profile page | Click profile menu link | User is correctly taken to their profile page | Pass ✅ |
| Wishlist menu link | Clicking the wishlist menu link takes the user to their wishlist page | Click wishlist menu link | User is correctly taken to their wishlist page | Pass ✅ |
| Admin link | Clicking the admin menu link takes the user to their product admin page | Click admin menu link | User is correctly taken to their product admin page | Pass ✅ |
| Signout link | Clicking the signout menu link signs the user out of their account | Click signout link | User is successfully signed out of their account | Pass ✅ |

<br />

`Hero Section`
<img src="./readme-images/features/hero-section.webp" alt="hero section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ------------------------ | --------------------------------------------------------------------------- | ---------------------- | --------------------------------------------- | --------- |
| Hero Section Background | Background image is displayed to the user | Load page | Background image is displayed to the user | Pass ✅ |
| Hero Section Background | Background image covers and remains centered over all section widths | Window resize | Background image remains centered and covers all widths | Pass ✅ |
| Hero Section Arrow icon | Arrow icon is shown only for larger screens | Window resize to large width | Arrow icon is visible to the user | Pass ✅ |
| Hero Section Arrow icon | Clicking the arrow icon directs the user to the latest products section below the hero image | Click arrow icon | Arrow icon scrolls user to the latest products section | Pass ✅ |

<br />

`Product Card`
<img src="./readme-images/features/product-card.webp" alt="product card">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-----------------------|----------------------------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------|-----------|
| Product card | Product card loads with the data of its product instance | Load product cards | Product cards all render with their respective product information | Pass ✅ |
| Product image | Product image is shown for each shoe | Load product card | Individual product image is shown for each shoe | Pass ✅ |
| Product image | Clicking the product image takes the user to its corresponding product detail page | Click product card image | User is taken to the product detail page | Pass ✅ |
| Product department | Correct department for the shoe is shown | Load product card | Correct department is shown | Pass ✅ |
| Product title | Correct product name for the shoe is shown | Load product card | Correct product name is shown | Pass ✅ |
| Price icon | Price icon for the price section is shown | Load product card | Price icon is shown | Pass ✅ |
| Sale percentage | If product is on sale, then a sale percentage box will be shown next to the list price | Load product card for product on sale | Sale percentage box is shown | Pass ✅ |
| Updated sale price | If product is on sale, then the updated sale price will be calculated and shown | Load product card for product on sale | Updated sale price is shown | Pass ✅ |
| Product Card Wishlist Icon | If a regular user is logged in, then a heart wishlist icon will be displayed to the user | Login as regular user | Wishlist heart icon is shown | Pass ✅ |
| Product Card Wishlist Icon | Clicking the wishlist icon adds the corresponding product as an item to the user's wishlist without triggering a page refresh | Click wishlist icon | Item is correctly added to user's wishlist without a page refresh | Pass ✅ |
| Product Card Wishlist Icon | If shoe is not already part of the user's wishlist, then the heart will change to a solid version to reflect it being added to the wishlist | Click wishlist icon | Solid heart icon is shown to reflect product has been added to their wishlist | Pass ✅ |
| Product Card Wishlist Icon | If shoe is already part of the user's wishlist, then the heart will change from a solid version to an empty outline version to reflect it has been removed from the user's wishlist | Click wishlist icon | Empty outline heart icon is shown to the user to reflect it has been removed from their wishlist | Pass ✅ |
| Product card edit icon | If admin is logged in, a product edit icon will be shown | Load product card as admin | Product edit icon is shown | Pass ✅ |
| Product card edit icon | If product edit icon is clicked, then admin will be taken to the update product page | Click product edit icon | Admin is taken to the update product page | Pass ✅ |
| Product card delete icon | If admin is logged in, a product delete icon will be shown | Load product card as admin | Product delete icon is shown | Pass ✅ |
| Product delete icon | When product delete icon is clicked, then delete confirmation popup will appear | Click product delete icon | Delete confirmation popup appears | Pass ✅ |

<br />

`Latest Shoes Section`
<img src="./readme-images/features/latest-shoe-section.webp" alt="latest shoes section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-----------------------|--------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------|-----------|
| Latest Shoes Section | When the user visits the homepage, the four most recent shoes are shown to the user | Load website homepage | The four most recent shoes added to the database are retrieved and shown to the user | Pass ✅ |
| Latest Shoes Section | Section is fully responsive for multiple screen sizes | Resize viewport | Section adapts to different screen sizes | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |

<br />

`Newsletter CTA Section`
<img src="./readme-images/features/newsletter-section.webp" alt="newsletter section">
<img src="./readme-images/features/newsletter-mobile.webp" alt="newsletter mobile">
<img src="./readme-images/features/newsletter-success.png" alt="newsletter success">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------- | --------- |
| Newsletter Section | Section is fully responsive for different widths | Resize viewport | Section is fully responsive for multiple screen sizes | Pass ✅ |
| Newsletter Image | Newsletter image is shown to the user | Load homepage | Newsletter image is displayed | Pass ✅ |
| Newsletter form | Entering an email correctly adds a user to the subscription list via Mailchimp | Enter email | User is added to the subscription list | Pass ✅ |
| Newsletter form | Not entering a valid email prompts the user for an email and prevents submission | Enter incorrect input | User is prompted to enter a valid email and submission is prevented | Pass ✅ |
| Newsletter form success message | Entering a valid email shows a success message to the user | Enter valid email address | Success message is displayed | Pass ✅ |

<br />

`Sale Section`
<img src="./readme-images/features/sale-section.webp" alt="sale section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-----------------------|------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------|-----------|
| Sale Section | When the user visits the homepage, four randomly selected products on sale are shown to the user | Load website homepage | Four randomly selected shoes on sale are retrieved and shown to the user | Pass ✅ |
| Sale Section | Only items on sale are shown in this section | Load website homepage | Only sale items are shown in this section | Pass ✅ |
| Sale Section | Section is fully responsive for mutliple screen sizes | Resize viewport | Section adapts to mutliple screen sizes | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |

<br />

`Brands Section`
<img src="./readme-images/features/brands-section.webp" alt="brands section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------|-----------------------------------------------------------------------------|----------------------|----------------------------------------------- |-----------|
| Brands Section | Brand logos are shown to the user | Load homepage | Brand logos are shown to the user | Pass ✅ |
| Brands Section | Section is fully responsive for mutliple screen sizes | Resize viewport | Section adapts to multiple screen sizes | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |

<br />

`Footer Section`
<img src="./readme-images/features/footer.webp" alt="footer section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------|------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------|-----------|
| Footer Section | Post card component is fully responsive to multiple screen widths | Resize viewport | Section adapts to multiple screen sizes | Pass ✅ |
| Social media icons | Each icon is rendered to the page | Load page | Social media icons are correctly loaded and displayed to the user | Pass ✅ |
| Facebook icon | Clicking the Facebook icon opens a screenshot of the business Facebook page in another tab | Click icon | Facebook page is opened in another tab and correctly shown to the user | Pass ✅ |
| Instagram icon | Clicking the Instagram icon opens the default homepage of Instagram | Click icon | Instagram homepage is opened in another tab and correctly shown to the user | Pass ✅ |
| Twitter icon | Clicking the Twitter icon opens the default homepage of Twitter | Click icon | Twitter homepage is opened in another tab and correctly shown to the user | Pass ✅ |
| Privacy policy | Clicking the Privacy Policy link opens the privacy policy in another tab | Click Privacy Policy link | Privacy Policy is opened in another tab | Pass ✅ |
| GitHub link | Clicking the GitHub link takes the user to my GitHub profile so that they can see my other projects | Click GitHub link | My GitHub profile is opened in another tab | Pass ✅ |
| GitHub repo link | Clicking the GitHub repo link takes the user to the repository for the Fleetfoot application | Click GitHub repo link | GitHub repository is opened in another tab | Pass ✅ |

<br />

`Products List Section`
<img src="./readme-images/features/product-list-section.webp" alt="products list section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------- |
| Products List Section | Section is fully responsive for multiple screen sizes | Resize viewport | Section adapts to multiple screen sizes | Pass ✅ |
| Hero Image | Hero image at the top of the page is shown when loading product list page | Load products list page | Hero image is shown when loading product list page | Pass ✅ |
| Free Shipping Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |
| Department Title | Title correctly shows the corresponding department for men's, women's, and kids' respectively | Load products list page by clicking men's, women's, and kids' department links from navigation | Correct title is shown to the user | Pass ✅ |
| Shoe Type Menu | Clicking a shoe type filters and displays only shoes of that type to the user | Click shoe type menu item | Shoes of that type are filtered and shown to the user | Pass ✅ |
| Shoe Type Menu | Clicking a shoe type menu item highlights it as active | Click shoe type menu item | Menu item is shown with a black background and white text to signify to the user what shoe types they are currently viewing | Pass ✅ |

<br />

`Products Search Bar`
<img src="./readme-images/features/searchbar.webp" alt="products searchbar">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------------- | --------- |
| Products Search bar | User enters a name of a brand of shoe or its title to filter products by | Enter shoe brand name or title | Shows matching products that are filtered and shown to the user | Pass ✅ |
| Products Search bar | Popup is shown to the user requesting a valid search query when an empty search query is entered | Submit an empty search query | Popup is displayed informing the user to enter a valid search query | Pass ✅ |
| Products Search button | Clicking the search button submits the search query | Click search button | Search query is correctly submitted | Pass ✅ |
| Products Search button | Hovering on the search button changes the background color | Hover on search button | Background color correctly changes | Pass ✅ |

<br />

`Products Sorting Dropdown`
<img src="./readme-images/features/dropdown-filter.webp" alt="sorting dropdown">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------- | --------- |
| Sorting Dropdown | Clicking the drop down for value: Name (A-Z) sorts products by name in ascending alphabetical order | Click value: Name (A-Z) | Products are correctly sorted by name in ascending alphabetical order | Pass ✅ |
| Sorting Dropdown | Clicking the drop down for value: Name (Z-A) sorts products by name in descending alphabetical order | Click value: Name (Z-A) | Products are correctly sorted by name in descending alphabetical order | Pass ✅ |
| Sorting Dropdown | Clicking the drop down for value: Price (low - high) sorts products by price in ascending order | Click value: Price (low - high) | Products are correctly sorted by price in ascending order | Pass ✅ |
| Sorting Dropdown | Clicking the drop down for value: Price (high - low) sorts products by price in descending order | Click value: Price (high - low) | Products are correctly sorted by price in descending order | Pass ✅ |
| Sorting Dropdown | Background color changes on hover | Hover over dropdown | Background color correctly changes | Pass ✅ |

<br />

`Pagination`
<img src="./readme-images/features/pagination.webp" alt="pagination">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ----------------- | --------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------------------- | --------- |
| Pagination | Maximum of nine shoes are rendered at any one time | Load articles list page | A max of nine shoes are shown to the user | Pass ✅ |
| Pagination number | When clicked, the user is shown the slice of products for that numbered section | Click the pagination number | Slice of products for that numbered section is shown to the user | Pass ✅ |
| First Button | On the first pagination cycle, the first button is not shown | Navigate to the first pagination cycle | First button is not shown | Pass ✅ |
| First Button | Clicking the first button takes the user back to the first page of the pagination | Click the first button | User is taken back to the first page of the pagination | Pass ✅ |
| Next Button arrow | Clicking the next button moves to the next set of products | Click the next button | Next set of products is shown to the viewer | Pass ✅ |
| Prev Button arrow | Clicking the prev button moves back to the previous set of products | Click the prev button | Previous set of products is shown to the viewer | Pass ✅ |
| Last Button | On the last pagination cycle, the last button is not shown | Navigate to the last pagination cycle | Last button is not shown | Pass ✅ |
| Last Button | Clicking the last button advances to the last set of products | Click the last button | Last set of products is shown to the viewer | Pass ✅ |

<br />

`Login Modal`
<img src="./readme-images/features/login-modal.webp" alt="login modal">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| -------------------- | ------------------------------------------------------------------------------------------ | --------------------------- | ---------------------------------------------------------------------- | --------- |
| Login Modal | Section is fully responsive for multiple screen sizes | Resize viewport | Section adapts to multiple screen sizes | Pass ✅ |
| Login Modal Image | Image is loaded and displayed to the user | Open modal | Image is correctly displayed to the user | Pass ✅ |
| Close icon | Clicking the close icon closes the modal | Click close icon | Login modal is correctly closed | Pass ✅ |
| Esc key | Pressing the Esc key closes the modal | Press Esc key | Login modal is correctly closed | Pass ✅ |
| Login form | All correct inputs are displayed on the form | Show form | All correct input fields for the form are displayed to the user | Pass ✅ |
| Login form | Entering incorrect credentials prevents user login and displays an error message popup | Enter incorrect credentials | User is prevented from logging in and error popup message is displayed | Pass ✅ |
| Remember me checkbox | Clicking the remember me checkbox sets the session expiry to 14 days to persist user login | Click checkbox | Session expiry is correctly set to 14 days on successful login | Pass ✅ |
| Form submit | The form submit button at the bottom of the form correctly submits the form | Click form submit button | Form is correctly submitted | Pass ✅ |
| Create account link | Clicking the create account link opens the registration modal | Click create account link | Registration modal is correctly opened | Pass ✅ |

<br />

`Registration Modal`
<img src="./readme-images/features/registration-modal.webp" alt="registration modal">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ------------------------ | --------------------------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------- | --------- |
| Registration Modal | Section is fully responsive for multiple screen sizes | Resize viewport | Section adapts to multiple screen sizes | Pass ✅ |
| Registration Modal Image | Image is loaded and displayed to the user | Open modal | Image is correctly displayed to the user | Pass ✅ |
| Close icon | Clicking the close icon closes the modal | Click close icon | Registration modal is correctly closed | Pass ✅ |
| Esc key | Pressing the Esc key closes the modal | Press Esc key | Registration modal is correctly closed | Pass ✅ |
| Registration form | All correct inputs are displayed on the form | Show form | All correct input fields for the form are displayed to the user | Pass ✅ |
| Registration form | Entering incorrect credentials prevents user registration and displays an error message popup | Enter incorrect credentials | User is prevented from registering and error popup message is displayed | Pass ✅ |
| Registration form | User password and password confirmation do not match | Enter mismatching passwords | User is prevented from registering and error popup message is displayed | Pass ✅ |
| Remember me checkbox | Clicking the remember me checkbox sets the session expiry to 14 days to persist user login | Click checkbox | Session expiry is correctly set to 14 days on successful login | Pass ✅ |
| Form submit | The form submit button at the bottom of the form correctly submits the form | Click form submit button | Form is correctly submitted | Pass ✅ |
| Login link | Clicking the login link opens the login modal | Click login link | Login modal is correctly opened | Pass ✅ |

<br />

`Product Detail Section`
<img src="./readme-images/features/product-detail.webp" alt="product detail section">
<img src="./readme-images/features/product-detail-mobile.webp" alt="product detail section on mobile">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------------------|--------------------------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------|-----------|
| Product Detail Section | Section is fully responsive for multiple screen sizes | Resize viewport | Section adapts to multiple screen sizes | Pass ✅ |
| Product Detail Information | Department, product title, and description text are correctly shown for the corresponding shoe | Load product detail page | Correct product details are shown | Pass ✅ |
| Product Detail Information | Department, product title, description text, shoe image, rating, and available sizes are correctly shown for the corresponding shoe | Load product detail page | All correct details belonging to this particular shoe are shown to the user | Pass ✅ |
| Detail Section Arrow icon | Clicking the arrow icon directs the user to the reviews section below the product detail section | Click arrow icon | Arrow icon scrolls user to the reviews section | Pass ✅ |

<br />

`Related Product Component`
<img src="./readme-images/features/related-product.webp" alt="related product component">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | -------------------------------------------------------------- | --------- |
| Related Product Component | Related product is made visible for larger screen sizes | Resize viewport to desktop width | Related Product Component is correctly shown to the user | Pass ✅ |
| Related Product Component | A product from the same brand as the one featured in the product detail section is randomly selected to show to the user | Load product detail page | Related product from the same brand is shown to the user | Pass ✅ |
| Related Product title | The title of the related product is correctly shown | Load product detail page | The title of the related shoe is correctly shown | Pass ✅ |
| Related Product image | The image of the related product is correctly shown | Load product detail page | The image of the related shoe is correctly shown | Pass ✅ |
| Related Product image | Clicking the product image takes the user to the product detail page for that shoe | Click related product image | User is taken to the correct product detail page for that shoe | Pass ✅ |

</br>

`Product Showcase Image`
<img src="./readme-images/features/showcase-image.webp" alt="product showcase image">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ----------------- | ------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------- | --------- |
| Showcase image | Showcase image is correctly shown to the user on page load | Load product detail page | Showcase image for that particular shoe is correctly shown to the user | Pass ✅ |
| Showcase image | Showcase image responds to changes in viewport width | Resize viewport | Showcase image correctly resizes | Pass ✅ |
| Background circle | Background circle is correctly shown to the user on page load | Load product detail page | Background circle is correctly shown to the user | Pass ✅ |
| Shadow image | Shadow image is correctly shown to the user on page load | Load product detail page | Shadow image is correctly shown to the user | Pass ✅ |

</br>

`Average Product Rating`
<img src="./readme-images/features/average-rating.webp" alt="average product rating">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------------|-----------|
| Average Product Rating | Average rating component is displayed to the user when product detail page is loaded | Load product detail page | Average rating component is correctly shown to the user | Pass ✅ |
| Average Product Rating | If no reviews and ratings have been assigned to a shoe, then five empty stars with a score of 0 will be rendered | Check average rating component with no reviews | Five empty stars with a score of 0 are correctly shown | Pass ✅ |
| Average Product Rating | Rating score and stars will change to reflect the aggregate of the average of all scores for that shoe based on reviews | Submit several reviews of different ratings to check calculation | Rating score and stars correctly reflect the aggregate average of all scores | Pass ✅ |

</br>

`Available Sizes Chart`
<img src="./readme-images/features/avaliable-sizes.webp" alt="Available sizes component">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------|
| Available Sizes Chart | Available Sizes Chart is displayed to the user when product detail page is loaded | Load product detail page | Available Sizes Chart is correctly shown to the user | Pass ✅ |
| Available Sizes Chart | Only the sizes currently in stock for a given shoe and size are displayed for the user to purchase | Load product detail page and check product stock for sizes in the database to ensure only available sizes are shown | Only available sizes for the shoe with a stock quantity greater than 0 are shown to the user | Pass ✅ |
| Size | Hovering over a size changes the background | Hover over size | Background color correctly changes | Pass ✅ |
| Size | Clicking a size sets it to a highlighted active state | Click size | Clicked size is set to highlighted active state | Pass ✅ |
| Size | Clicking a size removes the disabled state on the add to cart button | Click size | Disabled state is correctly removed on the add to cart button | Pass ✅ |

</br>

`Add To Cart Button`
<img src="./readme-images/features/add-to-cart-inactive.webp" alt="add to cart button inactive">
<img src="./readme-images/features/add-to-cart-active.webp" alt="add to cart button active">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------|-----------|
| Add To Cart Button | Add To Cart Button is displayed to the user when product detail page is loaded | Load product detail page | Add To Cart Button is correctly shown to the user | Pass ✅ |
| Add To Cart Button | When the product detail page is initially loaded, the button will be in a disabled state | Load product detail page | Button is correctly in a disabled state by default | Pass ✅ |
| Add To Cart Button | Clicking a size removes the disabled state on the add to cart button | Click size | Disabled state is correctly removed on the add to cart button | Pass ✅ |
| Increment button | Clicking the increment button increases the quantity of the item in the cart | Click increment button | Quantity of item is correctly incremented | Pass ✅ |
| Decrement button | Clicking the decrement button decreases the quantity of the item in the cart | Click decrement button | Quantity of item is correctly decremented | Pass ✅ |
| Decrement button | Clicking the decrement button when quantity is one will prevent the quantity from being lowered further | Click decrement button when quantity is one | Quantity of item is prevented from going below one | Pass ✅ |
| Add To Cart Button | When a size and a quantity have been set, then clicking the button adds the item and quantity to the user's cart | Click button with size and quantity chosen | Correct shoe and quantity are added to the user's cart | Pass ✅ |
| Notification | When an item has been added to a user's cart, a popup notification will be displayed to the user showing them the name of the product and a view cart button | Add product to shopping cart | Popup notification is correctly displayed to the user | Pass ✅ |
| Notification view cart button | When the user clicks the view cart button on the notification popup, they will be taken to their shopping cart | Click the view cart button | User is correctly taken to their shopping cart page | Pass ✅ |

</br>

`Product Review Section`
<img src="./readme-images/features/reviews-section.webp" alt="Customer review section">
<img src="./readme-images/features/reviews-section-empty.webp" alt="Customer review section empty">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------|-----------|
| Review Banner Heading | Banner heading at the top of the review section is correctly rendered and shown to the user | Load product detail page | Banner heading for review section is shown to the user | Pass ✅ |
| Reviews section | If user is not logged in, then a login message and button will be displayed to the user | Check review section when not logged in | Message and button are correctly displayed to the user | Pass ✅ |
| Login button | Clicking the login button will open the login modal | Click login button | Login modal is correctly shown to the user | Pass ✅ |
| Reviews section | If there are no reviews, then a message stating that there are currently no reviews will be displayed | Check the reviews section for a product with currently no reviews | Message stating no reviews is correctly displayed | Pass ✅ |
| Reviews section | If there are reviews, they are correctly displayed to the user | Check the reviews section for a product with reviews | Reviews are correctly displayed to the user | Pass ✅ |
| Review form | If the user has an account and is logged in, then a review form will be displayed for the user | Log in to an account and check the review section | Form is correctly displayed for the user | Pass ✅ |
| Review form | All correct inputs are displayed on the form | Show form | All correct input fields for the form are displayed to the user | Pass ✅ |
| Review form | When user submits a review, it is correctly displayed in the review section for that corresponding shoe | Submit review | Review is correctly displayed for the corresponding shoe | Pass ✅ |
| Review success notification | When user successfully submits a review, they are given a popup notification as feedback of success | Submit review | Success popup notification is correctly displayed for the user | Pass ✅ |
| Review error notification | If a user enters incorrect details for the review, they will be redirected back to the page and shown an error notification | Submit review with incorrect details | Error popup notification is correctly displayed for the user | Pass ✅ |
| Review | Details such as title, rating, date created, and the review content are all correctly shown to the user for each review | Submit review and check review section | Review is correctly rendered with all correct details | Pass ✅ |
| Review | The review item is fully responsive and readable for smaller screens | Resize viewport | Review is responsive and readable for smaller screens | Pass ✅ |

</br>

`Profile Section`
<img src="./readme-images/features/profile-section.png" alt="Profile section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| Profile Section | Profile Section is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Profile Section | Accessing the profile section when not logged in redirects the user back to the home page | Access page when not logged in | User is correctly redirected back to homepage | Pass ✅ |
| Hero Image | Hero image at the top of the page is shown when loading product list page | Load products list page | Hero image is shown when loading product list page | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |
| Delivery information form | All correct inputs are displayed on the form | Show form | All correct input fields for the form are displayed to the user | Pass ✅ |
| Delivery information form | The correct placeholder text is shown for each field in the form | Check each form field | Form fields all have correct placeholder text | Pass ✅ |
| Delivery information form | Submitting the form redirects the user back to the profile page with the populated fields | Show form with details | Form is rerendered with all fields populated | Pass ✅ |
| Delivery information form | Updating the delivery information on the user's profile automatically populates the checkout delivery information during the checkout process | Fill in delivery details and go to checkout page | Delivery details are correctly populated in the checkout form | Pass ✅ |
| Country field dropdown | The country field contains all valid countries for the profile | Show all valid countries as options | Click country field dropdown | Pass ✅ |
| Submit button | Hovering over submit button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Submit button | Clicking button submits the form | Click button | Form is correctly submitted | Pass ✅ |
| Profile update notification | When a user enters their profile information, they will see a popup notification as feedback | Submit profile information | Notification is correctly displayed to the user | Pass ✅ |
| Order history | If user currently has no order history, they will see a message informing them of no order history | View profile page before placing any orders in the store | Message is correctly shown to the user | Pass ✅ |
| Order history | If the user has an order history, then each order will be shown here in a list | Place an order on the store | Order is correctly saved and appended to the order history list | Pass ✅ |
| Order history item | The corresponding details of the order, order number, date ordered, cart items, and total are displayed for each corresponding order | Place an order on the store and check them on profile page | Order is shown to the user with all of the correct details for that order | Pass ✅ |
| Order history item | Clicking the order number takes the user to the correct corresponding order detail page | Click order number | User is taken to the correct order detail page | Pass ✅ |

</br>

`Wishlist Section`
<img src="./readme-images/features/wishlist-section.webp" alt="Wishlist section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ------- | ------------------------ | ----------------- | ------------------------------------------------- | --------- |
| Wishlist Section | Wishlist Section is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Wishlist Section | Accessing the wishlist section when not logged in redirects the user back to the home page | Access page when not logged in | User is correctly redirected back to homepage | Pass ✅ |
| Hero Image | Hero image at the top of the page is shown when loading product list page | Load products list page | Hero image is shown when loading product list page | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |
| Wishlist Icon | Clicking the wishlist icon adds the corresponding product as an item to the user's wishlist without triggering a page refresh | Click wishlist icon | Item is correctly added to user's wishlist without a page refresh | Pass ✅ |
| Wishlist Icon | If shoe is not already part of the user's wishlist, then the heart will change to a solid version to reflect it being added to the wishlist | Click wishlist icon | Solid heart icon is shown to reflect product has been added to their wishlist | Pass ✅ |
| Wishlist Icon | If shoe is already part of the user's wishlist, then the heart will change from a solid version to an empty outline version to reflect it has been removed from the user's wishlist | Click wishlist icon | Empty outline heart icon is shown to the user to reflect it has been removed from their wishlist | Pass ✅ |

</br>

`Product Admin Section`
<img src="./readme-images/features/admin-add-product.webp" alt="Product admin section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------ | --------- |
| Product Admin Section | Product Admin Section is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Product Admin Section | Accessing the Product Admin if not logged in or without superuser admin privileges redirects the user back to the homepage | Access page when not logged in or not as admin superuser | User is redirected back to the homepage | Pass ✅ |
| Hero Image | Hero image at the top of the page is shown when loading product list page | Load products list page | Hero image is shown when loading product list page | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |
| Form menu | The add product and increase stock count forms are shown in the form menu | Load admin page | Form menu items are correctly displayed to the admin | Pass ✅ |
| Form menu item | Clicking a form menu item highlights it to the admin | Click form menu item | Form menu item is correctly highlighted with a black background and white text | Pass ✅ |
| Form menu item | Clicking a form menu reveals its associated form on the page and hides the other one | Click form menu item | Corresponding form is displayed to the admin and the other is hidden | Pass ✅ |

<br />

`Add Product Form`
<img src="./readme-images/features/admin-add-product.webp" alt="Add product form">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|--------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| Add product form | Form and all correct inputs are displayed to the admin | Load product admin page and select add product form | Add product form is correctly displayed to the user with all correct inputs | Pass ✅ |
| Add product form | The correct placeholder text is shown for each field in the form | Check each form field | Form fields all have correct placeholder text | Pass ✅ |
| Add product form | When user submits form with correct details and passes validation, then a new product is added to the database | Submit form with correct product details and pass validation, then check database for newly added product | A new product is correctly added to the store | Pass ✅ |
| Add product form | If user leaves a required field blank, they will be notified in the form with validation | Submit form with required field left blank | User is correctly notified of the missing required field | Pass ✅ |
| Add product form | When user submits form with incorrect details, they are redirected back to the page with an error notification | Submit form with incorrect product details | User sees an error popup notification message | Pass ✅ |
| Image upload | If user uploads an image, then the image is correctly stored and fetched from an AWS S3 bucket. It will be shown for that product throughout the store | Upload image | Product image is correctly uploaded to AWS S3 for storage and shown in the store for that corresponding product | Pass ✅ |
| On sale checkbox | If user clicks on sale without setting a sale percentage, then they will be directed back to the form and shown an error message | Click on sale without setting a sale percentage | User is redirected back to the form with an error | Pass ✅ |
| Submit button | Hovering over submit button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Submit button | Clicking button submits the form | Click button | Form is correctly submitted | Pass ✅ |
| Add product notification | When a user successfully adds a new product to the database, they will be notified via a success popup message informing them | Successfully add new product to the database | User is correctly notified that a new product has been added | Pass ✅ |

</br>

`Increase Stock Count Form`
<img src="./readme-images/features/admin-update-stock.webp" alt="Increase stock count form">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------------------- | --------------------------------------------------------------------------------------------------------| --------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------- |
| Increase stock count form | Form and all correct inputs are displayed to the admin | Load product admin page and select increase stock count product form | Increase stock count form is correctly displayed to the user with all correct inputs | Pass ✅ |
| Increase stock count form | When user submits form with correct details and passes validation, then a selected product's stock level increases by the amount entered | Submit form and check product stock in the database to verify it has been increased | Product stock is successfully increased by the amount specified | Pass ✅ |
| Increase stock count form | When user submits form with incorrect details, they are redirected back to the page with an error notification | Submit form with incorrect product details | User sees an error popup notification message | Pass ✅ |
| Increase stock count form | If user leaves a required field blank, they will be notified in the form with validation | Submit form with required field left blank | User is correctly notified of the missing required field | Pass ✅ |
| Size dropdown | When the page loads, the size field will be set to a non-selectable disabled state by default | Load the product admin page and select the increase stock form | The size dropdown is correctly set to a disabled state by default | Pass ✅ |
| Product dropdown | When a product is selected for the form, the disabled state of the size field is removed and populated with all valid sizes for that particular shoe | Click the product dropdown | Size field is active and contains only valid sizes for that product | Pass ✅ |
| Submit button | Hovering over submit button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Submit button | Clicking button submits the form | Click button | Form is correctly submitted | Pass ✅ |
| Increase stock count notification | When a user successfully increases the stock count of a product in the database, they will be notified via a success popup message informing them | Successfully increase the stock level of a product in the database | User is correctly notified that the stock for that product has been updated | Pass ✅ |
| Checkout button | Hovering over checkout button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Checkout button | Clicking button sends the user to the checkout | Click button | User is correctly taken to the checkout page | Pass ✅ |
| Keep shopping button | Hovering over keep shopping button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Keep shopping button | Clicking the button takes the user to the homepage | Click button | User is correctly taken to the homepage | Pass ✅ |

</br>

`Update Product Page`
<img src="./readme-images/features/update-product-form.webp" alt="update product form">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| Update Product Page | The Update Product Page is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Update Product Page | Accessing the Update Product Page if not logged in or without superuser admin privileges redirects the user back to the homepage | Access page when not logged in or not as admin superuser | User is redirected back to the homepage | Pass ✅ |
| Edit product icon | When the edit icon is clicked on a product card, the admin is taken to the update product page | Click edit icon | Admin is correctly taken to the update page | Pass ✅ |
| Update product form | The correct placeholder text is shown for each field in the form | Check each form field | Form fields all have correct placeholder text | Pass ✅ |
| Update product form | Form and all correct inputs are displayed to the admin | Load update product form | Update product form is correctly displayed to the user with all correct inputs | Pass ✅ |
| Update product form | When the user is taken to the update page via the edit icon on the product card, the form is prepopulated with the data from that product | Click edit icon for a particular product | Form fields are correctly prepopulated with the data from the corresponding product | Pass ✅ |
| Update product form | When user submits form with correct details and passes validation, then the corresponding product instance is updated in the database | Submit form with correct product details and pass validation, then check database for the newly updated product | An existing product is correctly updated in the store | Pass ✅ |
| Update product form | If user leaves a required field blank, they will be notified in the form with validation | Submit form with required field left blank | User is correctly notified of the missing required field | Pass ✅ |
| Update product form | When user submits form with incorrect details, they are redirected back to the page with an error notification | Submit form with incorrect product details | User sees an error popup notification message | Pass ✅ |
| Image upload | If user uploads an image, then the image will overwrite the current one (if it exists) | Upload image | Product image is correctly uploaded to AWS S3 for storage and overwrites the previous image | Pass ✅ |
| Submit button | Hovering over submit button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Submit button | Clicking button submits the form | Click button | Form is correctly submitted | Pass ✅ |
| Update product notification | When a user successfully updates a product in the database, they will be notified via a success popup message informing them | Successfully update product in the database | User is correctly notified that the product has been updated | Pass ✅ |

</br>

`Shopping Cart Section`
<img src="./readme-images/features/cart-section.webp" alt="Shopping cart section">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|------------------------------- | --------------------------------------------------------------------------------------------------------| ----------------------------------------- | ------------------------------------------------------------------------------------------- | --------- |
| Shopping Cart Section | Shopping Cart Section is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Shopping Cart Section | If there are no items in the user's shopping cart when they visit the page, then an empty shopping cart message and a keep shopping button will be displayed to the user | Visit the shopping cart page with no items in cart | Message and keep shopping button are correctly shown to the user | Pass ✅ |
| Keep shopping button | If the user hovers over the button, it will change background color | Hover over button | Button correctly changes background color | Pass ✅ |
| Keep shopping button | If the user clicks the button, then they are sent to the homepage | Click button | User is correctly sent back to the homepage | Pass ✅ |
| Hero Image | Hero image at the top of the page is shown when loading product list page | Load products list page | Hero image is shown when loading product list page | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |
| Cart Items list | When a shoe of a given size and quantity is added to the cart, the cart item shows up in the list | Add item to cart and check shopping cart page | Cart item is correctly shown to the user | Pass ✅ |
| Cart summary | The user's subtotal, delivery, and grand total are correctly calculated and shown to the user | Add item to cart and check shopping cart summary information | Cart summary is correctly calculated and shown to the user | Pass ✅ |
| Free delivery delta message | If the user's subtotal is less than the free delivery threshold of €50, then a message will appear informing them of how much more they need to spend to qualify for free delivery | Add item to cart worth less than the €50 threshold and check cart summary | Free delivery delta message is correctly shown to the user with the correct delta amount | Pass ✅ |
| Free delivery delta message | If the user's subtotal is more than the free delivery threshold of €50, then the message will not be visible and the delivery fee will be €0.00 | Add item to cart worth more than the €50 threshold and check cart summary | Free delivery delta message is no longer visible and delivery total is set to €0.00 | Pass ✅ |

</br>

`Cart Item`
<img src="./readme-images/features/cart-item.webp" alt="Cart item">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| Cart Item | When a cart item is added to the shopping cart, it has the correct details of its department, title, size, and quantity along with the correct price information | Add item to cart and check shopping cart page | Cart item details are correct for each corresponding cart item | Pass ✅ |
| Quantity input | The input value of the quantity input correctly reflects the quantity of the cart item | Check shopping cart page with items in cart | Quantity input is populated with the correct value | Pass ✅ |
| Quantity increment button | Clicking the increment button increments the value of the quantity input by one each time | Click button | Quantity is correctly incremented | Pass ✅ |
| Quantity decrement button | Clicking the decrement button decrements the value of the quantity input by one each time | Click button | Quantity is correctly decremented | Pass ✅ |
| Quantity decrement button | Clicking the decrement button when the quantity is at one will prevent the value from being lowered further | Click button when quantity is one | Quantity is prevented from going below one | Pass ✅ |

</br>

`Checkout Section`
<img src="./readme-images/features/checkout-section.webp" alt="Checkout page">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| Checkout Section | Checkout Section is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Checkout Section | Accessing the checkout section with no items in your cart redirects the user back to the homepage with a notification informing them they have no items in their cart | Access checkout page with an empty cart | User is correctly redirected back to the homepage and a popup notification is displayed as feedback | Pass ✅ |
| Banner Heading | Banner heading at the top of the section is correctly rendered and shown to the user | Load website homepage | Banner heading is shown to the user | Pass ✅ |
| Checkout form | Checkout form is correctly shown with all correct inputs | Load checkout page | Form is shown with all correct inputs present | Pass ✅ |
| Checkout form | The correct placeholder text is shown for each field in the form | Check each form field | Form fields all have correct placeholder text | Pass ✅ |
| Checkout form | When checkout form is submitted, then user's profile delivery information is updated to reflect their details | Make a purchase and go to profile page | User's profile delivery information is updated | Pass ✅ |
| Checkout form | Inputs are grouped across three different fieldsets: details, delivery, and card payment respectively | Load checkout page | Form fields are grouped into their correct field sets | Pass ✅ |
| Checkout form | If any required inputs are left blank, the form will not submit | Submit form with blank required fields | Form does not submit | Pass ✅ |
| Card payment input | User is informed of incorrect details with an error message without a page reload | Fill in card details input with incorrect card details | User is notified by an error message without a page reload | Pass ✅ |
| Loading spinner overlay | A loading overlay spinner appears while the order is being processed once the form is submitted | Fill out checkout form and submit | Loading overlay is correctly shown | Pass ✅ |
| Loading spinner overlay | If transaction is either unsuccessful or successful, then overlay is removed | Submit checkout form | Overlay is removed | Pass ✅ |
| Card payment input | Order is successfully processed if all checkout details are correct and form is submitted | Fill out checkout form with correct details | Order is processed and added to database if order is successful | Pass ✅ |
| Payment success notification | A success notification popup is shown to the user if their order is successful | Fill out checkout form with correct details | Success popup notification is correctly shown to the user | Pass ✅ |
| Payment error notification | If the payment information is incorrect, the user will be redirected back to the checkout page and shown an error popup notification | Fill out checkout form with incorrect details | User is redirected and error popup notification is correctly shown to the user | Pass ✅ |
| Checkout order button | Hovering over checkout order button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Checkout order button | Clicking the checkout button submits the form | Click button | Checkout form is correctly submitted | Pass ✅ |
| Order summary | The user's subtotal, delivery, and grand total are correctly calculated and shown to the user | Load checkout page | Cart summary is correctly calculated and shown to the user | Pass ✅ |
| Cart Items list | All items in the cart will be listed below the order summary | Load checkout page | All cart items are correctly shown to the user | Pass ✅ |

</br>

`Order Confirmation Page`
<img src="./readme-images/features/confirmation-page.webp" alt="order confirmation page">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|-----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| Order Confirmation Page | Order Confirmation is fully responsive | Resize viewport | Form correctly adapts to multiple viewport widths | Pass ✅ |
| Order Confirmation Page | Accessing the Order Confirmation Page when not logged in or if the order confirmation does not belong to the user they are redirected back to the homepage | Access page when not logged in or as incorrect user | User is correctly redirected back to homepage | Pass ✅ |
| Order Confirmation Page | When user has successfully checked out and ordered they are directed to their order confirmation | Submit an order from the checkout page | User is redirected to their order confirmation | Pass ✅ |
| Order Confirmation Page | The order confirmation has the correct order details associated with the user's checkout information, reflecting the correct delivery address, order date, and billing info | Submit an order from the checkout page | Order confirmation displays the correct order details | Pass ✅ |
| Order Number | A randomly generated order number is created and assigned to the order | Submit an order from the checkout page | A unique order number is successfully generated for the given order | Pass ✅ |
| Return to home button | Hovering over the return to home button changes background color | Hover over button | Background color correctly changes | Pass ✅ |
| Return to home button | Clicking the return to home sends the user back to the home page | Click button | User is correctly taken back to the home page | Pass ✅ |

</br>

`404 Page`
<img src="./readme-images/features/404-page.png" alt="404 page">
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------- | ---------------------------------------------------------------- | --------------------- | ----------------------------------------------- | --------- |
| 404 Page | 404 page is displayed if the user enters an incorrect URL | Enter incorrect URL | 404 page is correctly shown | Pass ✅ |
| Hero Image | A full screen background image is correctly shown on the page | Load 404 page | Background image is correctly displayed | Pass ✅ |
| Homepage button | Clicking the homepage button takes the user back to the homepage | Click homepage button | User is successfully taken back to the homepage | Pass ✅ |

</br>

## Bugs

#### 1. **ProductStock Validation Error (Solved)**

#### Problem Description:

Initially, it was possible to add sizes to a shoe product outside of the range specified for its department. This meant that small shoe sizes for children could be added to an adult men’s shoe, which is incorrect.

#### Solution:

I added a clean method to the ProductStock model to raise a validation error if the entered size does not match the corresponding ranges defined in the Department model. If there is no match, a ValidationError will be raised on save, preventing the incorrect sizing from being added to the database.

<img src="./readme-images/testing/bugs/1-product-stock-validation-error-fix.webp" alt="code solution for product stock validation error" >

<br />

#### 2. **Create Data Command Error (Solved)**

#### Problem Description:

When populating data in the database using a custom management command, my initial logic involved loading both the product and size JSON fixtures into the database and then iterating through each product, assigning a size with a randomly generated stock amount. This raised a validation error as sizes not matching the correct department of each shoe were accidentally added.

#### Solution:

I implemented a filter statement in the loop to only include sizes belonging to the shoe’s department for each iteration. This ensured that only correct sizes were assigned to each shoe.

<img src="./readme-images/testing/bugs/2-create-data-command-error-fix.webp" alt="code solution for create data command error fix" >

<br />

#### 3. **Rating Model Validation Error: (Solved)**

#### Problem Description:

Users could submit any number as a rating for a shoe, but I wanted to restrict this to a range of 1 to 5.

#### Solution:

Using Django’s pre-made validators, I applied the MinValueValidator and MaxValueValidator to the rating field. This enforced the rating range restrictions.

<br />

#### 4. **Incorrect Price Sorting Error: (Solved)**

#### Problem Description:

Sorting products by price did not account for the sale price, resulting in incorrect sorting. This was because sale prices were derived from a current_price method on the model, which cannot be used by Django querysets for filtering.

<img src="./readme-images/testing/bugs/4-incorrect-price-sorting-error.webp" alt="code showing incorrect price sorting error" >

#### Solution:

I refactored the Product model to include list_price and current_price fields. By overriding the save method, I ensured that the current price was updated based on whether the product was on sale. This allowed the correct sorting of products by their current price.

<img src="./readme-images/testing/bugs/4-incorrect-price-sorting-error-fix.webp" alt="code solution for incorrect price sorting error" >

<br />

#### 5. **I Incorrect Product Sorting Error: (Solved)**

#### Problem Description:

When using the sorting dropdown menu, products were returned as a mixture of all shoe types, regardless of the user’s current shoe type filter. I wanted the sorting to apply only to the currently filtered shoe type.

<img src="./readme-images/testing/bugs/5-incorrect-product-sorting-error.webp" alt="code showing incorrect product sorting error" >

#### Solution:

I adjusted the links in the dropdown options to include a query parameter for the shoe type. By passing the shoe type through the context, only products matching the current shoe type were sorted and returned.

<img src="./readme-images/testing/bugs/5-incorrect-product-sorting-error-fix.webp" alt="code solution for incorrect product sorting error" >

<br />

#### 6. **Duplicate Cart Items Error: (Solved)**

#### Problem Description:

When adding items to the cart, selecting the same shoe and size resulted in duplicate items instead of incrementing the quantity of the existing item.

<img src="./readme-images/testing/bugs/6-duplicate-cart-items-error.webp" alt="code showing duplicate cart items error " >

#### Solution:

In the add-to-cart view, I looped over the cart items to check if an item with the same shoe and size already existed. If found, I updated the quantity value instead of adding a new instance to the cart.

<img src="./readme-images/testing/bugs/6-duplicate-cart-items-error-fix.webp" alt="code solution for duplicate cart items error" >

<br/>

#### 7. **ValueError in Random Sampling For Sale Items: (Solved)**

<img src="./readme-images/testing/bugs/7-sampling-error.webp" alt="code showing value error in random sampling for sale items" >

#### Problem Description:

The `random.sample()` function was used to select #### a random sample of 4 products from a sale_products queryset. If there were fewer than 4 products, `random.sample()` raised a ValueError.

<img src="./readme-images/testing/bugs/7-sampling-error-fix.webp" alt="code solution for value error in random sampling for sale items" >

#### Solution:

To prevent the ValueError, I adjusted the sample size to be the minimum of the number of products on sale and 4 using the `min()` function. This ensured the sample size was always valid, thus preventing the ValueError.

<br />

#### 8. **Validation error in Authentication forms: (Solved)**

#### Problem Description:

In multiple view functions across my app, the LoginForm and RegistrationForm forms were not being validated correctly whenever a post request was made from withe the login or registration model. This caused in an error resulting in an unreliable user experience and potential security vulnerabilities.

<img src="./readme-images/testing/bugs/8-authentication-error-code.webp" alt="code chowing authentication error" >

#### Solution:

The reason for this was because my both the login and registration forms were not defined in the view function before checking the contents of the post request. Defining them above my authentication logic ensure that they could be correctly used in the view functions for authentication and logging in.

<img src="./readme-images/testing/bugs/8-authentication-error-fix.webp" alt="code solution for validation error in authentication forms" >

<br />

#### 9. **Related products error: (Solved)**

#### Problem Description:

I noticed when clicking different products cards, some products would cause the app to crash when the product detail page was loaded. This would only happen for certain products.

<img src="./readme-images/testing/bugs/9-related-products-error.webp" alt="code showing related products error" >

#### Solution:

After inspecting the error and reviewing the data in my fixture files, I realized that I had not accounted for the edge case where certain products might not have a related brand associated with them for a given department. This oversight caused Django to trigger an error because the related products variable did not exist for some products. To resolve this issue, I implemented a conditional check in the template. Now, the related products section on the product detail page will only be displayed when there are products with the same brand present.

<img src="./readme-images/testing/bugs/9-related-products-error-fix.webp" alt="code solution for related products error" >

[Back to Top ^](#testing-documentation)
