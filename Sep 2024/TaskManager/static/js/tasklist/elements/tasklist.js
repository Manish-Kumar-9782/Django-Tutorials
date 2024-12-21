
// ===================== TaskList class ===================== //

function TaskList(tasklist_element) {
    this.tasklist = tasklist_element;
    this.id = tasklist_element.dataset.id;
    this.list = this.tasklist.querySelector("ul.task-list");
    this.textInput = this.tasklist.querySelector("input.add-task-input");
    this.tasks = {};

    this.onResponseAddTask = (res) => { on_response_add_task(res, this) };

    this.textInput.onkeypress = (e) => {

        if (e.key === "Enter") {
            e.preventDefault(); // preventing form from submitting.
            const fetchAddTaskRequest = (data) => {
                fetchRequest("api/add_task", data, this.onResponseAddTask)
            }
            onInputEnter(this, fetchAddTaskRequest)
        }
    }

    // a function to load all tasks in the tasklist
    this.addTask = function (task, data = {}) {
        const task_id = task.dataset.id;
        const newTask = new Task(task);
        this.tasks[task_id] = newTask;

        if (data.text) {
            newTask.setText(data.text);
        }

        if (data.isCompleted) {
            newTask.statusCheckBox.checked = data.isCompleted;
        }

        if (data.taskId) {
            newTask.setId(data.taskId);
        }
    }

    this.loadTasks = function () {
        this.tasklist.querySelectorAll("li.task-list-item").forEach(
            (task) => {
                this.addTask(task);
            }
        )
    }
    this.loadTasks();  // on TaskList Creation load all Tasks

}

TaskList.task_template = createListItem("", -1);

TaskList.prototype.createTask = function (text, id) {
    let taskObj = TaskList.task_template.cloneNode(true);
    this.addTask(taskObj, { text: text, taskId: id }); // adding task element to the tasklist
    this.list.appendChild(taskObj); // appending task to the tasklist

}
// ===================== TaskList class ===================== //