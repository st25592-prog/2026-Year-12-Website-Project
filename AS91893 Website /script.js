// =========================
// RUN WHEN PAGE LOADS
// =========================
document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // FORM VALIDATION
    // =========================
    const form = document.getElementById("contactForm");

    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            // Email pattern check
            const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

            if (name === "" || email === "" || message === "") {
                showMessage("Please fill in all fields", "error");
            } 
            else if (!email.match(emailPattern)) {
                showMessage("Please enter a valid email address", "error");
            } 
            else {
                showMessage("Message sent successfully!", "success");
                form.reset();
            }
        });
    }


    // =========================
    // IMAGE SLIDER (HOME PAGE)
    // =========================
    const images = [
        "images/food1.jpg",
        "images/food2.jpg",
        "images/food3.jpg"
    ];

    let index = 0;
    const slider = document.getElementById("slider");

    if (slider) {
        setInterval(() => {
            index = (index + 1) % images.length;
            slider.src = images[index];
        }, 3000);
    }


    // =========================
    // CARD FADE-IN ANIMATION
    // =========================
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, i) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "0.5s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, i * 150);
    });

});


// =========================
// SHOW MESSAGE FUNCTION
// =========================
function showMessage(text, type) {

    let messageBox = document.getElementById("formMessage");

    // Create message box if not there
    if (!messageBox) {
        messageBox = document.createElement("div");
        messageBox.id = "formMessage";
        document.body.appendChild(messageBox);
    }

    messageBox.textContent = text;

    if (type === "error") {
        messageBox.style.backgroundColor = "#ff4d4d";
    } else {
        messageBox.style.backgroundColor = "#28a745";
    }

    messageBox.style.color = "#fff";
    messageBox.style.padding = "10px";
    messageBox.style.position = "fixed";
    messageBox.style.bottom = "20px";
    messageBox.style.right = "20px";
    messageBox.style.borderRadius = "5px";

    // Remove after 3 seconds
    setTimeout(() => {
        messageBox.remove();
    }, 3000);
}