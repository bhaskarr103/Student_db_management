document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM content loaded");

    const inputFields = document.querySelectorAll(".form-control");

    inputFields.forEach(function (inputField) {
        inputField.addEventListener("focus", function () {
            console.log("Input field focused");
            this.style.borderColor = "green";
        });

        inputField.addEventListener("blur", function () {
            console.log("Focus lost");
            this.style.borderColor = "";
        });
    });
});
