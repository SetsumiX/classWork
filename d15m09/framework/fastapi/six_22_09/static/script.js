//Отрисовка задач
window.onload = function() {
    fetch("/todos")
    .then(responce => responce.json())
    .then(data => {
        const list = document.getElementById("taskList");
        list.innerHTML = "";
        data.todos.forEach(todo => {
            const li = document.createElement("li");
            li.textContent = todo.task;
            li.onclick = () => deleteTask(todo.id);
            list.appendChild(li);
        });
    });
};

//Добавление задачи
function addTask() {
    const input = document.getElementById("taskInput");
    const task = input.value.trim()
    if(task){
        fetch("/todos", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({task})
        })
        .then((_) => {
            input.value = "";
            window.onload();
        });
    };
};

//Удаление
function deleteTask(id) {
    fetch(`/todos/${id}`, {method: "DELETE"})
    .then(()=>window.onload());
};
