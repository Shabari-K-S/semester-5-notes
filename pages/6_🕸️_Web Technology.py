import streamlit as st 
from streamlit_option_menu import option_menu

st. set_page_config(layout="wide")

st.title("Web Technology")

st.write("###")
# List of video URLs
video_urls = {
    "Internet History":"https://www.youtube.com/watch?v=Oh93xiKv-Jg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&ab_channel=Education4u",
    "Internet services":"https://www.youtube.com/watch?v=72z8C9WM8x0&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=2&ab_channel=Education4u",
    "World Wide Web(WWW)":"https://www.youtube.com/watch?v=yoJPysX1xzU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=3&ab_channel=Education4u",
    "HTML tutorial":"https://www.youtube.com/watch?v=4bg2AUp6Y8w&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=4&ab_channel=Education4u",
    "HTML tags - 1":"https://www.youtube.com/watch?v=GMun4-g5Y6E&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=5&ab_channel=Education4u",
    "HTML tags - 2":"https://www.youtube.com/watch?v=rTYhLG7PgCM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=6&ab_channel=Education4u",
    "HTML tags - 3":"https://www.youtube.com/watch?v=iO2X3D9jFfM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=7&ab_channel=Education4u",
    "HTML Tables":"https://www.youtube.com/watch?v=A3NIKULhZls&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=8&ab_channel=Education4u",
    "Anchor and Image":"https://www.youtube.com/watch?v=cJ7CM8rvqgU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=9&ab_channel=Education4u",
    "Frames":"https://www.youtube.com/watch?v=A1XlIDDXgwg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=10&ab_channel=Education4u",
    "Forms":"https://www.youtube.com/watch?v=4zj9OAHxb5E&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=11&ab_channel=Education4u",
    "Form Attributes":"https://www.youtube.com/watch?v=LfYIwJN2n-I&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=12&ab_channel=Education4u",
    "CSS" :"https://www.youtube.com/watch?v=kk_pfNxU1AM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=13&ab_channel=Education4u",
    "Internal CSS":"https://www.youtube.com/watch?v=kk_pfNxU1AM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=13&ab_channel=Education4u",
    "External CSS - 1":"https://www.youtube.com/watch?v=kk_pfNxU1AM&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=13&ab_channel=Education4u",
    "External CSS - 2":"https://www.youtube.com/watch?v=VEZ7CT6w4FY&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=16&ab_channel=Education4u",
    "Inline CSS":"https://www.youtube.com/watch?v=tXdf6MPGPpk&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=17&ab_channel=Education4u",
    "CSS Box Model":"https://www.youtube.com/watch?v=70zTtCEaCG8&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=18&ab_channel=Education4u",
    "CSS List":"https://www.youtube.com/watch?v=kJaJNjNzjqc&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=19&ab_channel=Education4u",
    "DHTML":"https://www.youtube.com/watch?v=a-_SKo17FKA&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=20&ab_channel=Education4u",
    "XML":"https://www.youtube.com/watch?v=pCmPduLzD0k&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=21&ab_channel=Education4u",
    "Declaration and Doc":"https://www.youtube.com/watch?v=iLC12EinND0&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=22&ab_channel=Education4u",
    "WML":"https://www.youtube.com/watch?v=sN1usZH00C4&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=23&ab_channel=Education4u",
    "Javascript":"https://www.youtube.com/watch?v=J2q0x70YDPk&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=24&ab_channel=Education4u",
    "Javascript syntax":"https://www.youtube.com/watch?v=YGOhbWBcOPE&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=25&ab_channel=Education4u",
    "Implementing JS":"https://www.youtube.com/watch?v=Ia09ZN2-_e8&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=26&ab_channel=Education4u",
    "Variables and Scope":"https://www.youtube.com/watch?v=DwWtu7VLTwg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=27&ab_channel=Education4u",
    "JS functions":"https://www.youtube.com/watch?v=rmvnFH_obhE&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=28&ab_channel=Education4u",
    "JS Array - 1":"https://www.youtube.com/watch?v=nyhRPNOE1X8&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=29&ab_channel=Education4u",
    "JS Array - 2":"https://www.youtube.com/watch?v=XMY5j-ZE238&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=30&ab_channel=Education4u",
    "JS Object - 1":"https://www.youtube.com/watch?v=1YEJS1mMMhA&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=31&ab_channel=Education4u",
    "JS Object - 2":"https://www.youtube.com/watch?v=JMHRlvrAa1A&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=32&ab_channel=Education4u",
    "Built-in JS functions":"https://www.youtube.com/watch?v=LBKNGrPNZSE&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=33&ab_channel=Education4u",
    "JS Event Handling":"https://www.youtube.com/watch?v=2vKBqzl6zAU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=34&ab_channel=Education4u",
    "Java Servlet":"https://www.youtube.com/watch?v=UoG9kH5BoBY&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=35&ab_channel=Education4u",
    "Servlet Architecture":"https://www.youtube.com/watch?v=Dt9zvPeRPjU&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=36&ab_channel=Education4u",
    "Life Cycle Of Servlet":"https://www.youtube.com/watch?v=SpOWu3NHFIw&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=37&ab_channel=Education4u",
    "Parameter Data - 1":"https://www.youtube.com/watch?v=t4w71DCNuVw&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=38&ab_channel=Education4u",
    "Parameter Data - 2":"https://www.youtube.com/watch?v=wq7pRoKUV1o&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=39&ab_channel=Education4u",
    "Session Tracking":"https://www.youtube.com/watch?v=5SIJnF7hqak&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=40&ab_channel=Education4u",
    "Cookies - 1":"https://www.youtube.com/watch?v=_w2TYBy_7L0&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=41&ab_channel=Education4u",
    "Cookies - 2":"https://www.youtube.com/watch?v=BgEcYGXEklI&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=42&ab_channel=Education4u",
    "Servlet and Concurrency":"https://www.youtube.com/watch?v=p2vPH8Babbg&list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp&index=44&ab_channel=Education4u",
    # Add more video URLs as needed
}

links = list(video_urls.keys())
tab1,tab2 = st.tabs(["Video","Notes"])

with tab1:
  c1,c2 = st.columns([7,3])

  title = "Web Technology"
  # Sidebar to display video list
  with c2:
      selected_video_index = option_menu(title, links,default_index=0)

  with c1:
      st.video(video_urls[selected_video_index])


with tab2:
  st.header("Notes")
  st.write("---")
  st.header("Unit - 1")
  st.write("---")

  st.markdown(
  """
### 1. HTML Tages and Elements

HTML (Hypertext Markup Language) is the standard language used to create and design webpages. HTML consists of various tags and elements that structure the content on a webpage. Here are some fundamental HTML tags and elements:

1. **<!DOCTYPE html>:** Declares the HTML version being used (HTML5 in most modern cases).

2. **<html>:** The root element of an HTML page.

3. **<head>:** Contains meta-information about the HTML document, such as title, links to stylesheets, and scripts.

4. **<title>:** Sets the title of the HTML document, which appears in the browser's title bar or tab.

5. **<body>:** Contains the content of the HTML document, including text, images, links, and other elements.

6. **<h1>, <h2>, <h3>, ..., <h6>:** Define header levels, where `<h1>` is the highest and `<h6>` is the lowest.

7. **<p>:** Represents a paragraph of text.

8. **<a>:** Creates hyperlinks to other web pages or resources.

9. **<img>:** Embeds images in the document.

10. **<ul>, <ol>, <li>:** Used for creating unordered (bulleted) and ordered (numbered) lists.

11. **<div>:** A generic container element used for grouping other HTML elements and applying styles.

12. **<span>:** Similar to `<div>`, but for inline elements. It is often used to apply styles to a specific portion of text.

13. **<br>:** Represents a line break.

14. **<hr>:** Creates a horizontal line to separate content.

15. **<strong>:** Represents strong importance or emphasis (usually displayed as bold).

16. **<em>:** Represents emphasized text (usually displayed as italic).

17. **<a href="URL">...</a>:** Defines a hyperlink. The "href" attribute contains the URL to which the link points.

18. **<input>:** Used for various form elements like text boxes, checkboxes, radio buttons, etc.

19. **<form>:** Defines an HTML form for user input.

20. **<table>:** Defines an HTML table for organizing data into rows and columns.

These are just a few examples of HTML tags and elements. HTML provides a variety of tags to structure content, create links, and define the layout and appearance of a webpage. Each tag serves a specific purpose and can be combined to create complex and interactive web pages.
  """
  )

  st.markdown(
  """
---

###  2. CSS3 -Inline, embedded and external style sheets 

CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML. CSS3 is the latest version of CSS, introducing new features and improvements. There are three ways to apply CSS styles to HTML documents: Inline styles, Embedded styles, and External styles.

### 1. Inline Styles:

Inline styles are applied directly to individual HTML elements using the "style" attribute. This method is useful for applying unique styles to a specific element.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Inline Styles Example</title>
</head>
<body>
  <h1 style="color: blue; text-align: center;">This is a Heading</h1>
  <p style="font-size: 16px; color: green;">This is a paragraph with inline styles.</p>
</body>
</html>
```

In this example, the styles (color, text-align, font-size) are applied directly to the `<h1>` and `<p>` elements using the "style" attribute.

### 2. Embedded Styles:

Embedded styles are defined within the HTML document using the `<style>` tag in the head section. This allows you to apply styles to multiple elements on the same page.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Embedded Styles Example</title>
  <style>
    h1 {
      color: blue;
      text-align: center;
    }

    p {
      font-size: 16px;
      color: green;
    }
  </style>
</head>
<body>
  <h1>This is a Heading</h1>
  <p>This is a paragraph with embedded styles.</p>
</body>
</html>
```

In this example, the styles for `<h1>` and `<p>` are defined within the `<style>` tag in the head section, allowing you to apply consistent styles across multiple elements.

### 3. External Styles:

External styles involve placing the CSS code in a separate file with a `.css` extension and linking it to the HTML document using the `<link>` tag. This method is useful for applying styles consistently across multiple pages.

**styles.css:**
```css
/* styles.css */
h1 {
  color: blue;
  text-align: center;
}

p {
  font-size: 16px;
  color: green;
}
```

**index.html:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>External Styles Example</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <h1>This is a Heading</h1>
  <p>This is a paragraph with external styles.</p>
</body>
</html>
```

In this example, the CSS styles are saved in a separate file (`styles.css`) and linked to the HTML document using the `<link>` tag. This method allows for easy maintenance and consistent styling across multiple pages.
  """
  )

  st.markdown(
  """
---
### 3. Transformations – Transitions – Animations. Bootstrap Framework

Bootstrap is a popular front-end framework that simplifies the process of designing responsive and visually appealing websites. It includes a set of predefined styles, components, and JavaScript plugins to enhance the development workflow. Bootstrap also provides utilities for handling transformations, transitions, and animations.

### Transformations:

Bootstrap includes utility classes for handling CSS transformations. These classes can be used to apply translation, rotation, scaling, and skewing to elements. Here's an example of using Bootstrap's transformation classes:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <title>Bootstrap Transformations Example</title>
</head>
<body>

<div class="container mt-5">
  <div class="row">
    <div class="col-md-4">
      <div class="card">
        <img src="image.jpg" class="card-img-top img-fluid" alt="Image">
        <div class="card-body">
          <h5 class="card-title">Card Title</h5>
          <p class="card-text">Some example text.</p>
          <a href="#" class="btn btn-primary">Read More</a>
        </div>
      </div>
    </div>
  </div>
</div>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</body>
</html>
```

In this example, the Bootstrap classes `img-fluid` and `card` are used to create a responsive image and a card component. Bootstrap's utility classes for transformations are applied implicitly when needed for responsiveness.

### Transitions:

Bootstrap does not provide specific utility classes for transitions, but you can use custom CSS to apply transitions. Here's a simple example:

```html
<style>
  .my-transition {
    transition: all 0.3s ease;
  }

  .my-transition:hover {
    transform: scale(1.1);
    opacity: 0.8;
  }
</style>

<div class="container mt-5">
  <div class="row">
    <div class="col-md-4">
      <div class="card my-transition">
        <img src="image.jpg" class="card-img-top img-fluid" alt="Image">
        <div class="card-body">
          <h5 class="card-title">Card Title</h5>
          <p class="card-text">Some example text.</p>
          <a href="#" class="btn btn-primary">Read More</a>
        </div>
      </div>
    </div>
  </div>
</div>
```

In this example, the `.my-transition` class is used to define a transition on hover. The `:hover` pseudo-class is then used to specify the styles that should be applied during the hover state.

### Animations:

Bootstrap also includes some predefined CSS animations that you can use. For example, you can use the `animated` class along with other animation classes like `fadeIn`, `bounce`, etc.:

```html
<div class="container mt-5">
  <div class="row">
    <div class="col-md-4">
      <div class="card animated fadeIn">
        <img src="image.jpg" class="card-img-top img-fluid" alt="Image">
        <div class="card-body">
          <h5 class="card-title">Card Title</h5>
          <p class="card-text">Some example text.</p>
          <a href="#" class="btn btn-primary">Read More</a>
        </div>
      </div>
    </div>
  </div>
</div>
```

In this example, the `animated` class is combined with `fadeIn` to create a fade-in animation when the card is displayed.

Remember to include the Bootstrap CSS and JavaScript files in your project to leverage the full capabilities of the framework.
  """
  )

  st.write("---")
  st.header("Unit - 2")
  st.write("---")

  st.markdown(
  """
### 1. JavaScript DOM Model

The JavaScript Document Object Model (DOM) is a programming interface for web documents. It represents the structure of an HTML document as a tree-like structure where each node corresponds to an element, attribute, or piece of text in the document. JavaScript can be used to manipulate the DOM, allowing dynamic modification of the content, structure, and style of a web page.

Here's a simple explanation of the JavaScript DOM model with an example:

### Example: Manipulating the DOM

Let's say we have the following HTML document:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DOM Example</title>
</head>
<body>

  <h1 id="main-heading">Hello, World!</h1>
  <p id="demo">This is a paragraph.</p>

  <script src="script.js"></script>
</body>
</html>
```

And the corresponding JavaScript file (`script.js`):

```javascript
// script.js

// Accessing an element by its ID
var mainHeading = document.getElementById("main-heading");

// Modifying the content of the element
mainHeading.innerHTML = "Hello, JavaScript!";

// Accessing an element by its ID
var demoParagraph = document.getElementById("demo");

// Changing the text content and style of the element
demoParagraph.textContent = "This paragraph has been modified using JavaScript.";
demoParagraph.style.color = "blue";
demoParagraph.style.fontSize = "18px";

// Creating a new element and appending it to the body
var newParagraph = document.createElement("p");
newParagraph.textContent = "This is a new paragraph created with JavaScript.";
document.body.appendChild(newParagraph);
```

In this example:

1. The JavaScript file is included at the end of the HTML body to ensure that the DOM has been fully loaded before the script runs.

2. The `document.getElementById` method is used to access HTML elements by their ID. In this case, we access the elements with IDs "main-heading" and "demo."

3. The `innerHTML` property is used to modify the content of the "main-heading" element.

4. The `textContent` property is used to change the text content of the "demo" paragraph, and the `style` property is used to modify its color and font size.

5. The `createElement` method is used to create a new paragraph element (`<p>`), and the `appendChild` method is used to append it to the body of the document.

When you open this HTML file in a web browser, the JavaScript code will dynamically modify the content and style of the page based on the interactions with the DOM.
  """
  )

  st.markdown(
  """
  ---
### 2. xception Handling

Exception handling in programming is a mechanism that allows you to gracefully handle errors or exceptional situations that may occur during the execution of a program. In JavaScript, exception handling is done using the `try`, `catch`, `finally`, and `throw` statements.

Here's an example of exception handling in JavaScript:

```javascript
// Example function that throws an exception
function divideNumbers(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

// Example of using try, catch, and finally
try {
  var result = divideNumbers(10, 2);
  console.log("Result:", result);

  // This will throw an exception
  var zeroResult = divideNumbers(5, 0);
  console.log("This line will not be executed");
} catch (error) {
  console.error("Error:", error.message);
} finally {
  console.log("This block will be executed regardless of whether an exception occurs or not.");
}

// This line will be executed despite the exception in the try block
console.log("Program continues after the exception handling block.");
```

Explanation of the example:

1. The `divideNumbers` function takes two parameters (`a` and `b`) and attempts to divide `a` by `b`. If `b` is zero, it throws a custom error using the `throw` statement.

2. The `try` block contains the code that may potentially throw an exception. In this example, the first call to `divideNumbers` inside the `try` block is successful, while the second call results in an exception.

3. The `catch` block is executed if an exception occurs in the `try` block. It catches the exception and allows you to handle it gracefully. In this example, it logs the error message to the console.

4. The `finally` block is optional and is executed regardless of whether an exception occurs or not. It is often used for cleanup or finalization tasks.

5. The program continues to execute after the exception handling block.

Output:
```
Result: 5
Error: Cannot divide by zero
This block will be executed regardless of whether an exception occurs or not.
Program continues after the exception handling block.
```

In this example, the `try` block is used to encapsulate code that might throw an exception. If an exception occurs, the `catch` block is executed to handle the error. The `finally` block is then executed regardless of whether an exception occurred or not. This helps ensure that certain actions, such as cleanup, are performed even in the presence of exceptions.
  """
  )

  st.markdown(
  """
---
### 3.Form Validatio in HTML

Form validation in HTML is a crucial aspect of creating interactive and user-friendly web forms. HTML5 introduced various attributes and features that support client-side form validation. Here's an example of form validation using HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Form Validation Example</title>
  <style>
    .error {
      color: red;
    }
  </style>
</head>
<body>

  <h2>Registration Form</h2>
  
  <form id="registrationForm" onsubmit="return validateForm()">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <span id="usernameError" class="error"></span><br>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <span id="emailError" class="error"></span><br>
    
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <span id="passwordError" class="error"></span><br>
    
    <input type="submit" value="Register">
  </form>

  <script>
    function validateForm() {
      var username = document.getElementById("username").value;
      var email = document.getElementById("email").value;
      var password = document.getElementById("password").value;

      // Reset error messages
      document.getElementById("usernameError").innerHTML = "";
      document.getElementById("emailError").innerHTML = "";
      document.getElementById("passwordError").innerHTML = "";

      // Validate username
      if (username.length < 5) {
        document.getElementById("usernameError").innerHTML = "Username must be at least 5 characters.";
        return false;
      }

      // Validate email
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        document.getElementById("emailError").innerHTML = "Invalid email format.";
        return false;
      }

      // Validate password
      if (password.length < 8) {
        document.getElementById("passwordError").innerHTML = "Password must be at least 8 characters.";
        return false;
      }

      // Form is valid
      alert("Registration successful!");
      return true;
    }
  </script>

</body>
</html>
```

Explanation of the example:

1. The form includes three input fields for username, email, and password, each with a corresponding `<span>` element to display error messages.

2. The `required` attribute is used on each input field to ensure that the user provides a value.

3. The `onsubmit` attribute of the form tag is set to call the `validateForm` function when the form is submitted.

4. The `validateForm` function retrieves the values of the input fields and performs validation checks.

5. If any validation check fails, an error message is displayed next to the corresponding input field, and the function returns `false` to prevent the form from submitting.

6. If all validation checks pass, an alert is shown, and the function returns `true`, allowing the form to be submitted.

This is a basic example of client-side form validation in HTML using JavaScript. Keep in mind that client-side validation is not sufficient for security purposes, and server-side validation should also be implemented to ensure the integrity of the data submitted.
  """
  )

  st.markdown(
  """
---
### 4. Built-in objects

Built-in objects in JavaScript provide a range of functionalities and are available globally in any JavaScript environment. These objects are part of the JavaScript language specification and do not need to be explicitly created. Here are some common built-in objects in JavaScript, along with examples:

### 1. **Object:**
  The base object in JavaScript.

  ```javascript
  var person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
  };
  ```

### 2. **Array:**
  Used for creating and manipulating arrays.

  ```javascript
  var colors = ["red", "green", "blue"];
  ```

### 3. **String:**
  Provides methods for working with strings.

  ```javascript
  var message = "Hello, World!";
  console.log(message.length); // Outputs: 13
  ```

### 4. **Number:**
  Provides methods for working with numbers.

  ```javascript
  var pi = 3.14159;
  console.log(pi.toFixed(2)); // Outputs: 3.14
  ```

### 5. **Boolean:**
  Represents a Boolean value (`true` or `false`).

  ```javascript
  var isTrue = true;
  ```

### 6. **Function:**
  Used for creating functions.

  ```javascript
  function greet(name) {
    console.log("Hello, " + name + "!");
  }
  ```

### 7. **Date:**
  Represents dates and times.

  ```javascript
  var today = new Date();
  console.log(today.toDateString());
  ```

### 8. **Math:**
  Provides mathematical functions and constants.

  ```javascript
  var result = Math.sqrt(25);
  console.log(result); // Outputs: 5
  ```

### 9. **RegExp:**
  Represents regular expressions.

  ```javascript
  var pattern = /\d+/; // Matches one or more digits
  ```

### 10. **Error:**
  Represents an error object.

  ```javascript
  try {
    // Some code that may throw an error
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
  ```

### Example combining several built-in objects:

```javascript
// Creating an array of objects
var people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 },
  { name: "Bob", age: 40 }
];

// Iterating through the array and displaying information
people.forEach(function(person) {
  console.log(person.name + " is " + person.age + " years old.");
});

// Using the Math object to calculate the average age
var totalAge = people.reduce(function(sum, person) {
  return sum + person.age;
}, 0);

var averageAge = totalAge / people.length;
console.log("Average age: " + averageAge.toFixed(2));
```

In this example, we have an array of objects representing people. We use the Array, Object, and Math built-in objects to manipulate and display information about the people, including calculating the average age.
  """
  )

  st.markdown(
"""
---
### 5. Event Handling

It seems there might be a little confusion in your question. Java and JavaScript are two different programming languages, and they have different approaches to event handling.

If you are referring to event handling in **Java (for desktop applications, not web development):**

In Java, event handling is typically done using the Swing library or JavaFX for graphical user interfaces. Here's a brief overview:

1. **Swing Event Handling:**
   ```java
   import javax.swing.*;
   import java.awt.event.ActionEvent;
   import java.awt.event.ActionListener;

   public class MyFrame extends JFrame {
       private JButton myButton;

       public MyFrame() {
           myButton = new JButton("Click Me");
           myButton.addActionListener(new ActionListener() {
               @Override
               public void actionPerformed(ActionEvent e) {
                   // Handle button click event
                   JOptionPane.showMessageDialog(MyFrame.this, "Button Clicked!");
               }
           });

           getContentPane().add(myButton);
           setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
           setSize(300, 200);
           setLocationRelativeTo(null);
           setVisible(true);
       }

       public static void main(String[] args) {
           SwingUtilities.invokeLater(new Runnable() {
               @Override
               public void run() {
                   new MyFrame();
               }
           });
       }
   }
   ```

2. **JavaFX Event Handling:**
   ```java
   import javafx.application.Application;
   import javafx.event.ActionEvent;
   import javafx.event.EventHandler;
   import javafx.scene.Scene;
   import javafx.scene.control.Button;
   import javafx.scene.layout.StackPane;
   import javafx.stage.Stage;

   public class MyJavaFXApp extends Application {
       public static void main(String[] args) {
           launch(args);
       }

       @Override
       public void start(Stage primaryStage) {
           primaryStage.setTitle("JavaFX Button Example");

           Button myButton = new Button("Click Me");
           myButton.setOnAction(new EventHandler<ActionEvent>() {
               @Override
               public void handle(ActionEvent event) {
                   // Handle button click event
                   System.out.println("Button Clicked!");
               }
           });

           StackPane root = new StackPane();
           root.getChildren().add(myButton);
           primaryStage.setScene(new Scene(root, 300, 200));
           primaryStage.show();
       }
   }
   ```

If you are referring to event handling in **JavaScript (for web development):**

In web development, JavaScript is used for event handling. Here's a simple example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Event Handling</title>
</head>
<body>

    <button id="myButton">Click Me</button>

    <script>
        // Get the button element by its id
        var button = document.getElementById("myButton");

        // Add an event listener for the "click" event
        button.addEventListener("click", function() {
            // Handle button click event
            alert("Button Clicked!");
        });
    </script>

</body>
</html>
```

In this JavaScript example, an event listener is added to a button element. When the button is clicked, the specified function is executed.

If you can provide more details or clarify your question, I'd be happy to offer more specific information!
"""
  )

  st.markdown(
    """
    ---
    ### 6. JSON introduction , Syntax

    JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is often used to transmit data between a server and a web application, as well as to store and exchange data. JSON is language-independent, meaning it can be used with various programming languages.

### JSON Syntax:

JSON data is represented as key-value pairs, similar to objects in many programming languages. The basic syntax includes objects, arrays, strings, numbers, booleans, and null. Here's a quick breakdown:

1. **Objects:**
   - An object is an unordered collection of key-value pairs enclosed in curly braces `{}`.
   - Keys and values are separated by a colon `:`. Key-value pairs are separated by commas `,`.
   - Example:
     ```json
     {
       "name": "John Doe",
       "age": 30,
       "isStudent": false,
       "grades": [90, 85, 92]
     }
     ```

2. **Arrays:**
   - An array is an ordered collection of values enclosed in square brackets `[]`.
   - Example:
     ```json
     ["apple", "banana", "orange"]
     ```

3. **Strings:**
   - A string is a sequence of characters enclosed in double quotes `" "` or single quotes `' '`.
   - Example:
     ```json
     "Hello, World!"
     ```

4. **Numbers:**
   - A number can be an integer or a floating-point number.
   - Example:
     ```json
     42
     ```

5. **Booleans:**
   - Represents either `true` or `false`.
   - Example:
     ```json
     true
     ```

6. **Null:**
   - Represents a null value.
   - Example:
     ```json
     null
     ```

### JSON Example:

```json
{
  "person": {
    "firstName": "Alice",
    "lastName": "Smith",
    "age": 28,
    "isStudent": false,
    "address": {
      "city": "New York",
      "zipCode": "10001"
    },
    "hobbies": ["reading", "traveling"]
  },
  "employees": [
    {
      "id": 1,
      "name": "John",
      "position": "Developer"
    },
    {
      "id": 2,
      "name": "Jane",
      "position": "Designer"
    }
  ],
  "status": true
}
```

In this example:

- There's an object named "person" with various key-value pairs, including nested objects ("address") and an array of hobbies.
- There's an array named "employees" containing objects with information about different employees.
- There's a boolean value "status" set to `true`.

JSON is commonly used in web development for data exchange between a server and a client, and it has become a standard format for APIs (Application Programming Interfaces). When exchanging data between a web server and a web client, the server often sends data to the client in JSON format, which the client can then parse and use in its application.
    """
  )

  st.write("---")
  st.header("Unit - 3")
  st.write("---")
  st.markdown(
    """
    ### 1. Servlet concept and cookies

    Servlets are Java-based server-side components used for building web applications. They extend the capabilities of servers to generate dynamic content and handle requests from clients. Let's explore the concepts of servlets and cookies in Java.

### Servlet Concepts:

1. **Servlet Lifecycle:**
   - Initialization: Servlet container loads the servlet.
   - Service: Servlet handles client requests using `service()` method.
   - Destruction: Servlet container unloads the servlet.

2. **Servlet Mapping:**
   - Servlets are mapped to specific URL patterns in the deployment descriptor (`web.xml` or annotations).

3. **Request and Response:**
   - Servlets process incoming requests (`HttpServletRequest`) and generate responses (`HttpServletResponse`).

4. **Session Management:**
   - Servlets can maintain session information using HttpSession.

### Servlet Example:

Let's create a simple servlet that handles a GET request and returns a basic HTML response:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/HelloServlet")
public class HelloServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        out.println("<h2>Hello, Servlet!</h2>");
        out.println("</body></html>");
    }
}
```

In this example:
- The `doGet` method handles HTTP GET requests.
- The `response` object is used to send an HTML response to the client.

### Cookies:

Cookies are small pieces of data sent by a server to a client's browser. They are stored on the client's machine and sent back to the server with subsequent requests. Cookies are commonly used for session management, user tracking, and personalization.

### Cookie Example:

Let's modify the servlet to set a cookie and display its value:

```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/HelloServlet")
public class HelloServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        // Creating a cookie named "user" with a value
        Cookie userCookie = new Cookie("user", "John");
        userCookie.setMaxAge(3600); // Cookie will expire in 1 hour
        response.addCookie(userCookie);

        out.println("<html><body>");
        out.println("<h2>Hello, Servlet!</h2>");
        out.println("<p>Cookie set: user=John</p>");
        out.println("</body></html>");
    }
}
```

In this example:
- We create a `Cookie` named "user" with a value of "John" and set its maximum age.
- The cookie is added to the response using `response.addCookie()`.

This is a simple example of setting a cookie. In a real-world scenario, cookies are often used for more complex tasks, such as session management, user authentication, and storing user preferences.
    
    """ 
  )

  st.markdown(
    """
    ---
    ### 2. Jdbc connectivity

    Java Database Connectivity (JDBC) is a Java-based API that allows Java applications to interact with relational databases. It provides a standardized way to connect to databases, execute SQL queries, and process the results. Below is an example of JDBC connectivity with a MySQL database.

### JDBC Connectivity Example:

Assuming you have a MySQL database named "testdb" with a table named "users" having columns `id`, `username`, and `email`. Here's how you can connect to the database and retrieve data using JDBC:

1. **Download and include the MySQL Connector/J JAR:**
   - Download the MySQL Connector/J JAR file from [MySQL official website](https://dev.mysql.com/downloads/connector/j/).
   - Add the downloaded JAR to your Java project.

2. **Java Code:**
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;
   import java.sql.PreparedStatement;
   import java.sql.ResultSet;
   import java.sql.SQLException;

   public class JdbcExample {
       // JDBC URL, username, and password of MySQL server
       private static final String JDBC_URL = "jdbc:mysql://localhost:3306/testdb";
       private static final String USERNAME = "your_username";
       private static final String PASSWORD = "your_password";

       public static void main(String[] args) {
           Connection connection = null;
           PreparedStatement preparedStatement = null;
           ResultSet resultSet = null;

           try {
               // Load the JDBC driver
               Class.forName("com.mysql.cj.jdbc.Driver");

               // Establish a connection
               connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

               // SQL query
               String sqlQuery = "SELECT id, username, email FROM users";

               // Create a PreparedStatement
               preparedStatement = connection.prepareStatement(sqlQuery);

               // Execute the query and retrieve the results
               resultSet = preparedStatement.executeQuery();

               // Process the results
               while (resultSet.next()) {
                   int id = resultSet.getInt("id");
                   String username = resultSet.getString("username");
                   String email = resultSet.getString("email");

                   System.out.println("ID: " + id + ", Username: " + username + ", Email: " + email);
               }
           } catch (ClassNotFoundException | SQLException e) {
               e.printStackTrace();
           } finally {
               // Close resources in reverse order of creation
               try {
                   if (resultSet != null) resultSet.close();
                   if (preparedStatement != null) preparedStatement.close();
                   if (connection != null) connection.close();
               } catch (SQLException e) {
                   e.printStackTrace();
               }
           }
       }
   }
   ```

3. **Note:**
   - Replace `"your_username"` and `"your_password"` with your MySQL username and password.
   - Make sure the MySQL server is running on `localhost` and listening on the default port `3306`.

This example demonstrates the basic steps for JDBC connectivity:

- Load the JDBC driver.
- Establish a connection to the database.
- Create and execute a SQL query using `PreparedStatement`.
- Process the results using a `ResultSet`.
- Close the resources (connection, statement, result set) to release database resources.

Remember to handle exceptions properly in a real-world scenario, and also consider using try-with-resources statement (available in Java 7 and later) for automatic resource management.
    """
  )


  st.write("---")
  st.header("Unit - 4")
  st.write("---")
  st.markdown(
    """
    ### 1. PHP Built in function

    PHP comes with a vast array of built-in functions that simplify various tasks, ranging from string manipulation to file handling, and much more. Here are some commonly used PHP built-in functions with examples:

### 1. **String Functions:**

- **strlen()**: Returns the length of a string.
  ```php
  $str = "Hello, World!";
  echo strlen($str); // Outputs: 13
  ```

- **strpos()**: Finds the position of the first occurrence of a substring in a string.
  ```php
  $str = "Hello, World!";
  echo strpos($str, "World"); // Outputs: 7
  ```

- **substr()**: Returns a part of a string.
  ```php
  $str = "Hello, World!";
  echo substr($str, 0, 5); // Outputs: Hello
  ```

### 2. **Array Functions:**

- **count()**: Returns the number of elements in an array.
  ```php
  $numbers = [1, 2, 3, 4, 5];
  echo count($numbers); // Outputs: 5
  ```

- **array_push()**: Pushes one or more elements onto the end of an array.
  ```php
  $fruits = ["apple", "banana"];
  array_push($fruits, "orange", "grape");
  print_r($fruits); // Outputs: Array ( [0] => apple [1] => banana [2] => orange [3] => grape )
  ```

- **array_pop()**: Pops the element off the end of the array.
  ```php
  $fruits = ["apple", "banana", "orange"];
  $lastFruit = array_pop($fruits);
  echo $lastFruit; // Outputs: orange
  ```

### 3. **File Handling Functions:**

- **file_get_contents()**: Reads the entire contents of a file into a string.
  ```php
  $content = file_get_contents("example.txt");
  echo $content;
  ```

- **file_put_contents()**: Writes data to a file.
  ```php
  $data = "Hello, File!";
  file_put_contents("example.txt", $data);
  ```

### 4. **Math Functions:**

- **rand()**: Generates a random integer.
  ```php
  $randomNumber = rand(1, 10);
  echo $randomNumber;
  ```

- **sqrt()**: Returns the square root of a number.
  ```php
  $number = 25;
  echo sqrt($number); // Outputs: 5
  ```

### 5. **Date and Time Functions:**

- **date()**: Formats a local time/date.
  ```php
  echo date("Y-m-d H:i:s"); // Outputs: Current date and time in YYYY-MM-DD HH:MM:SS format
  ```

- **strtotime()**: Parses any English textual datetime description into a Unix timestamp.
  ```php
  $timestamp = strtotime("next Saturday");
  echo date("Y-m-d", $timestamp); // Outputs: Next Saturday's date
  ```

These examples cover just a small subset of the extensive collection of PHP built-in functions. PHP's documentation provides comprehensive information on each function, including usage, parameters, and examples.
    """
  )

  st.markdown(
    """
    ---
    ### 2. Xml schema

    XML Schema, often referred to as XSD (XML Schema Definition), is a way to define the structure and constraints of XML documents. It provides a set of rules to specify the elements, attributes, and data types allowed in an XML document. XML Schema is commonly used to validate XML documents and ensure they conform to a predefined structure.

Here is an example of an XML Schema with a corresponding XML document:

### XML Schema (example.xsd):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <!-- Define the structure of the XML document -->
  <xs:element name="bookstore">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="book" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title" type="xs:string"/>
              <xs:element name="author" type="xs:string"/>
              <xs:element name="price" type="xs:decimal"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```

### XML Document (example.xml):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Introduction to XML</title>
    <author>John Doe</author>
    <price>29.99</price>
  </book>
  <book>
    <title>Web Development with HTML</title>
    <author>Jane Smith</author>
    <price>39.95</price>
  </book>
</bookstore>
```

In this example:

- The XML Schema (`example.xsd`) defines a bookstore element with a sequence of book elements. Each book has a title, author, and price.
- The XML Document (`example.xml`) adheres to the structure defined in the XML Schema.

Key components of the XML Schema:

- **`<xs:schema>`**: The root element that encapsulates the entire schema.
- **`<xs:element>`**: Defines an element in the XML document. It can have attributes like name, type, and minOccurs (minimum occurrences) or maxOccurs (maximum occurrences).
- **`<xs:complexType>`**: Describes the content model for an element, specifying the child elements and their order.
- **`<xs:sequence>`**: Ensures that the child elements appear in the specified sequence.

This XML Schema ensures that any XML document adhering to its structure will have a root element named "bookstore," containing one or more "book" elements, each with a "title," "author," and "price." The data types (`xs:string` and `xs:decimal`) provide additional constraints on the content of specific elements. When an XML document is validated against this schema, it must conform to these rules to be considered valid.
    """
  )

  st.markdown(
    """
    ---
    ### 3. Xml parser

    XML parsers are tools or libraries that parse (read and interpret) XML documents. They are commonly used in programming to extract data from XML and make it usable within an application. There are various XML parsers available for different programming languages. I'll provide an example using a common XML parser in the context of the PHP programming language.

### Example using PHP's SimpleXML Parser:

Consider the following XML document (`data.xml`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Introduction to XML</title>
    <author>John Doe</author>
    <price>29.99</price>
  </book>
  <book>
    <title>Web Development with HTML</title>
    <author>Jane Smith</author>
    <price>39.95</price>
  </book>
</bookstore>
```

Now, let's use PHP's SimpleXML parser to read and process this XML:

```php
<?php
// Load the XML file
$xml = simplexml_load_file('data.xml');

// Loop through each book element
foreach ($xml->book as $book) {
    // Access the data within each book
    $title = $book->title;
    $author = $book->author;
    $price = $book->price;

    // Display the information
    echo "Title: $title<br>";
    echo "Author: $author<br>";
    echo "Price: $price<br><br>";
}
?>
```

In this PHP example:

1. `simplexml_load_file('data.xml')` is used to load the XML file into a SimpleXML object. This object allows easy traversal and extraction of data from the XML document.

2. The `foreach` loop is used to iterate through each `<book>` element in the XML document.

3. Within the loop, we access the data within each `<book>` element using SimpleXML's object notation (`$book->title`, `$book->author`, `$book->price`).

4. The information is then displayed using `echo`.

When you run this PHP script, it will output:

```
Title: Introduction to XML
Author: John Doe
Price: 29.99

Title: Web Development with HTML
Author: Jane Smith
Price: 39.95
```

This is a basic example of using an XML parser to read and process XML data. Other programming languages have similar XML parsing libraries or modules, such as `ElementTree` in Python, `DOM` and `SAX` parsers in Java, and many more. The choice of parser may depend on the programming language and specific requirements of your application.
    """
  )

  st.write("---")
  st.header("Unit - 5")
  st.write("---")
  st.markdown(
    """
    ### 1. Mvc architecture

    Model-View-Controller (MVC) is a software design pattern commonly used for developing interactive and dynamic web applications. It separates an application into three interconnected components: the Model, the View, and the Controller. This separation of concerns helps in maintaining a clean and organized codebase.

Let's explore each component of the MVC architecture and provide an example in the context of a simple web application.

### 1. **Model:**

The Model represents the application's data and business logic. It is responsible for managing the data, validating it, and responding to requests for information about the state of the application.

**Example:**
```php
// Model class representing a simple user
class UserModel {
    private $username;
    private $email;

    public function __construct($username, $email) {
        $this->username = $username;
        $this->email = $email;
    }

    public function getUsername() {
        return $this->username;
    }

    public function getEmail() {
        return $this->email;
    }
}
```

### 2. **View:**

The View is responsible for presenting the data to the user and handling user interface logic. It receives data from the Model and generates the output that is displayed to the user.

**Example:**
```php
// View class for displaying user information
class UserView {
    public function render(UserModel $user) {
        echo "<p>Username: {$user->getUsername()}</p>";
        echo "<p>Email: {$user->getEmail()}</p>";
    }
}
```

### 3. **Controller:**

The Controller acts as an intermediary between the Model and the View. It receives user input, processes it (possibly updating the Model), and updates the View accordingly. It manages the flow of data between the Model and the View.

**Example:**
```php
// Controller class for managing user interactions
class UserController {
    private $model;
    private $view;

    public function __construct(UserModel $model, UserView $view) {
        $this->model = $model;
        $this->view = $view;
    }

    public function updateUserData($username, $email) {
        // Update the model with new user data
        $this->model = new UserModel($username, $email);

        // Render the updated user data in the view
        $this->view->render($this->model);
    }
}
```

### Example Usage:

```php
// Create a Model instance
$userModel = new UserModel("john_doe", "john@example.com");

// Create a View instance
$userView = new UserView();

// Create a Controller instance
$userController = new UserController($userModel, $userView);

// Initial rendering of user data
$userView->render($userModel);

// Update user data through the Controller
$userController->updateUserData("jane_smith", "jane@example.com");
```

In this example:

1. The `UserModel` represents a simple user with properties like username and email.
2. The `UserView` displays user information received from the Model.
3. The `UserController` manages the interaction between the Model and the View, updating the Model and triggering the View to render the updated data.

This MVC architecture separates concerns, making the code more modular, scalable, and easier to maintain. It also allows for code reusability and promotes the principle of "separation of concerns."
    """
  )

  st.markdown(
    """
    ---
    ### 2. angular,React, docker,direvtives 

    It looks like your question is asking about Angular, React, Docker, and directives. Let me provide a brief explanation and examples for each:

### 1. **Angular:**

Angular is a JavaScript framework developed and maintained by Google. It is used for building dynamic web applications. Angular provides a modular and structured way of building applications through components, services, and dependency injection.

**Example:**
```typescript
// Angular Component
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: '<h1>Hello, {{ name }}!</h1>',
})
export class AppComponent {
  name = 'Angular';
}
```

In this example, we have an Angular component that displays a greeting using data binding (`{{ name }}`).

### 2. **React:**

React is a JavaScript library for building user interfaces, developed and maintained by Facebook. It allows developers to build UI components that can efficiently update and render based on changes in data.

**Example:**
```jsx
// React Component
import React, { useState } from 'react';

function App() {
  const [name, setName] = useState('React');

  return (
    <div>
      <h1>Hello, {name}!</h1>
    </div>
  );
}

export default App;
```

In this React example, we use the `useState` hook to manage the component's state and update the UI dynamically.

### 3. **Docker:**

Docker is a platform for developing, shipping, and running applications in containers. Containers are lightweight, portable, and consistent environments that package an application and its dependencies.

**Example:**
```dockerfile
# Dockerfile
FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

This Dockerfile is for a Node.js application. It sets up the application's environment, installs dependencies, and defines how to run the application.

### 4. **Directives:**

Directives in the context of web development generally refer to instructions given to the browser in the form of HTML attributes. Both Angular and React use directives, but they are implemented differently.

**Angular Directive Example:**
```html
<!-- Angular Directive -->
<p *ngIf="isUserLoggedIn">Welcome, {{ username }}!</p>
```

In Angular, `*ngIf` is a structural directive that conditionally renders or removes an element based on the provided expression.

**React "Directive" Example:**
```jsx
// React Conditional Rendering
function Greeting({ isUserLoggedIn, username }) {
  return isUserLoggedIn ? <p>Welcome, {username}!</p> : null;
}
```

In React, conditional rendering is achieved through JavaScript expressions. The `Greeting` component renders a paragraph if `isUserLoggedIn` is `true`, otherwise, it renders `null`.

These examples provide a basic overview of Angular, React, Docker, and directives. Each technology has its own strengths and use cases, and the choice depends on the requirements of your project.
    """
  )