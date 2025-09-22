document.addEventListener("DOMContentLoaded", function() {
    const buttonWelcome = document.querySelector("#btn-do-greeting");
    const buttonGetProfile = document.querySelector("#btn-get-data-profile");
    const messageDiv = document.getElementById("message");
    const buttonStat = document.querySelector("#btn-get-stats");
    const buttonClear = document.querySelector("#btn-do-clear");

    /**
     * Универсальная функция, для получения данных
     * @param {String} endpoint - запрос апи
     * @param {Function} successCB - функция коллбека
     * @return Response - возвращает ответ на сервер
     */
    async function fetchData(endpoint, successCB) {
        try {
            messageDiv.innerHTML = `<p class="loading">Загрузка</p>`;
            messageDiv.className = "";
            const response = await fetch(endpoint);
            if (Response.ok) throw new Error(`HTTP error. Status: ${response.status}`);
            const data = await response.json();
            successCB(data);
        } catch (error) {
            console.error("Ошибка при получении данных", error);
            messageDiv.innerHTML = `<p class="error">Ошибка</p>`;
            messageDiv.className = "error";
        }
    }

    //приветствие
    function displayWelcome(data) {
        messageDiv.innerHTML = `
        <h2>${data.message}</h2>
        <p>Доброе(-ый) ${data.greeting_time}, ${data.user}!</p>
        <small>Время запроса: ${data.time_temp}</small>
        `;
        messageDiv.className = "success"
    }

    function displayProfile(data) {
        messageDiv.innerHTML = `
        <h2>Профиль пользователя</h2>
        <form>
        <p><strong>Email:</strong> ${data.email}</p>
        <p><strong>Роль:</strong> ${data.role}</p>
        <p><strong>Последний вход:</strong> ${data.last_login}</p>
        <p><strong>Права доступа:</strong> ${data.permission.join(", ")}</p>
        <p><strong>Количество входов:</strong> ${data.login_count}</p>
        </form>
        `;
        messageDiv.className = "success"
    }

    function displayStatistic(data) {
        messageDiv.innerHTML = `
        <h2>Профиль пользователя</h2>
        <form>
        <p><strong>Количество пользователей:</strong> ${data.total_users}</p>
        <p><strong>Активные пользователи:</strong> ${data.active_users}</p>
        <p><strong>Новые пользователи(На неделе):</strong> ${data.new_users_week}</p>
        <p><strong>Статус системы:</strong>
        <span style="color: ${data.system ? "green" : "red"}"> ${data.system}</span></p>
        </form>
        `;
        messageDiv.className = "success"
    }

    //вызов переключения страницы
    buttonWelcome.addEventListener("click", () => fetchData("/api/welcome", displayWelcome));
    buttonGetProfile.addEventListener("click", () => fetchData("/api/profile", displayProfile));
    buttonStat.addEventListener("click", () => fetchData("/api/statistic", displayStatistic));
    buttonClear.addEventListener("click", () => {
        messageDiv.innerHTML = "...Здесь будут данные...";
        messageDiv.className = "NonData";
    });

    function autoRefresh() {
        const buttonRefresh = document.createElement("button");
        buttonRefresh.textContent = "*Автообновление приветствия*";
        buttonRefresh.style.margin = "20px";
        buttonRefresh.addEventListener("click", ()=> {
            setInterval(() => {
                fetchData("/api/welcome", displayWelcome);
            }, 5000)
        buttonRefresh.disabled = true;
        buttonRefresh.textContent = "*Автообновление влючено*"
        })
        document.querySelector("p").appendChild(buttonRefresh);
    }
    autoRefresh()
});