//Waits until page fully loads
document.addEventListener("DOMContentLoaded", function () {

    // CONTACT FORM 
    const form = document.getElementById("contactForm");
    
    //Only runds if form exists
    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            //Gets users inputs
            const name = document.getElementById("name");
            const email = document.getElementById("email");
            const message = document.getElementById("message");

            //Validation (checks empty fields to see if all fields are filled)
            if (!name.value || !email.value || !message.value) {
                alert("Please fill in all fields");
                return;
            }

            alert("Message sent successfully!");
            form.reset();
        });
    }

    // IMAGE SLIDER FIX
    const slider = document.getElementById("slider");

    if (slider) {

        //List of slider images
        const images = [
            "images/Gemini_Generated_Image_r5rx46r5rx46r5rx.png",
            "images/Gemini_Generated_Image_r5rx46r5rx46r5rx-4.png",
            "images/Gemini_Generated_Image_r5rx46r5rx46r5rx-3.png"
        ];

        let index = 0;

        //Changes images every 3 seconds
        setInterval(() => {
            index = (index + 1) % images.length;
            slider.src = images[index];
        }, 3000);
    }

});