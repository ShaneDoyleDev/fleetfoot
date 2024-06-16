<h1 align="center">Fleetfoot 👟</h1>

<img src="readme-images/readme-banner.webp" alt="Sneakers floating in space">

<h3 align="center"><a href="https://fleetfoot-df010c0d8dc8.herokuapp.com/">➡️ View the live project here ⬅️</a></h3>

<br/>

<div align="center">

![GitHub language count](https://img.shields.io/github/languages/count/ShaneDoyleDev/fleetfoot)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/ShaneDoyleDev/fleetfoot)
![GitHub repo size](https://img.shields.io/github/repo-size/ShaneDoyleDev/fleetfoot)

</div>

## Introduction

Fleetfoot is a full-stack ecommerce store I created for a fictional shoe brand specializing in catering to a wide range of footwear needs. The core demographic includes fitness enthusiasts who value quality and performance, fashion-forward professionals who prioritize style and brand reputation, and outdoor adventurers who seek durable, high-performance products.

Users can make credit card purchases through Stripe and sign up for an account to save their profile and delivery information for future convenience. Additionally, they have the ability to leave reviews and ratings on shoes they have purchased, helping others make informed decisions. For marketing purposes, users can also sign up for a newsletter to stay updated on the latest product releases, exclusive offers, and company news.

Care was taken to create a visually cohesive UI and UX experience for visitors to enhance engagement. SEO strategies involving keyword research and optimized semantic HTML were used to improve the discoverability of the site through search engines.

<h3 align="center"><img src="./readme-images/website-preview.webp" alt="a preview of the website shown on a range of different devices"></h3>

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Components](#components)
  - [Wireframe](#wireframe)
  - [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Agile Workflow](#agile-workflow)
  - [Epics And User Stories](#epics-user-stories-and-tasks)
  - [Github Project Boards](#github-project-boards)
  - [MoSCoW Prioritization](#moscow-prioritization)
  - [Story Points](#story-points-and-t-shirt-sizing)
  - [Project Milestones](#project-milestones)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Implementations](#future-implementations)
- [SEO & Marketing](#seo-and-marketing)
  - [Personas](#personas)
  - [Marketing Methods](#marketing-methods)
  - [Keyword Research](#keyword-research)
  - [SEO](#seo)
  - [Sitemap](#sitemap)
  - [Facebook Page](#facebook-page)
  - [Email Marketing](#email-marketing)
  - [GDPR](#gdpr)
- [Technologies](#technologies)
  - [Programming Languages](#programming-languages)
  - [Applications and Libraries](#applications-and-libraries)
- [Local Development & Deployment](#deployment--local-development)
  - [Local Development](#local-development)
  - [Heroku Deployment](#heroku-deployment)
  - [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Credits](#credits)
  - [Code Used And Tutorials](#code-used-and-tutorials)
  - [Acknowledgments](#acknowledgments)

## User Experience (UX)

Fleetfoot was designed as an e-commerce store specializing in selling a wide range of shoes from popular brands. Our primary demographic includes younger individuals, ranging from fashion enthusiasts and comfort seekers to quality-conscious shoppers.

When crafting and planning the design and user experience, I focused on our target demographic to ensure that Fleetfoot’s brand and UI/UX resonate with them in both look and feel. Here’s how I achieved this:

1. **Demographic-Driven Design**:

   - Our design reflects the latest fashion trends, appealing directly to younger shoppers.
   - Bold modern design, and stylish imagery are used throughout the site.

2. **User-Centric Interface**:

   - The navigation is simple and user-friendly, allowing easy browsing and shopping.
   - Responsive design ensures a seamless experience across all devices.

3. **Enhanced User Experience**:

   - Fast loading times and smooth transitions make for an enjoyable shopping experience.
   - Personalized recommendations help users find the perfect pair of shoes quickly.

4. **Efficient Store Management**:

   - User stories were crafted to address both shopper needs and administrative functionalities.
   - Admins can efficiently manage store inventory through comprehensive CRUD (Create, Read, Update, Delete) capabilities.

5. **Responsive Layout**:
   - Care was taken to ensure the layout is fast and responsive for both small and larger devices.
   - The design adapts smoothly, providing a consistent experience regardless of screen size.

### User stories

#### Site Owner Goals

1. As the **site owner**, I want to have an admin account that gives me special privileges for managing store inventory.

2. As the **site owner**, I want to be able to add new products to the database to update the store's inventory.

3. As the **site owner**, I want to be able to increase the stock levels of an existing item if its stock is low or about to be sold out.

4. As the **site owner**, I want to be able to update the information of an existing product, if for example I need to change its sale price or apply a sale discount to it.

5. As the **site owner**, I want to be able to remove an existing product, if for example it is discontinued and I no longer want to sell it.

6. As the **site owner**, I want to have a newsletter section encouraging users to provide their emails for marketing purposes.

7. As the **site owner**, I want users to be aware of how much they need to spend to qualify for free shipping so that they are motivated to spend a little more.

8. As the **site owner**, I want to show related products next to a shoe a user is viewing so that they are encouraged to further browse the products for sale and remain on the store for a long period.

9. As the **site owner**, I want the website design to have a modern look and be aesthetically pleasing and professional to make a good impression on visitors.

10. As the **site owner**, I want to have a section showing links to the various social media channels associated with the brand.

11. As the **site owner**, I want to have a section showing legal copyright information along with the privacy policy for the business.

</br>

#### User Goals

1. As a **user**, I want to be able to easily register with a unique username and password to create an account.

2. As a **user**, I want to be able to easily log in to the site with my username and password to view my account.

3. As a **user**, I want to persist my login session for a longer period of time by clicking a "remember me" box.

4. As a **user**, I want to be able to easily sign out of the site to keep my account secure.

5. As a **user**, I want to receive notifications as feedback confirmation for important actions I perform on the site, including registration, login, logout, and any updates or deletions of store products.

6. As a **user**, I want to have a profile section so that I can save and edit my delivery information for future purchases.

7. As a **user**, I want to be able to keep track of my order history so that I can check my previous orders at a later time if I need to.

8. As a **user**, I want to be able to see at a glance some of the latest shoe releases in season.

9. As a **user**, I want to be able to see at a glance items in the store that are on sale so that I could potentially find and get a good deal.

10. As a **user** who is potentially a brand loyalist, I want to be able to see at a glance the types of brands that are on offer without having to browse through different items in the store.

11. As a **user**, I want to be able to search for shoes only for my gender.

12. As a **user**, I want to be able to filter shoes by different types (sneakers, trainers, high tops, boots, slides).

13. As a **user**, I want to be able to search for shoes based on a descriptive keyword like a brand name.

14. As a **user**, I want to be able to sort by price and name in both ascending and descending order to ease my browsing experience.

15. As a **user**, I want to avoid excessive scrolling when looking through the different store products by having a pagination component to organize them.

16. As a **user**, I want to add shoes I would like to buy at a future date to my wishlist with the click of an icon so I can keep track of them in a central location.

17. As a **user**, I want to see reviews other customers have written on a shoe to help inform my purchasing decision.

18. As a **user**, I want to write my own review and rate a shoe I have purchased to share my opinion and give feedback.

19. As a **user**, I want to see if a product is on sale and how much I could save on my purchase.

20. As a **user**, I want to see the available sizes that are on sale for a product so that I can see if the size of the shoe I wish to purchase is available.

21. As a **user**, I want to be able to see my cart content before checkout and make adjustments to it before I go to the checkout page.

22. As a **user**, I want the store to remember my delivery details and add them to my profile if I have not already done so for future purchases.

23. As a **user**, I want to see delivery confirmation after a successful purchase has been made so that I see a summary of all my order details.

24. As a **user**, I want to be able to check back on my previous order history so that I can see previous order that i have made with the store.

</br>

## Design

- #### Colour Scheme

  ### <img src="./readme-images/design/colors.webp" alt="color palette for the website">

The store features a bold and modern design inspired by other clothing stores and brands. As the images are oriented around a space theme, the UI features a primarily black and white color palette along with various shades of gray for different elements. This allows the UI to blend nicely with the images to create a cohesive visual feel for the brand and allows the colors of the shoes themselves to take center stage in a clean and spacious design.

- #### Typography

  ### <img src="./readme-images/design/typography.webp" alt="typography list for the website">

Roboto was selected as the typeface for the brand and UI due to its clean, bold, and modern sans-serif design, which perfectly complements the imagery and contemporary aesthetic of the UI. It maintains excellent readability across various sizes, making it ideal for diverse applications. Strong, bold typefaces are utilized for headings and important text, ensuring both high readability and a sleek, modern appearance.

- #### Components

  ### <img src="./readme-images/design/components.webp" alt="ui component list for the website">

I adopted a component-centric approach in my UI design, concentrating on creating reusable components that can be applied across various contexts. This strategy ensures a consistent and cohesive appearance throughout the user interface, significantly enhancing the overall user experience on my site.

- #### Wireframe

### <img src="./readme-images/design/figma-wireframes.webp" alt="figma ui wireframe">

I used Figma to create the high-fidelity visual mockup. Upon completion, I had a clear and detailed representation of how I wanted the site to look. This clarity allowed me to transition more efficiently into coding the CSS using Tailwind.

- Complete Wireframes - [View](https://www.figma.com/design/N4FCISeuJglTvhDmGeT9dF/Fleetfoot?node-id=0-1&t=4sotgbvjk1e4XWDK-0)

- Desktop Wireframe - [View](https://www.figma.com/design/N4FCISeuJglTvhDmGeT9dF/Fleetfoot?node-id=345-4782&t=4sotgbvjk1e4XWDK-0)

- Tablet Wireframe - [View](https://www.figma.com/design/N4FCISeuJglTvhDmGeT9dF/Fleetfoot?node-id=345-4783&t=4sotgbvjk1e4XWDK-0)

- Mobile Wireframe - [View](https://www.figma.com/design/N4FCISeuJglTvhDmGeT9dF/Fleetfoot?node-id=345-4784&t=4sotgbvjk1e4XWDK-0)

- Design System - [View](https://www.figma.com/design/N4FCISeuJglTvhDmGeT9dF/Fleetfoot?node-id=327-2&t=4sotgbvjk1e4XWDK-0)

- #### Entity-Relationship Diagram

### <img src="./readme-images/design/edr-diagram.png" alt="the entity-relationship diagram">

Leveraging DrawSQL, I crafted an Entity-Relationship Diagram (ERD) for my PostgreSQL database. This approach proved invaluable, enabling me to visually map out the schema of each entity. It offered a clear, coherent view of how each of the tables interconnected within the database, significantly enhancing my understanding and management of the data structure.

- **User Model** - Used to handle user accounts for when a user registers with the application.
- **Profile Model** - Used to save the user's address within the application.
- **Department Model** - Used to represent a department in the store. There is one for Men's, Women's, and Kids' shoes.
- **Brand Model** - Used to represent a brand (e.g., Nike, Adidas) associated with a particular shoe.
- **Shoe Type Model** - Used to represent a particular type of shoe (e.g., sneakers, boots).
- **Product Model** - Used to represent an actual product in the database.
- **Size Model** - Used to represent the sizing of a shoe and relate it to a particular department (e.g., shoe size: 9 - Men's).
- **Product Stock Model** - An associative table between product and a given size. Each combination of size and product has a corresponding stock level to manage store inventory.
- **Wishlist Model** - Used to keep track of individual wishlist items belonging to a user profile they may wish to purchase in the future.
- **Review Model** - Used to represent a review for a particular product.
- **Rating Model** - Used to represent a rating and is associated with a review. Ratings are in the range of 1 to 5.
- **Order Model** - Used to represent an order for a given purchase.
- **Order Line Item Model** - Represents an individual item within the associated order.

</br>

## Agile Workflow

### Epics, User Stories and Tasks

#### Epics

### <img src="./readme-images/agile/epics.webp" alt="list of project epics on Github">

Using Agile methods, I started my blog project by setting clear goals and deciding what features it would have. I identified the main themes, or "epics," which were broad outlines of what I wanted to achieve. These epics were like the big-picture goals of my project, guiding me towards what I wanted to build.

#### User Stories

### <img src="./readme-images/agile/user-stories.webp" alt="list of project user stories on Github">

After defining all project epics, I broke them down into user stories. These stories were more detailed and focused on the needs and problems of my potential users. They helped me stay on track with my project goals, making sure I was building something people would actually find useful. For each story, I created a GitHub issue, describing the feature from a user's perspective and listing what criteria it needed to meet to be considered done.

#### Tasks

### <img src="./readme-images/agile/tasks.webp" alt="list of tasks on a user story card">

I then listed all the individual tasks needed to complete each user story, breaking down the work into small, manageable parts. I used a checklist to keep track of what had been done and what still needed attention. This helped me stay organized and focused on the small details, ensuring that I met all the criteria for my user stories throughout the project.

### Github Project Boards

#### Github Project - User Stores List

### <img src="./readme-images/agile//user-stories.webp" alt="user stories project board">

With the aid of GitHub projects, I grouped and organized all my user stories together in a project list view. This enabled me to visually grasp the most crucial aspects of each user story, and visualizing the interconnectedness between user stories and their respective Epics provided invaluable insights into the project's overarching goals and objectives.

You can see the project board here - <a href="https://github.com/users/ShaneDoyleDev/projects/8">User stories list</a>

#### Github Project - Kanban Board

### <img src="./readme-images/agile/kanban-board.webp" alt="user stories kanban board">

I also implemented a Kanban board as an effective information radiator throughout each project milestone. This strategic approach enabled me to monitor the progress of tasks—from the initial backlog to current work-in-progress, all the way to completion. By visually mapping out each step of the process, the Kanban board provided a clear, real-time overview of the project's status, ensuring seamless tracking and management of tasks at every stage.

You can see the project board here - <a href="https://github.com/users/ShaneDoyleDev/projects/8/views/2">Kanban board</a>

### MoSCoW Prioritization

### <img src="./readme-images/agile/moscow.webp" alt="list of moscow labels on a Gihub project board">

I used MoSCoW prioritization technique to label each user story and prioritize tasks according to their significance to the project's objectives. This strategic approach enabled me to identify and focus on the most critical tasks first, ensuring the project remained on schedule. By optimizing my time management in this manner, I could concentrate on delivering the essential features required for the Minimum Viable Product (MVP) and other key deliverables, effectively steering the project towards its successful completion while aligning with the project's overarching goals.

- **Must have**: These are non-negotiable requirements that the project needs to be successful and meet the requirement scope of the Minimum Viable Product (MVP).
- **Should have**: Important but not vital requirements, which could be included if time and resources permit.
- **Could have**: Desirable but not necessary requirements. These are features that could be added as additional features and enhancements for the app in the future.

### Story Points and T-Shirt Sizing

### <img src="./readme-images/agile/t-shirt-sizing.webp" alt="list of moscow t-shirt sizing values on a Gihub project board">

T-shirt sizing is a popular method used in Agile to measure story points. This was what I employed as my chosen method to evaluate the effort required for completing each user story. User stories were compared against a benchmark task, with size categories — ranging from XS to XXL — assigned to represent the relative complexity and effort needed.

I learned about this agile estimation technique from these learning resources:

- <a href="https://activecollab.com/blog/project-management/t-shirt-sizing">T-Shirt Sizing - Agile Estimation Guide</a>
- <a href="https://asana.com/resources/t-shirt-sizing">How to Use T-Shirt Sizing to Estimate Projects</a>

### Project Milestones

### <img src="./readme-images/agile/project-milestones.webp" alt="Project milestones">

The project timeline was strategically segmented into four key milestones, one for each week of development. Each milestone each represents a distinct sprint or unit of work. This structure played a crucial role in the planning and development phases, enabling me to prioritize the development of the most critical features first from week one onwards.

By adopting this approach, I effectively minimized the risk of allocating time to features that were not essential to the app's core functionality, ensuring a more focused and efficient progression towards the project goals.

You can see the project milestones here - <a href="https://github.com/ShaneDoyleDev/fleetfoot/milestones">Project milestones</a>

</br>

## Features

### Existing Features

<br />

<h3 align="center">Navigation Bar (Desktop)</h3>

### <div align="center"><img src="./readme-images/features/navigation-desktop.webp" alt="Desktop navigation bar"></div>

- The navigation bar on desktop is overlaid on top of the hero image and consists of two main sections to the left and right of each other.

- The left side of the navigation contains the company logo, which, when clicked, takes the user back to the homepage of the site. Next to this are menu links to the three departments of the store (Men's, Women’s, and Kids respectively) used for organizing the shoe products. Clicking each one will take the user to the products list page of shoes for that department.

- The right side of the navigation features login and registration items for logging into and creating an account with the website and also features the cart showing the user their current cart total.

In addition to this, when the user logs in, they will be presented with a profile section for managing their profile details and a wishlist section allowing them to save products they may wish to purchase in the future.

- For admin users, there is an additional link to the product admin section, which takes them to the product admin page, allowing them to add new products and update the existing stock of products in the store.

### <div align="center"><img src="./readme-images/features/navigation-tablet.webp" alt="Tablet navigation bar"></div>

- On tablet screens, these sections collapse into a column formation to prevent them from conflicting with each other on smaller screen widths.

<br />

---

<br />

<h3 align="center">Navigation Bar (Mobile)</h3>

### <div align="center"><img src="./readme-images/features/navigation-hamburger.webp" alt="Navigation hamburger"></div>

### <div align="center"><img src="./readme-images/features/navigation-mobile.webp" alt="Navigation hamburger"></div>

- On mobile screens, the navigation bar will reveal a hamburger icon which, when clicked, will show a fullscreen overlay of the mobile navigation menu.

The mobile navigation menu features all of the same navigation menu items found on the desktop navigation but they have been rearranged to accommodate the width of smaller screens.

- Clicking the Fleetfoot title logo will take the users to the homepage, and the close icon in the top right-hand corner of the navigation overlay will close the mobile navigation.

<br />

---

<br />

<h3 align="center">Hero Section</h3>

### <div align="center"><img src="./readme-images/features/hero-section.webp" alt="Website hero image"></div>

- The Hero Section occupies the full width of the screen and is located at the top of the page, above the fold (i.e., the portion of the webpage visible without scrolling). Given its prime location, I wanted it to capture the visitor's attention and prompt them to engage further with the content or offerings of the website.

- I also ensured to position the imagery in a way that would look good across a range of different devices, from desktops to mobile.

- When on large screens, an animated arrow icon becomes visible that, when clicked, directs the user using smooth scroll to the section just below the hero image. This informs them that there is more content below, as the hero image grows to take up the full screen on larger sizes. I thought this would be a nice little UX feature to add.

<br />

---

<br />

<h3 align="center">Product Card</h3>

### <img src="./readme-images/features/product-card.webp" alt="Product card">

- The product card is a reusable UI component used to showcase each of the shoes in the store by summarizing key information at a glance that shoppers would be interested in.

- A clickable showcase of the shoe is shown along with the corresponding department (e.g., men's, women's, kids) and the list price.

- Additionally, if the product is on sale, the percentage off will be shown along with the calculated sale price next to the list price to show users how much they will save.

- There is a wishlist heart icon that, when clicked, will toggle the product in the user's wishlist. This updates the database via an AJAX call, which prevents a page reload. When clicked, the heart will change from an outline to a solid icon to reflect the change to the user.

- If a user with admin privileges logs into the site, they will be presented with an edit icon and a delete icon. Clicking the edit icon will take them to the product admin page where they can edit the existing information and update the stock of that particular product.

- Clicking the delete icon will trigger a warning confirmation box as a safety measure, which, when confirmed, will delete the product from the store's database.

<br />

---

<br />

<h3 align="center">Latest Shoes Section</h3>

### <img src="./readme-images/features/latest-shoe-section.webp" alt="Latest shoes section">

- The latest products section is there to showcase all of the latest products that have been recently added to the store.

- Positioned below the homepage's hero image, this section is one of the first elements visitors see. Its placement appeals to fashion-conscious buyers who are especially keen on purchasing the latest releases of shoes from their favorite brands when they are released.

<br />

---

<br />

<h3 align="center">Newsletter CTA Section</h3>

### <img src="./readme-images/features/newsletter-section.webp" alt="Newsletter CTA section">

- The Newsletter Call-To-Action (CTA) Section features compelling imagery alongside a message aimed at enticing users to sign up. On desktops, the image and CTA are side by side; on smaller screens, they shift to a column layout for better usability.

- The newsletter sign-up form uses an embedded form from Mailchimp that I customized to match the look and feel of the rest of the site. When users submit their email, they are added to the store's subscription list via Mailchimp.

### <img src="./readme-images/features/newsletter-success.png" alt="Newsletter sign-up success message">

- On successful submission, users will be notified via a popup message just below the input to inform them.

### <img src="./readme-images/features/newsletter-mobile.webp" alt="Newsletter CTA section on mobile">

- This section is fully responsive and changes orientation for a better layout on smaller screen sizes.

<br />

---

<br />

<h3 align="center">Sale Section</h3>

### <img src="./readme-images/features/sale-section.webp" alt="Sale section">

- For shoppers who are conscious of wanting to get the best deals on sale, this section of the website is there to highlight any products which are currently on sale for a good discount.

- This section will be randomly populated with four chosen sale items each time the page loads, so the user will see new sale items on each visit.

<br />

---

<br />

<h3 align="center">Brands Section</h3>

### <img src="./readme-images/features/brands-section.webp" alt="Brands section">

- As loyal brand followings withing the fashion market are common, this section allows the store to showcase well-known brands that are available for sale at a glance.

- Followers of these brands, upon seeing their logos, may be enticed to further explore the store's offerings. This helps retain visitors for longer periods, which is why this section is featured prominently on the homepage.

<br />

---

<br />

<h3 align="center">Footer Section</h3>

### <img src="./readme-images/features/footer.webp" alt="">

- The footer section of the website is used to show links to corresponding social media pages for the store. (Since this is a fictional store, the links just direct to the homepage of each social media platform respectively.)

- Clicking the Facebook icon will direct the user to a screenshot mockup of the Facebook page I created. Since Facebook deletes these unused business pages, I used this screenshot as a fallback.

- Below the social media images, there is some important legal information in the form of a privacy policy to comply with GDPR standards and also copyright information.

- I also use this section to link to my own personal GitHub profile for others to see my portfolio of work.

<br />

---

<br />

<h3 align="center">Products List Section</h3>

### <img src="./readme-images/features/product-list-section.webp" alt="Products list section">

- The products of the store are divided across three categories of customers: men, women, and kids.

- The heading of the section will change to reflect which department the user is currently viewing. Only shoes belonging to the corresponding department will be shown.

- The page features a range of options to help customers search and filter for the products they want.

- The shoe products are further divided across several shoe types. When selecting the shoe type in the menu, only the shoes belonging to that type will be shown.

- Pagination is used to limit the number of products shown at any one time to the user, preventing excessive page scrolling while viewing.

<br />

---

<br />

<h3 align="center">Products Search Bar</h3>

### <img src="./readme-images/features/searchbar.webp" alt="Products search bar">

- Typing a brand or part of a description into the search bar will only show products which match the search term.

- If a user submits an empty search query, they will be notified via a popup notification.

<br />

---

<br />

<h3 align="center">Products Sorting Dropdown</h3>

### <img src="./readme-images/features/dropdown-filter.webp" alt="Products sorting dropdown">

- The sorting dropdown allows a user to sort the list of products by either name in alphabetical order or by price when clicked.

- Users can sort by these options in either ascending or descending order.

<br />

---

<br />

<h3 align="center">Pagination</h3>

### <img src="./readme-images/features/pagination.webp" alt="Pagination component">

- Pagination is implemented on the products list to display a maximum of nine products at a time, reducing clutter and minimizing scrolling.

- Clicking the pagination buttons will take the user to that section of the list. First and last buttons are also provided for convenience to allow the user to quickly reach the beginning or end of the list for faster navigation.

<br />

---

<br />

<h3 align="center">Login Modal</h3>

### <img src="./readme-images/features/login-modal.webp" alt="Login model">

- Clicking the login menu item in the navigation will cause a login modal popup to appear as an overlay on the screen.

- Having a modal provides a nicer interactive experience for the user as it means they don't have to navigate to a separate page for authentication purposes.

- Users can log in using a username and password that they defined during the registration process.

- Clicking the cross icon will close the login modal.

- Clicking the "remember me" checkbox will set the session expiry to 1209600 seconds, which is equivalent to 14 days. This means the user's login session will persist for 14 days, allowing them to revisit the site without needing to log in again during this period.

- If the user enters incorrect details, they will be redirected back to the home screen and given a notification informing them that their credentials are incorrect.

- If the user logs in correctly, they will be shown a success notification and new features will be available to them.

- The modal form is fully responsive, ensuring ease of interaction on smaller screen sizes.

<br />

---

<br />

<h3 align="center">Registration Modal</h3>

### <img src="./readme-images/features/registration-modal.webp" alt="Registration form">

- Clicking the registration menu item in the navigation will cause a registration modal popup to appear as an overlay on the screen.

- Users are required to enter a username and a password along with a password repeat field as their credentials.

- If a user leaves a field invalid, they are redirected back to the homepage, and an error validation message is displayed.

- Upon successful account creation, a new user is added to the database, and they receive a notification via a popup message.

- The modal form is fully responsive, ensuring ease of interaction on smaller screen sizes.

<br />

---

<br />

<h3 align="center">Product Detail Section</h3>

### <img src="./readme-images/features/product-detail.webp" alt="product detail section">

- When a user clicks on a product card, the corresponding product detail page will be shown for that product. Here the user can see more information about it.

- The product detail section features a more detailed product description, which is a good area to strategically place keywords in the content for SEO.

- It also features a main showcase hero image for the particular shoe, along with the rating, and available sizes to purchase.

- Users can select a specific quantity and add it to their cart from this page.

### <img src="./readme-images/features/product-detail-mobile.webp" alt="product detail section">

- This section, as with all sections, is fully responsive as each of these sections will arrange themselves into a column formation for a better viewing experience on smaller screens.

<br />

---

<br />

<h3 align="center">Related Product Component</h3>

### <img src="./readme-images/features/related-product.webp" alt="Related product component">

- In order to prolong the user's shopping experience and view more products, I created a related product component in this section.

- Since many shoppers tend to have a loyalty to certain brands, the related product section shows another shoe from the same brand for them to view and potentially purchase.

- The component will randomly select a shoe of the same brand from the store each time the page loads.

<br />

---

<br />

<h3 align="center">Product Showcase Image</h3>

### <img src="./readme-images/features/showcase-image.png" alt="product showcase image">

- The product hero image is showcased front and center and is designed to be eye-catching, displaying the product in a way that is dynamic and interesting to look at.

- Each product for the store is rendered as a cutout PNG with transparency that I made in Photoshop. Doing it this way allows me to rotate the image and use a shadow to give it a more dynamic look and make for a more aesthetically pleasing experience for the viewer.

<br />

---

<br />

<h3 align="center">Average Product Rating</h3>

### <img src="./readme-images/features/average-rating.webp" alt="eAverage product rating">

- This component allows the user to see an aggregate of the overall average rating of the product from all customer reviews combined.

- If no ratings are provided, then a list of empty stars will be rendered to reflect that.

- If reviews are submitted, then the corresponding amount of filled stars will be shown to reflect the overall average rating along with the score.

- This handy component allows the user to quickly get a feel for the customer opinions of the product at a glance without having to wade through multiple reviews.

<br />

---

<br />

<h3 align="center">Avaliable Sizes Chart</h3>

### <img src="./readme-images/features/avaliable-sizes.webp" alt="Available sizes component">

- A list of available sizes will be shown for each product, which, when clicked, will allow the user to add that size to their shopping cart.

- Only sizes that are currently in stock for that product will be shown, to prevent users from attempting to purchase a size that is currently sold out.

<br />

---

<br />

<h3 align="center">Add To Cart Button</h3>

### <img width="400" src="./readme-images/features/add-to-cart-inactive.webp" alt="Add to cart inactive">

- If a user has not selected a size, the "Add to Cart" button will be greyed out and a "Select a size" message will be displayed. When the button is in this state, it is not clickable. This is to prevent the user from trying to add a shoe of an unspecified size to their cart.

### <img width="400" src="./readme-images/features/add-to-cart-active.webp" alt="Add to cart active">

- Once a size is selected, the button changes to a clickable state and the message changes to "Add to Cart".

- A quantity input with increment and decrement buttons allows a user to select a quantity of items to buy. The number will correspond to the quantity of that item in the cart.

<br />

---

<br />

<h3 align="center">Product Review Section</h3>

### <img src="./readme-images/features/reviews-section.webp" alt="Customer review section">

- This section is used to render a list of reviews that customers have previously written for the product featured on its detail page.

### <img src="./readme-images/features/reviews-section-empty.webp" alt="Customer review section">

- If there are currently no reviews for the product, a message box notifies the user of this.

- Each review features the username of the customer, a star rating in the range of 1 to 5, the date it was created, and the review itself.

### <img src="./readme-images/features/review-form.webp" alt="Customer review form">

- If the user is logged in, they will see a form allowing them to write their own review of the product.

- If a user leaves a field blank or tries to submit a rating greater or less than the range of 1 to 5, they will be notified via popup and redirected back to the page, preventing them from submitting a review with incorrect details.

<br />

---

<br />

<h3 align="center">Profile Section</h3>

### <img src="./readme-images/features/profile-section.png" alt="Profile section">

- The profile section is where a user can fill in their profile information. This information will be used to populate the checkout form for convenience every time they wish to make a purchase.

- The profile section is available for the user to access only after they have registered for an account and logged in.

- As this view contains sensitive information pertaining to the user, it is protected and only accessible to the logged-in user. Any attempt to access it otherwise will redirect the user back to the homepage.

- To the right of the form, users can see a list of their order history. Each item in their order history features a summary of the order information.

- Clicking the order number takes the user to their order confirmation page so they can see more detail about that particular order. Having their history organized in one place allows them to efficiently keep track of their prior purchases.

<br />

---

<h3 align="center">Wishlist Section</h3>

### <img src="./readme-images/features/wishlist-section.webp" alt="Wishlist section">

- When a user clicks the heart icon next to a product, it will be added to the user's wishlist section and show up here. This allows users to save an item for future purchase.

- Clicking the heart icon once changes it to a solid version and adds the item to the wishlist. Clicking it again changes it to an outline and removes it.

<br />

---

<h3 align="center">Product Admin Section</h3>

### <img src="./readme-images/features/admin-add-product.webp" alt="Product admin section">

- The product admin section allows the admin to make changes to the store's inventory. There are two forms here: one to allow the admin to add a new product to the inventory and another to update the stock levels of an existing item. There is a menu that allows the admin to toggle between them dynamically.

- The add product form is used to add a product to the store's database. Here, they can enter all required details for the product.

### <img src="./readme-images/features/admin-update-stock.webp" alt="Product admin section">

- The increase stock section allows admins to update and add to the existing stock levels of a product. This is used when more quantities of an item need to be added to the store as they come in.

- If data entered into either form does not align with the validation requirements, the admin will be redirected back to the page and shown the form error.

- If data is submitted correctly, a success popup notification will notify them of a successful addition to the database.

<br />

---

<h3 align="center">Shopping Cart Section</h3>

### <img src="./readme-images/features/cart-section.webp" alt="Shopping cart section">

- When a user adds a shoe of a selected size and quantity, it will appear in the cart section of the store.

  Here, users can make adjustments to the items in their cart before they proceed to checkout.

- Each cart item shows the product image and details along with a quantity input for adjusting how much of the items they wish to purchase.

- Users can update the quantity by entering an amount and clicking update to change it and clicking remove will remove it from the customer's shopping cart.

- When an item has been adjusted or removed from the cart, the user will be notified via a pop-up.

- To the right of the cart item is the summary of the cart total along with any potential delivery fees.

### <img src="./readme-images/features/delivery-delta-message.webp" alt="Delivery delta message">

- If the customer's purchase total is below the free delivery threshold of €50, they will be shown the delivery fee along with a message showing the free delivery delta.

<br />

---

<h3 align="center">Checkout Section</h3>

### <img src="./readme-images/features/checkout-section.webp" alt="Checkout page">

- The checkout section is where the user can make a purchase on the shoes they have added to their cart after entering their billing details.

- This section features the Stripe card element used by the Stripe API to securely process credit card payments.

- To the right of the form is the cart summary so users can see their total and any delivery costs. If the user is below the free delivery threshold, they will be notified of this along with the price delta.

- Below the cart summary is a list of the items in the user's cart so they can confirm that they are about to purchase the correct shoes from the store. An "Adjust Cart" button is provided for convenience to take the user back to the cart if they need to change something.

<br />

---

<h3 align="center">Order Confirmation</h3>

### <img src="./readme-images/features/confirmation-page.webp" alt="0rder confirmation page">

- After the user has successfully made a purchase, they will be taken to their order confirmation page. This outlines all of the details the customer will need to see after purchase.

- These order details are stored in the database so that the user can access them from their profile page.

- For security purposes, the view for rendering the confirmation page is protected so that only the logged-in user the order belongs to can access it to protect their information.

- Clicking the "Back to Home" button at the bottom of the form takes them back to the homepage.

<br />

---

<h3 align="center">404 Page</h3>

### <img src="./readme-images/features/404-page.png" alt="404 page">

- The 404 Page showcases a relevant, colorful image that fits with the site's overall style, reassuring users they're still on the same website. It provides a button to easily return to the homepage for a smoother experience.

<br />

---

### Future Implementations

1. **Light and Dark Theme Options**

   - Users can toggle between light and dark themes using a switch in the navbar, enhancing the reading experience based on ambient light levels and time of day.

   <br/>

2. **Discount Coupons**

   - Discount codes could be issued at certain points in the year, allowing the customer to redeem discounts on certain products.

   - Users could enter the coupon code at checkout to qualify for some percentage of discount off their order.

   <br/>

3. **Enhanced Social Media Integration**

   - As social media marketing is an important part of the overall strategy of many e-commerce stores, there could be more features added to improve integration with social media platforms beyond a Facebook page.

   - Possible features include:

     - Sharing buttons for various social media platforms on product pages.
     - Integration with Instagram shopping to allow users to purchase products directly from social media posts.
     - Social media login options for faster account creation and login.

     <br/>

4. **Image Gallery**

   - Having an interactive photo gallery of the product featured at different angles and allowing the user to interactively zoom in would be a nice addition to the product viewing experience.

   - Additional features could include:
     - High-resolution images for detailed viewing.
     - 360-degree views to give a comprehensive look at the product.
     - Videos demonstrating the product in use to provide better context for the customers.

</br>

## SEO And Marketing

Fleetfoot is a B2C e-commerce store specializing in selling a wide variety of shoes from well-known brands. In order to compete against similar businesses in the space, both SEO and marketing strategies needed to be revitalized to drive traffic and boost sales. By understanding the target audience and crafting a tailored approach, we can enhance the brand’s online presence and engage with potential customers more effectively. This section outlines the personas developed from market research, the marketing methods suited for our demographic, and the keyword research conducted to optimize search engine rankings.

### Personas

During my marketing research, I identified the core demographic for Fleetfoot. I created three imaginary personas to ensure that the content and keywords effectively address the needs and interests of diverse customer segments. This approach tailors the marketing and SEO strategy to attract and engage these potential customers more effectively. Here are the personas and their characteristics:

#### Persona 1: Fitness Enthusiast

- **Lifestyle:** Active, health-conscious, regularly attends the gym and outdoor activities
- **Interests:** Running, hiking, yoga, fitness trends, healthy eating
- **Shopping Habits:** Prefers online shopping for convenience, values quality and performance in products, often influenced by customer reviews and expert comparisons

#### Persona 2: Fashion-Forward Professional

- **Lifestyle:** Trendy, urban, enjoys staying updated with the latest fashion trends
- **Interests:** Fashion, design, music, attending social events
- **Shopping Habits:** Enjoys both online and in-store shopping, prioritizes style and brand reputation, looks for unique and limited edition items

#### Persona 3: Outdoor Adventurer

- **Lifestyle:** Adventurous, nature lover, frequently engages in outdoor activities such as hiking, camping, and trekking
- **Interests:** Environmental conservation, hiking, traveling, photography
- **Shopping Habits:** Prefers shopping for durable and functional products, values sustainability and eco-friendliness, often reads product reviews and comparison guides before purchasing

</br>

### Marketing Methods

Given that my users primarily belong to a younger demographic, it is very likely that they are active on social media. Therefore, leveraging these platforms for marketing is an effective strategy to make them aware of new products, sales, and discounts. Having a Facebook page and a **subscription newsletter** would be ideal for keeping them engaged and informed. Using a platform like **Facebook** for real-time updates and promotions, a subscription newsletter, and potential **influencer partnerships** could further enhance brand visibility and reach within this target audience.

After doing some research on other footware retailers in the space like **JD Sports**, **Foot Locker** and **Footshop**. I came up with some more detailed strategies for each marketing platform:

#### Facebook Business Page

- **Real-Time Updates:** The Facebook page could be used to post real-time updates about new product launches, ongoing sales, and exclusive discounts. Regular posts, stories, and engaging content can keep the audience informed and interested.

- **Interactive Content:** Create polls, quizzes, and live videos to increase engagement. the page can be used to respond to comments and messages promptly to build a community and foster loyalty.

- **Events and Groups:** Host virtual events and create groups for more niche communities within the audience. This fosters a sense of belonging and encourages more active participation.

#### Subscription Newsletter

- **Regular Communication:** A subscription newsletter could be an excellent way to provide curated content directly to the users’ inboxes. Regular updates can include personalized recommendations, exclusive discounts, and sneak peeks of upcoming products.
- **Segmentation:** I could segment the email list based on user preferences and behavior to send targeted content that resonates more effectively with different user groups.
- **Engaging Content:** Incorporate visually appealing designs, user-generated content, and stories that resonate with the audience. This keeps the newsletter interesting and engaging.

#### Influencer Partnerships:

- **Authenticity and Reach:** Partnering with influencers who align with the brand values could significantly enhance the reach and credibility of Fleetfoot. Influencers can showcase your products in a relatable and authentic way, which is often more effective than traditional advertising and would appeal to a younger demographic in particular
- **Collaborative Campaigns:** Fleetfoot could work with influencers on campaigns that include giveaways, unboxing videos, reviews, and tutorials. This type of content can drive significant engagement and conversion rates.

</br>

### Keyword Research

To attract the maximum number of customers, it is crucial for an eCommerce store to achieve high rankings on search engines. High search engine rankings increase visibility, drive more traffic to the site, and ultimately boost sales.

When developing an effective list of keywords for SEO optimization, I began by brainstorming a range of general topics. Since I had clearly defined personas before starting this process, it helped me understand the specific needs, interests, and shopping habits of each persona. This understanding allowed me to brainstorm topics that are highly relevant to them. Below is the list of keywords I chose, based on a mix of long-tail and short-tail variations.

##### **Topic** - Specific Shoe Types and Styles

Focusing on specific shoe types and styles allowed me to target a broad range of customer interests and preferences. Many shoppers search for shoes based on their specific needs, such as everyday wear, workouts, casual outings, or specific occasions. By finding keywords on these topics, I could attract visitors looking for these specific products and help guide them towards making a purchase.

#### Keyword Ideas

- Best sneakers for everyday wear
- Trainers for workouts
- Stylish hightops
- Durable boots for hiking
- Comfortable sliders for summer
- Designer hightops for streetwear
- Casual high-top shoes
- Versatile hightops for casual wear
- Cushioned sliders for lounging

##### **Topic** - Popular Brands and Models

Brand loyalty is strong in the footwear market. Shoppers often search for their favorite brands or specific models they've heard about. By highlighting popular brands and models, I could capture the interest of brand-conscious consumers and those looking for the latest or most trusted products from well-known companies.

#### Keyword Ideas

- Best Nike sneakers
- Top Adidas trainers
- Popular Adidas running shoes
- Latest Converse hightops
- Popular Birkenstock sliders
- Popular Timberland casual boots
- On running high performance
- Best Reebok casual sneakers

##### **Topic** - Performance and Comfort

Comfort and performance are key factors for many shoe buyers, especially for athletic footwear. By looking into keywords around this topic, I could potentionally attract customers looking for shoes that meet their specific performance needs or comfort needs in a shoe.

#### Keyword Ideas

- Best trainers for running and fitness
- Comfortable sneakers for all-day wear
- Waterproof boots for rain
- Cushioned sliders for comfort
- Best trainers for gym workouts
- Lightweight running trainers
- All-day comfort sneakers

#### Chosen keywords

Once I had brainstormed a list of keywords for each of my topics, I used them to further refine my list by entering them into a free AI-powered [SEO keyword research tool](https://www.ryrob.com/keyword-tool/). Using this tool, I came up with a final list of keywords that provided a good balance between having a sufficient volume of searches and not being overly competitive, with a difficulty ranking of either low or medium at most.

<img width="500" src="./readme-images/marketing/keyword-research/best-shoes-for-running-and-gym.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/best-adidas-trainers-for-men.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/ladies-shoes-online-sale.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/womens-sneakers-for-comfort.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/best-sneakers for-everyday-wear.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/popular-shoes-to-buy.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/childrens-shoes-online-sale.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/best-slides-for-summer.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/sneakers-for-everyday-use.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/mens-shoes-discount-sale.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/shoes-for-indoor-use.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/coolest-kids-shoes.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/latest-comfortable-shoes.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/stylish-shoe-brands.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/stylish-high-tops.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/sneakers-on-sale.webp" alt="Keyword ranking statistics">
<img width="500" src="./readme-images/marketing/keyword-research/top-nike-trainers.webp" alt="Keyword ranking statistics">

<br/>

### SEO

With these keywords chosen, I made sure to tactically place them in key areas of the site where they would make sense in order to help bolster the page ranking. I made sure to use them in appropriate areas of the site with semantic HTML tags where it made sense to do so and avoided keyword stuffing to ensure the content and user experience were not affected. Three particular areas of focus on the site included:

#### Meta Tags

<img width="500" src="./readme-images/marketing/seo/meta-tags.webp" alt="Keyword meta tags">

<br/>

I used the content meta tag to provide some keywords in the description of the site and also the keywords meta tag to include all of the keywords I chose from my research.

#### Headers

<img width="500" src="./readme-images/marketing/seo/latest-header.webp" alt="Keyword in heading">
<img width="500" src="./readme-images/marketing/seo/latest-header.webp" alt="Keyword in heading">
<img width="500" src="./readme-images/marketing/seo/cta-heading.webp" alt="Keyword in heading">
<img width="500" src="./readme-images/marketing/seo/brands-header.webp" alt="Keyword in heading">
<img width="500" src="./readme-images/marketing/seo/sale-header.webp" alt="Keyword in heading">

<br/>

The headers of the site for different sections were another opportunity to use keywords as they carry semantic weight for ranking. By including relevant keywords in headers (`<h1>`, `<h2>`, etc.), I ensured that search engines would recognize the importance of these terms, helping to improve the page’s ranking.

#### Product Descriptions

<img width="500" src="./readme-images/marketing/seo/air-force-description.webp" alt="Keyword in product description">
<img width="500" src="./readme-images/marketing/seo/birkenstock-description.webp" alt="Keyword in product description">
<img width="500" src="./readme-images/marketing/seo/air-max-plus-description.webp" alt="Keyword in product description">

<br/>

Finally, the product descriptions were written to include the keywords where appropriate to that section. This ensured that the content remained relevant and useful to the users while still optimizing for search engines. Each product description was carefully crafted to naturally integrate the keywords, improving both SEO and user experience.

#### Sitemap

I generated the complete sitemap using [XML Sitemaps](https://www.xml-sitemaps.com/). A sitemap provides important information about the pages, videos, and other files on your website, and the relationships between them. This helps search engines like Google crawl your site more efficiently and effectively. The sitemap includes metadata about each URL, such as the last update date, change frequency, and priority compared to other URLs.

After generating the sitemap, I added a <strong>robots.txt</strong> file to guide search engine crawlers on which pages to crawl and index. The <strong>robots.txt</strong> file helps manage crawler traffic and prevent the indexing of certain parts of your site that you want to keep private or unnecessary for search engine results.

#### Facebook Page

<img width="500" src="./readme-images/marketing/fleetfoot-facebook-page.webp" alt="Fleetfoot Facebook page">

As social media is a core part of my marketing strategy for my demographic, having a Facebook page is crucial for improving market reach and serving as an entry point to the main e-commerce store. This page allows for direct engagement with our target audience, helping to build a loyal following. Additionally, it provides a platform for showcasing products, promoting events, and driving website traffic. By leveraging Facebook’s advertising tools and insights, we can create targeted campaigns and refine our marketing strategies. The page also supports customer interaction and feedback, enhancing our brand’s reputation and credibility.

As Facebook can potentially delete ‘fake’ business profiles on its platform, which could lead to the deactivation of the page, I have taken the necessary steps to ensure compliance. After creating the page and uploading the necessary assets, along with creating an initial post, I have supplied a screenshot of the finished page that the user would see if they navigated to it.

</br>

#### Email Marketing

<img width="500" src="./readme-images/marketing/newsletter/email-subscription.png" alt="Call to action subscription form">
<img width="500" src="./readme-images/marketing/newsletter/subscription-success.png" alt="Call to action subscription form">

A CTA section was created on the home page to entice users to sign up for the subscription newsletter. The text informs users of the benefits, ensuring they are notified of the latest deals and discounts in the store, thereby increasing their chances of making substantial savings on their favorite products. This could be of particular value to the younger demographic, such as students, who are likely to be interested in the latest releases of new trendy styles from popular brands. Being conscious of their disposable income, they are also likely to want to take advantage of any deals or sales the store offers.

<img width="500" src="./readme-images/marketing/newsletter/mailchimp-dashboard.png" alt="Call to action subscription form">

The email subscription is handled by [Mailchimp](https://mailchimp.com/). Using their embedded form, I integrated and modified the HTML and styling to make it fit in with the theme of my website.

#### GDPR

As your e-commerce store interacts with sensitive personal data from users and uses their emails for potential newsletter purposes, it is crucial to ensure compliance with GDPR requirements. A privacy policy was generated from [Privacy Policy Generator](https://www.privacypolicygenerator.info/) to help in this regard.

Users can find a link to the full privacy policy in the footer section of the store. You nac see the privacy policy for Fleetfoot here - <a href="https://www.termsfeed.com/live/a563c3a6-f140-469d-8834-920feee0bb83">Privacy Policy</a>

</br>

## Technologies

### Programming Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Applications and Libraries

1. [Django](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design. Used for building the main application structure and functionality.

2. [Tailwind](https://tailwindcss.com/) - Tailwind is a CSS framework that allows you to compose your styles by combining utility classes directly in the HTML markup.

3. [PostgreSQL](https://www.postgresql.org/) - An open-source, advanced object-relational database system used to store data for the application.

4. [Code Institute Database Maker](https://dbs.ci-dbs.net/) - An API utilized in the application, allowing up to 100 requests per day for free. It enables filtering the response by category and language.

5. [Visual Studio Code](https://code.visualstudio.com/) - A source-code editor developed by Microsoft for Windows, Linux, and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. Used as the preferred IDE for coding the HTML, CSS, and JavaScript, aiding in the development process and creation of markdown README files.

6. [Amazon Web Services](https://aws.amazon.com/) - AWS and specifically its S3 storage service were used to handle storing and accessing static and media files for deployment.

7. [Git](https://git-scm.com/) - A free and open-source distributed version control system used to handle the project's code versioning, enabling tracking of changes and collaboration.

8. [GitHub](https://github.com/) - A platform for hosting and sharing source code, utilizing Git for version control. It hosts the project remotely, making the source code accessible to others, and is used for deploying the site via GitHub Pages.

9. [GitKraken](https://www.gitkraken.com/) - A graphical user interface (GUI) Git client that facilitates managing Git repositories through a visual interface, particularly useful for visualizing commit history and managing complex Git operations.

10. [Datagrip](https://www.jetbrains.com/datagrip/) - A database management environment developed by JetBrains, designed to provide a better workflow for managing databases with advanced code insights, efficient schema navigation, and running queries.

11. [Figma](https://www.figma.com/) - An interface design application used for UI/UX design, allowing for the experimentation with design elements such as colors and layouts to create visual mockups.

12. [Shields.io](https://shields.io/) - A service used to create badges for README files, enhancing the documentation with visual indicators of project status, license, and other metrics.

13. [TinyPNG](https://tinypng.com/) - An online service used for compressing PNG and JPEG images to reduce file size without losing much quality, optimizing web performance.

14. [Midjourney](https://www.midjourney.com/) - I utilized Midjourney to generate all the website images. By incorporating specific keywords, I ensured that the images were produced in a consistent art style for a cohesive visual design. With my paid account plan, I have the right to use these generated images for my project, in line with Midjourney's [terms of service](https://docs.midjourney.com/docs/terms-of-service).

15. [Heroku](https://heroku.com/) - A platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud, used for deploying the website.

16. [DrawSQL](https://drawsql.app/) - An online tool for designing and visualizing database schemas through Entity-Relationship Diagrams (ERD), helping to conceptualize and communicate the database structure.

17. [Stripe API](https://stripe.com/) - The Stripe API was used to securely process credit card payments.

18. [Django Tailwind](https://github.com/timonweb/django-tailwind) - A Django application that integrates Tailwind CSS into Django projects, simplifying the process of using Tailwind CSS in Django templates.

19. [Django Widget Tweaks](https://github.com/jazzband/django-widget-tweaks) - A Django app for customizing form field rendering in templates, allowing for easy manipulation of form fields in Django templates.

20. [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - The Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2.

21. [Django Storages](https://django-storages.readthedocs.io/en/latest/) - A collection of custom storage backends for Django, facilitating the integration of storage solutions such as Amazon S3.

22. [Django Countries](https://pypi.org/project/django-countries/) - A Django app that provides country choices for use with forms, flag icons, and country data.

23. [Gunicorn](https://gunicorn.org) - A Python WSGI HTTP Server for UNIX, used as a web server gateway interface that allows Django applications to communicate with web servers.

24. [Pillow](https://python-pillow.org/) - The Python Imaging Library adds image processing capabilities to your Python interpreter, enabling image opening, manipulation, and saving across a wide variety of formats.

25. [Dj Database URL](https://pypi.org/project/dj-database-url/) - A Django utility that allows you to utilize the `DATABASE_URL` environment variable to configure your Django application's database settings, simplifying database configuration.

26. [Python Decouple](https://pypi.org/project/python-decouple/) - A utility that helps to separate settings from code, enabling the easy management of environment variables and configuration.

27. [Psycopg2](https://www.psycopg.org/) - A PostgreSQL database adapter for the Python programming language, facilitating connection and interaction with PostgreSQL from Python.

<br />

## Deployment & Local Development

#### Local Development

1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. (Optional): Set up a virtual environment in the project folder using `python3 -m venv [virtual_environment_name]`
5. (Optional): To activate the virtual environment, on Windows run `myvenv\Scripts\activate` and on macOS and Linux, run `source myvenv/bin/activate`
6. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
7. **Note**: The project is set up to use environment variables. You will need to set these up in your local environment. See [Environment Variables](#environment-variables) for more information.
8. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
9. (Optional): To populate the database with initial store data, you can run a custom Django command I created by typing `python manage.py initialise_store_data` into the terminal. This will wipe any previous data and populate it with all of the shoe product fixture files. In addition, it will generate a random number of stock levels for each shoe and corresponding size. Note that running this script can take some time to complete. Both the fixture files and the management command are in the products app.
10. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.
11. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.
12. To get Tailwind CSS working, you need to start the build process so it can scan your classes and update its output in the `styles.css` file. To do this, open a new terminal window and type `python manage.py tailwind start`. This command uses the [Django Tailwind](https://github.com/timonweb/django-tailwind) package to integrate Tailwind CSS with your Django project.

#### Heroku Deployment

1. Ensure the project repository has been uploaded to Github.
1. Login to the Heroku dashboard and create a new app.
1. Connect your GitHub repository to your Heroku app.
1. In the Settings tab, ensure that the Python Buildpack is added.
1. Set environment variables in the Config Vars section of the Settings tab.
1. In the Deploy tab, enable automatic deploys from your GitHub repository.
1. Click the "Deploy Branch" button to deploy the app.
1. Once the app has been deployed, click the "Open App" button to view the app.

#### Environment Variables

- For local deployment, you will need to create a .env file in the root directory of the project and set the environment variables in this file.

- **Note**: Ensure the .env file is included in the .gitignore file to exclude it from your GitHub repo to prevent the environment variables from being publicly exposed.

- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.
- You need to define the following environment variables:

  - `SECRET_KEY`: The secret key for your Django project. This is a critical setting that's used for cryptographic signing, and should be kept secret at all times. It's used to provide cryptographic signing and should be a long, random string of bytes.

  - `ENVIRONMENT`: The environment in which your Django project is running. Typical values are `development`, `staging`, or `production`.

  - `DEBUG`: A boolean that turns on/off debug mode. Set to `True` for development to enable detailed error pages and logging for debugging. Set to `False` in production to improve performance and security.

  - `DATABASE_URL`: The URL for your database. This should include the database engine, username, password, host, port, and database name. For a Postgres database, it typically looks like `postgres://USER:PASSWORD@HOST:PORT/DB_NAME`.

  - `STRIPE_PUBLIC_KEY`: The Stripe public key, used to identify your account with Stripe.

  - `STRIPE_SECRET_KEY`: The Stripe secret key, used for API calls to Stripe.

  - `STRIPE_WEBHOOK_SECRET`: The Stripe webhook secret, used to validate webhook events.

  - `AWS_ACCESS_KEY_ID`: The AWS access key ID, used to authenticate with AWS services.

  - `AWS_S3_CUSTOM_DOMAIN`: The custom domain for the S3 bucket.

  - `AWS_SECRET_ACCESS_KEY`: The AWS secret access key, used to authenticate with AWS services.

  - `AWS_STORAGE_BUCKET_NAME`: The name of the S3 bucket, used for storing static and media files.

<br />

## Testing

[Link to TESTING.md](TESTING.md)

## Credits

### Code Used And Tutorials

- [Code Institute: Boutique Ado](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentecomm) - This series from Code Institute served as a solid introduction to building an eCommerce store using Django. Certain pieces of code were used to help build parts of the database schema and the functionality for parts of the application, such as the shopping cart and checkout.

- [Udemy: Python Django - The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide/) - This course helped me dive deeper into Django, covering many aspects of the framework in greater detail.

- [Very Academy: Ajax Like Feature](https://www.youtube.com/watch?v=GxA2I-n8NR8&list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT) - In helping to build out the wishlist functionality, I used this tutorial from Very Academy to help build the logic for making Ajax requests to Django so that the wishlist could be updated without triggering a page reload.

- [Django Documentation: Custom Template Tags and Filters](https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/) - I used this to help build a simple custom template tag for returning a range object that represents a sequence of numbers from 0 up to a specified value, which was used for my ratings feature.

- [Django Documentation: Data Fixtures](https://docs.djangoproject.com/en/4.2/howto/initial-data/) - To efficiently populate my database with data, I learned about fixtures, how they work, and how they can be loaded into a database from this section of the Django documentation.

- [Very Academy: Custom Commands](https://www.youtube.com/watch?v=pbq5GQUX1Pk) - I used this guide to learn more about Django custom commands. I created my own command called `initialise_store_data.py` to help automate the process of initializing the store data with products and randomly assigning stock levels to each shoe and size to simulate the inventory of a real online store.

- [Colt Steele's Git and GitHub Course](https://www.udemy.com/course/git-and-github-bootcamp/) - As my project grew, maintaining a clear and secure git history became paramount. The chapter on using interactive rebase was instrumental in enabling me to clean up and refactor earlier commits to ensure the necessary changes were grouped together logically in my git history.

### Media

- [Material Design Icons](https://m3.material.io/styles/icons/overview) - This was the icon set I used for all icons across the website.
- [Midjourney](https://www.midjourney.com/) - All images were generated with the usage of Midjourney.

### Acknowledgments

- My Mentor [Lauren-Nicole](https://github.com/CluelessBiker) - who offered excellent advice, provided solid feedback, and supported me during my work on this project.

- The Code Institute Community - Both my class and the community have been invaluable. Having access to a wonderful group of people who share my passion for coding has significantly aided my journey in coding thus far.

- To you, dear reader, for taking the time to read my documentation. Have a cookie! 🍪

<br/>

[Back to Top ^](#introduction)
