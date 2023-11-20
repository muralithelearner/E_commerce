
// script.js

function updatePlaceholder() {
    var contactInput = document.getElementById("contactInput");

    // Check if the input value matches an email pattern
    if (/^\S+@\S+\.\S+$/.test(contactInput.value)) {
        contactInput.placeholder = "Enter your mobile number";
    } else {
        contactInput.placeholder = "Enter your email address";
    }
}
