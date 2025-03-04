




function updateCourseOptions() {
    const category = document.getElementById("category").value;
    const courseSelect = document.getElementById("course");
    
    const itCourses = [
        { value: "data_science", text: "Data Science & Business Analytics" },
        { value: "cyber_security", text: "Cyber Security & Ethical Hacking" },
        { value: "cloud_devops", text: "Cloud & DevOps" },
        { value: "chess_analytics", text: "Chess Analytics" }
    ];
    
    const professionalCourses = [
        { value: "event_management", text: "Event Management" },
        { value: "nail_artistry", text: "Nail Artistry" },
        { value: "makeup_artistry", text: "Makeup Artistry" },
        { value: "spoken_english", text: "Spoken English" }
    ];
    
    courseSelect.innerHTML = '<option value="">-- Select Course --</option>';
    
    let courses = category === "it" ? itCourses : category === "professional" ? professionalCourses : [];
    
    courses.forEach(course => {
        const option = document.createElement("option");
        option.value = course.value;
        option.textContent = course.text;
        courseSelect.appendChild(option);
    });
}



document.getElementById("enquiry-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const form = this;
    const formData = new FormData(form);
    
    // Disable submit button to prevent multiple submissions
    const submitButton = form.querySelector("button[type='submit']");
    submitButton.disabled = true;

    fetch("{% url 'enquire_now' %}", {
        method: "POST",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            document.getElementById("success-message").style.display = "block";
            form.reset();
        } else {
            document.getElementById("success-message").style.display = "none";
        }
    })
    .catch(error => console.error("Error:", error))
    .finally(() => {
        // Re-enable submit button after request completes
        submitButton.disabled = false;
    });
});
