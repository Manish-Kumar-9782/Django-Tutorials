
// ===================== TaskList class ===================== //

function TaskList(tasklist_element) {
    this.tasklist = tasklist_element;
    this.id = tasklist_element.dataset.id;
    this.list = this.tasklist.querySelector("ul.task-list");
    this.textInput = this.tasklist.querySelector("input.add-task-input");
    this.isEnterPressed = false;
    this.tasks = {};

    this.onResponseAddTask = (res) => { on_response_add_task(res, this) };
    this.onResponseUpdateTask = null

    this.loadTasks();  // on TaskList Creation load all Tasks
    this.assignTaskEvents(); // on TaskList Creation assign all Task Events


    // # ------------------------------------------ # //
    this.textInput.onkeypress = (e) => {
        if (e.key === "Enter") {
            e.preventDefault(); // preventing form from submitting.
            const fetchAddTaskRequest = (data) => {
                fetchRequest("api/add_task", data, this.onResponseAddTask)
            }
            onAddTaskInputEnter(this, fetchAddTaskRequest)
        }
    }


    // # ------------------------------------------ # //
    TaskList.task_edit_input.onkeypress = (e) => {

        if (e.key === "Enter") {
            this.isEnterPressed = true;
            e.preventDefault(); // preventing form from submitting.
            const task = this.getTask(TaskList.active_edit_task);

            this.onResponseUpdateTask = (res) => {
                on_response_update_task(res, task)
            };

            const fetchEditTaskRequest = (data) => {
                fetchRequest("api/update_task", data, this.onResponseUpdateTask)
            }

            this.replaceWithText(TaskList.active_edit_task);
            // this line will trigger onblur event

            onEditTaskInputEnter(task, fetchEditTaskRequest)
        }

    }

    // # ------------------------------------------ # //

    // a function to assign events to the task_edit_input
    // this event will run when the input element is out of focus.
    // for example: click outside the input element
    TaskList.task_edit_input.onblur = (e) => {
        console.log("onblur")

        if (!this.isEnterPressed) {
            this.replaceWithText(this.getActiveEditTask());
        }
        this.isEnterPressed = false;
    }

    // # ------------------------------------------ # //
}
// -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- //


// ================ TaskList static properties ================ //

TaskList.task_template = createListItem("", -1);
TaskList.task_edit_input = createEditInput();
TaskList.active_edit_task = null

// ================ TaskList static properties ================ //




// =============== TaskList prototype methods =============== //

TaskList.prototype.createTask = function (text, id) {
    let taskObj = TaskList.task_template.cloneNode(true);
    this.addTask(taskObj, { text: text, taskId: id });
    // adding task element to the tasklist
    this.list.appendChild(taskObj); // appending task to the tasklist

}

// ---------------- TaskList class prototype getter and setter ---------------- //

TaskList.prototype.getTask = function (task_id) {
    return this.tasks[task_id];
}

TaskList.prototype.getEditInput = function () {
    return TaskList.task_edit_input;
}

TaskList.prototype.setInputValue = function (text) {
    TaskList.task_edit_input.value = text;
}

TaskList.prototype.getInputValue = function () {
    return TaskList.task_edit_input.value;
}

TaskList.prototype.inputReplaceWith = function (task) {
    TaskList.task_edit_input.replaceWith(task);
}

TaskList.prototype.setActiveEditTask = function (task_id) {
    TaskList.active_edit_task = task_id;
}

TaskList.prototype.getActiveEditTask = function () {
    return TaskList.active_edit_task;
}

// ---------------- TaskList class prototype getter and setter ---------------- //

// Adding methods to TaskList prototype
TaskList.prototype.addTask = function (task, data = {}) {
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

TaskList.prototype.loadTasks = function () {
    this.tasklist.querySelectorAll("li.task-list-item").forEach(
        (task) => { this.addTask(task) }
    );
}

TaskList.prototype.assignTaskEvents = function () {
    for (let task_id in this.tasks) {
        const task = this.tasks[task_id];
        task.assignEvent("edit", (e) => { this.replaceWithInput(task_id) });
    }
}

TaskList.prototype.replaceWithInput = function (task_id) {
    const task = this.getTask(task_id);
    const input = this.getEditInput();
    this.setInputValue(task.taskText.innerText);
    task.taskText.replaceWith(input);
    this.setActiveEditTask(task_id);
    input.focus();
}

TaskList.prototype.replaceWithText = function (task_id) {
    const task = this.getTask(task_id);
    const input = this.getEditInput();
    const task_text = this.getInputValue();
    task.setText(task_text);
    input.replaceWith(task.taskText);
    this.setActiveEditTask(null);
}

// =============== TaskList prototype methods =============== //