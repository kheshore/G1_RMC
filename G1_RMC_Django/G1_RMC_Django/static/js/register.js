const emailField = document.querySelector("#email");

const submitBtn = document.querySelector('.submit-btn');
const emailFeedbackArea = document.querySelector(".emailFeedbackArea");

emailField.addEventListener("keyup", (e) => {
    
    const emailVal = e.target.value;
    emailField.classList.remove("is-invalid");
    emailFeedbackArea.style.display = "none";
   
    if (emailVal.length > 0){
        console.log("working")
        fetch("/authentication/validate_email", {
            body:JSON.stringify({email : emailVal}),
            method : "Post" 
        })
        .then((res) => res.json())
        .then((data) =>{
            console.log("data", data);
            if (data.email_error){
                emailField.classList.add("is-invalid");
                emailFeedbackArea.style.display = "block";
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
            }
        })
    }
    
})