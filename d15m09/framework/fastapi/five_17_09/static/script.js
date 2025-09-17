document.addEventListener("DOMContentLoaded", function() {
    const buttonWelcome = document.querySelector(".btn1");
    const buttonGetProfile = document.querySelector(".btn2");
    const messageDiv = document.getElementById("message");
    const body = document.body;
    const data = {
        welcome: {
            message: body.dataset.welcomeMessage,
            userName: body.dataset.welcomeUser,
            timeIsIt: body.dataset.welcomeTimeIsIt,
        },
        profile: {
            email: body.dataset.profileEmail,
            role: body.dataset.profileRole,
            beOnline: body.dataset.profileBeOnline,
        },
    };

    buttonWelcome.addEventListener("click", (e)=> {
        console.log("Message of greeting");
        messageDiv.innerHTML = `
            <h2>${data.welcome.message}</h2>
            <p>Привет,
            ${data.welcome.userName}!</p>
            <p>Good ${data.welcome.timeIsIt}!</p>
        `;
    })
    buttonGetProfile.addEventListener("click", (e)=> {
        console.log("Geting profile");
        messageDiv.innerHTML = `
            <h2>User profile:</h2>
            <p>Email: ${data.profile.email}!</p>
            <p>Role: ${data.profile.role}</p>
            <p>Last login: ${data.profile.beOnline}</p>
        `;
    })
});