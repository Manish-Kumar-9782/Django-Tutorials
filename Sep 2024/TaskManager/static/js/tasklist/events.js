
// ----------------- Task List elements event handler functions ----------------- //

function onClickDelete(selfTask, reqFunc) {
    const data = {
        "taskId": selfTask.id
    }
    console.log(data)
    // sending delete request...
    reqFunc(data)
}



function onInputEnter(selfTaskList, reqFunc) {

    const data = {
        text: selfTaskList.textInput.value,
        taskList: selfTaskList.id
    };
    console.log(data)
    reqFunc(data)
    selfTaskList.textInput.value = ''

}



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


// ----------------- Task List elements event handler functions ----------------- //


