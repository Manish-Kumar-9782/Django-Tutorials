
// ----------------- Task List elements event handler functions ----------------- //

function onClickDelete(selfTask, reqFunc) {
    const data = {
        "taskId": selfTask.id
    }
    console.log(data)
    // sending delete request...
    reqFunc(data)
}


// an event handler function to add task to the task list.
function onAddTaskInputEnter(selfTaskList, reqFunc) {

    const data = {
        text: selfTaskList.textInput.value,
        taskList: selfTaskList.id
    };
    console.log(data)
    reqFunc(data)
    selfTaskList.textInput.value = ''

}


// an event handler function to update the task status
// status: isCompleted
function onCheckItem(selfTask, reqFunc) {

    const data = {
        "update": {
            "isCompleted": selfTask.statusCheckBox.checked,
        },
        "taskId": selfTask.id
    }
    console.log(data)
    // sending update request...
    reqFunc(data)
}



function onEditTaskInputEnter(selfTask, reqFunc) {
    const data = {
        "update": {
            "text": selfTask.getText()
        },
        "taskId": selfTask.id
    }

    // sending request
    reqFunc(data)
}
// ----------------- Task List elements event handler functions ----------------- //


