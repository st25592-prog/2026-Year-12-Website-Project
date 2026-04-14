// =========================
// FORM VALIDATION
// =========================

document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    if (name === "" || email === "" || message === "") {
        alert("Please fill in all fields");
    } else {
        alert("Message sent successfully!");
    }
});


// =========================
// IMAGE SLIDER
// =========================

let images = [
    "images/food1.jpg",
    "images/food2.jpg",
    "images/food3.jpg"
];

let index = 0;

function changeImage() {
    let slider = document.getElementById("slider");
    if (slider) {
        index = (index + 1) % images.length;
        slider.src = images[index];
    }
}

setInterval(changeImage, 3000);