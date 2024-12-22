
// ===================== TaskList class ===================== //

function TaskList(tasklist_element) {
    this.tasklist = tasklist_element;
    this.id = tasklist_element.dataset.id;
    this.list = this.tasklist.querySelector("ul.task-list");
    this.textInput = this.tasklist.querySelector("input.add-task-input");
    this.tasks = {};

    this.onResponseAddTask = (res) => { on_response_add_task(res, this) };
    this.onResponseUpdateTask = null

    this.textInput.onkeypress = (e) => {
        if (e.key === "Enter") {
            e.preventDefault(); // preventing form from submitting.
            const fetchAddTaskRequest = (data) => {
                fetchRequest("api/add_task", data, this.onResponseAddTask)
            }
            onAddTaskInputEnter(this, fetchAddTaskRequest)
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
            (task) => { this.addTask(task) }
        )
    }


    // a function to assign events to all tasks in the tasklist
    // these are only events which can be assigned to the task directory
    // for other events we need to assign them to the task object directly
    this.assignTaskEvents = function () {
        for (let task_id in this.tasks) {
            const task = this.tasks[task_id];
            task.assignEvent("edit", (e) => { this.replaceWithInput(task_id) });
        }
    }


    // # ------------------------------------------ # //
    this.isEnterPressed = false;
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

    this.loadTasks();  // on TaskList Creation load all Tasks
    this.assignTaskEvents(); // on TaskList Creation assign all Task Events
}


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

// a method to replace the text of a task with an input element
TaskList.prototype.replaceWithInput = function (task_id) {
    const task = this.getTask(task_id);
    const input = this.getEditInput();
    // first we need assign the text of the task to the input element
    this.setInputValue(task.taskText.innerText);
    task.taskText.replaceWith(input);
    this.setActiveEditTask(task_id); // setting the active edit task
    input.focus(); // focusing on the input element
}


// a method to replace the input element with the text of the task
TaskList.prototype.replaceWithText = function (task_id) {
    const task = this.getTask(task_id);
    const input = this.getEditInput();
    // first we need assign the text of the to the task from input_element.
    const task_text = this.getInputValue();
    task.setText(task_text);
    input.replaceWith(task.taskText);
    this.setActiveEditTask(null) // resetting the active edit task
}





// =============== TaskList prototype methods =============== //