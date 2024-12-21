
function getCsrfToken() {
    return document.getElementsByName("csrfmiddlewaretoken")[0].value
}



const get_list_item_template = (text, taskId) => {
    return `<li class="task-list-item">

    <div>
        <input class="task-list-item-checkbox"
               type="checkbox"
               name="task-${taskId}"
               id="task-${taskId}" >

        <span class="task-list-item-text">
           ${text}
        </span>
    </div>

    <div class="list-item-actions">
        <button class="delete-task-item">
            <i class="bi bi-x-lg"></i>
        </button>
    </div>
</li>`
}


const createListItem = (text, taskId) => {
    const el = document.createElement('div');
    el.innerHTML = get_list_item_template(text, taskId);
    return el.firstElementChild;
}



