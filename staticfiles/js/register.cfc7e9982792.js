console.log("hello")
const usernamefield = document.querySelector("#username");
const feedbackfield = document.querySelector(".invalid_feedback");
const emailfield = document.querySelector("#email");
const passwordfield = document.querySelector("#password");
const emailfeedbackfield = document.querySelector(".emailinvalid_feedback");
const usernamesuccessOut = document.querySelector(".usernamesuccessOut");
const showpasswordToggle = document.querySelector(".showpassword");
const submitBTN = document.querySelector(".submit-btn");

const handleToggle = (e)=>{
    if(showpasswordToggle.textContent=== "show"){
        showpasswordToggle.textContent = "hide";
        passwordfield.setAttribute("type","text");
    }else{
        showpasswordToggle.textContent = "show";
        passwordfield.setAttribute("type","password");
    }
    
}

showpasswordToggle.addEventListener("click",handleToggle);  


emailfield.addEventListener("keyup", (event) => {
    console.log("7777777", 7777777)
    const emailvalue = event.target.value;
    console.log("emailval",emailvalue)

 if(emailvalue.length > 0){
    fetch("/authentication/emailvalidation", {
        body:JSON.stringify({
            email:emailvalue
        }),
        method:"POST",
 }).then(res=>res.json()).then(data=>{

    console.log("data",data);
    if(data.email_error){
        // submitBTN.setAttribute("disabled",true);
        submitBTN.disabled = true;
        emailfield.classList.add("is-invalid");
        emailfeedbackfield.style.display = 'block';
        emailfeedbackfield.innerHTML =`<p>${data.email_error}</p>`
    }else{
        submitBTN.removeAttribute("disabled");
    }
 });
}
});

usernamefield.addEventListener("keyup", (event) => {
    console.log("7777777", 7777777)
    const usernamevalue = event.target.value;
    console.log("usernameval",usernamevalue)
    usernamesuccessOut.textContent=`checking ${usernamevalue} `;

 if(usernamevalue.length > 0){
    fetch("/authentication/usernamevalidation", {
        body:JSON.stringify({
            username:usernamevalue
        }),
        method:"POST",

    }).then(res=>res.json()).then(data=>{

        console.log("data",data);
        usernamesuccessOut.style.display = 'none';
        if(data.username_error){
            usernamefield.classList.add("is-invalid");
            feedbackfield.style.display = 'block';
            feedbackfield.innerHTML =`<p>${data.username_error}</p>`;
            submitBTN.disabled = true;

        }else{
            usernamefield.classList.remove("is-invalid");
            feedbackfield.style.display = 'none';
            submitBTN.removeAttribute("disabled");
            
        }
        
    });
}
}); 



