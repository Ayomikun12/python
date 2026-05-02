const form = document.getElementById("loginForm");
const inputs = document.querySelectorAll(".input-box input");

form.addEventListener("submit", function(e) {
    let isValid = true;

    inputs.forEach((input) => {
        const inputBox = input.parentElement;
        const errorBox = inputBox.querySelector(".username-error");

        if (input.value.trim() === "") {
            inputBox.classList.add("error");
            errorBox.style.display = "block";
            isValid = false;
        } else {
            inputBox.classList.remove("error");
            errorBox.style.display = "none";
        }
    });

    if (!isValid) {
        e.preventDefault(); // stop submission if invalid
    }
});
