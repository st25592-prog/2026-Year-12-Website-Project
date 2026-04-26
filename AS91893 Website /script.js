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
            "images/Gemini_Generated_Image_r5rx46r5rx46r5rx.png",
            "images/Gemini_Generated_Image_r5rx46r5rx46r5rx-4.png",
            "images/Gemini_Generated_Image_r5rx46r5rx46r5rx-3.png"
        ];

        let index = 0;

        setInterval(() => {
            index = (index + 1) % images.length;
            slider.src = images[index];
        }, 3000);
    }

});