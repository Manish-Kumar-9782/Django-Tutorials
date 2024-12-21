// a response function to add task to the selfTask list
// selfTask is the TaskList object
function on_response_add_task(res, selfTaskList) {

    if (res) {
        data = res.data
        console.log(data)
        selfTaskList.createTask(data.text, data.taskId)
    }

}


// a response function to delete task by using selfTask object
// selfTask is the Task object
function on_response_delete_task(res, selfTask) {

    if (res) {
        if (res.status = "success") {
            selfTask.task.remove();
        }
    }
}


// a response function to update task by using selfTask object
// selfTask is the Task object
function on_response_update_task(res, selfTask) {

    if (res) {
        if (res.status == "success") {
            const taskId = res.data.taskId;
            // const taskCheckBox = document.getElementById(`task-${taskId}`)
            selfTask.statusCheckBox.checked = res.data.update.isCompleted;
        }
    }
}
