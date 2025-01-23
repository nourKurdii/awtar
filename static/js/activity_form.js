// Initialize the intl-tel-input library
var input = document.querySelector("#phone_number");

var iti = window.intlTelInput(input, {
    preferredCountries: ["PS"], // Make Palestine the default
    onlyCountries: ["PS", "IL"], // Allow Palestine (+970) and Israel (+972)
    initialCountry: "PS", // Set Palestine as the initial selected country
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js" // For better validation and formatting
});

// Ensure the phone number starts with the correct country code
input.addEventListener("focus", function () {
    if (input.value === "") {
        var countryData = iti.getSelectedCountryData();
        input.value = "+" + countryData.dialCode; // Add the dial code
    }
});

// Validate the phone number on form submission
document.querySelector("#activityForm").addEventListener("submit", function (e) {
    if (!iti.isValidNumber()) {
        e.preventDefault();
        alert("Please enter a valid phone number with +970 or +972.");
    }
});
