document.addEventListener("DOMContentLoaded", function() {
    const button_1 = document.querySelector(".btn1")

    if(button_1){
        button_1.addEventListener("click", (e) =>{
            const body = document.body;
            const message = body.dataset.message;
            const username = body.dataset.user;

            const messageDiv = document.getElementById("message");
            if (messageDiv){
                messageDiv.innerHTML = `<h2>${message}</h2>`
                messageDiv.innerHTML += `<p>Hi, ${username}</p>`
            }
        })
    }
});