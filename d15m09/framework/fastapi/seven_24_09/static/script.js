window.onload = function() {
    fetch("/api/todos")
    .then(response=>{
        if (response.status === 401){
            window.location.href = "/login";
            return
        };
        return response.json();
    })
    .then((data) => {
        if(!data) return;
        console.log(data + " Дата(.then(data =>...))")
    const list = document.querySelector(".task-list")
    list.innerHTML = "";
    data.todos.forEach(todo => {
        const li = document.createElement("li");
        if(todo.complete){
            li.classList.add("completed");
        };
        const span = document.createElement("span");
        span.classList = "task-text";
        span.textContent = todo.task;
        span.onclick = () => toggleTask(todo.id);
        
        const deleteBtn = document.createElement("button");
        deleteBtn.className = "delete-button";
        deleteBtn.textContent = "Удалить";
        deleteBtn.onclick = () => deleteTask(todo.id);
        li.appendChild(span);
        li.appendChild(deleteBtn);
        list.appendChild(li);
    })
    .catch(error =>{
        console.log("Ошибка", error);
        // window.location.href = "/login";
    })
});
}


function addTask() {
    const input = document.getElementById("task-input");
    const task = input.value.trim();
    if (task){
        fetch("/api/todos", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({task: task})
        })
        .then((response) => {
            if (response.ok){
                input.value = "";
                window.onload();
            } else {
                throw new Error("Ошибка добавления задачи");
            }
        })
        .catch((error) => console.log("Ошибка", error))
    }
};

function deleteTask(id) {
    fetch(`/api/todos/${id}`, {
        method: "DELETE"
        })
    .then((response) => {
        if (response.ok){
            input.value = "";
            window.onload();
        } else {
            throw new error("Ошибка удаления задачи")
        }
    })
    .catch((error) => console.Error("Ошибка", error))
};

function toggleTask(id) {
    fetch(`/api/todos/${id}/toggle`, {
         method: "PUT"
    })
    .then((response) => {
        if (response.ok){
            window.onload();
        } else {
            throw new error("Ошибка изменения статуса задачи")
        }
    })
    .catch((error) => console.Error("Ошибка", error))
};