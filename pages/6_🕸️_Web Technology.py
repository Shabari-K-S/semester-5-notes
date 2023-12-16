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

c1,c2 = st.columns([7,3])

title = "Web Technology"
# Sidebar to display video list
with c2:
    selected_video_index = option_menu(title, links,default_index=0)

with c1:
    st.video(video_urls[selected_video_index])



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
### 4. 
"""
)