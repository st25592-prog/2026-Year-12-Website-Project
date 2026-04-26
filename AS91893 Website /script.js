document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // CONTACT FORM FIX (WORKING)
    // =========================
    const form = document.getElementById("contactForm");

    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            const name = document.getElementById("name");
            const email = document.getElementById("email");
            const message = document.getElementById("message");

            if (!name.value || !email.value || !message.value) {
                alert("Please fill in all fields");
                return;
            }

            alert("Message sent successfully!");
            form.reset();
        });
    }

    // =========================
    // IMAGE SLIDER FIX
    // =========================
    const slider = document.getElementById("slider");

    if (slider) {
        const images = [
            "Images/Gemini_Generated_Image_gcrg3cgcrg3cgcrg.png",
            "images/food1.jpg",
            "images/food2.jpg"
        ];

        let index = 0;

        setInterval(() => {
            index = (index + 1) % images.length;
            slider.src = images[index];
        }, 3000);
    }

});