
document.addEventListener("DOMContentLoaded", function() {

    // Get the form element
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        // Get all input elements within the form
        const inputs = form.querySelectorAll("input[type='text']");

        // Loop through each input to check if it's empty
        for (let input of inputs) {
            if (input.value.trim() === "") {
                alert("Please answer all questions before submitting the form.");
                event.preventDefault();  // Prevent the form submission
                return;
            }
        }
    });

});
