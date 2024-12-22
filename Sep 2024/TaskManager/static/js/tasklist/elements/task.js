// ===================== Task class ===================== //

function Task(task_element) {
    this.task = task_element;
    this.id = task_element.dataset.id;

    // elements for event handing.
    this.deleteButton = this.task.querySelector("button.delete-task-item");
    this.statusCheckBox = this.task.querySelector("input[type=checkbox].task-list-item-checkbox")
    this.taskText = this.task.querySelector("span.task-list-item-text");

    this.onResponseUpdateTask = (res) => { on_response_update_task(res, this) };
    this.onResponseDeleteTask = (res) => { on_response_delete_task(res, this) };


    // assigning event handler for deleting the task
    this.deleteButton.onclick = (e) => {
        e.preventDefault(); // preventing form from submitting.
        const fetchDeleteRequest = (data) => {
            fetchRequest("api/delete_task", data, this.onResponseDeleteTask)
        }

        onClickDelete(this, fetchDeleteRequest)
    };

    // assigning event handler for updating the task
    // updating the task status and text
    this.statusCheckBox.onchange = (e) => {

        const fetchStatusRequest = (data) => {
            fetchRequest("api/update_task", data, this.onResponseUpdateTask)
        }
        onCheckItem(this, fetchStatusRequest)
    };

    this.assignEvent = function (eventNames, eventFunc) {

        switch (eventNames) {
            case "delete":
                this.deleteButton.onclick = eventFunc;
                break;
            case "update":
                this.statusCheckBox.onchange = eventFunc;
                break;
            case "edit":
                this.taskText.onclick = eventFunc;
                break;
        }

    }

    // setter and getter methods

    this.setText = function (text) {
        this.taskText.innerText = text;// updating the text of the task
    }

    this.getText = function () {
        return this.taskText.innerText;
    }

    this.setId = (id) => {
        this.id = id;
        this.task.dataset.id = id
    }

    // set attributes
    this.setAttr = (attr, value) => {
        this.task.setAttribute(attr, value);
    }
}
// ===================== Task class ===================== //

