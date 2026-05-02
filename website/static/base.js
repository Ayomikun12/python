const form = document.getElementById("signupForm");
const inputs = document.querySelectorAll(".input-box input");

const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirmPassword");

form.addEventListener("submit", function (e) {

    let isValid = true;

    // Check empty fields
    inputs.forEach((input) => {
        const inputBox = input.parentElement;
        const errorText = inputBox.querySelector(".username-error");

        if (input.value.trim() === "") {
            inputBox.classList.add("error");
            errorText.style.display = "block";
            isValid = false;
        } else {
            inputBox.classList.remove("error");
            errorText.style.display = "none";
        }
    });

    // Password match validation
    const password = passwordInput.value.trim();
    const confirmPassword = confirmPasswordInput.value.trim();
    const confirmBox = confirmPasswordInput.parentElement;
    const confirmErrorText = confirmBox.querySelector(".username-error");

    if (confirmPassword !== "" && password !== confirmPassword) {
        confirmBox.classList.add("error");
        confirmErrorText.textContent = "Passwords do not match";
        confirmErrorText.style.display = "block";
        isValid = false;
    } else if (confirmPassword !== "") {
        confirmErrorText.textContent = "Please Confirm your password";
    }

    if (!isValid) {
        e.preventDefault();
    }

    // // Final success
    // if (isValid) {
    // const userData = {
    //     name: document.getElementById("name").value.trim(),
    //     email: document.getElementById("email").value.trim(),
    //     phone: document.getElementById("phone").value.trim()
    // };

    // Save user details
    // localStorage.setItem("user", JSON.stringify(userData));

    // Redirect to dashboard
    // window.location.href = "/dashboard";

    // signupForm.addEventListener("submit", function (e) {
    //     if (!isValid) {
    //         e.preventDefault(); // stop form submission
    //     }
    // });

// }

});


// const form = document.getElementById("signupForm");
// const inputs = document.querySelectorAll(".input-box input");

// form.addEventListener("submit", function (e) {
//     e.preventDefault(); // stop page reload

//     let isValid = true;

//     inputs.forEach((input) => {
//         const inputBox = input.parentElement;
//         const errorBox = inputBox.querySelector(".username-error");

//         if (input.value.trim() === "") {
//             inputBox.classList.add("error");
//             errorBox.style.display = "block";
//             isValid = false;
//         } else {
//             inputBox.classList.remove("error");
//             errorBox.style.display = "none";
//         }
//     });

//     // Password match check
//     const password = document.getElementById("password").value;
//     const confirmPassword = document.getElementById("confirmPassword").value;

//     if (password !== confirmPassword) {
//         alert("Passwords do not match");
//         isValid = false;
//     }

//     // If everything is correct
//     if (isValid) {
//         // SEND TO BACKEND (later)
//         // For now, redirect to dashboard
//         window.location.href = "/dashboard";
//     }
// });






// const form = document.querySelector("form");
// const fields = form.querySelectorAll(".input-box");

// form.addEventListener("submit", (e) => {
//   e.preventDefault();
//   let valid = true;

//   fields.forEach(field => {
//     const input = field.querySelector("input");

//     if (!input || input.value.trim() === "") {
//       field.classList.add("invalid");
//       valid = false;
//     } else {
//       field.classList.remove("invalid");
//     }
//   });

//   if (valid) {
//     form.submit();
//   }
// });