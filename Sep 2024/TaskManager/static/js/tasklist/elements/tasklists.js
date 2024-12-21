// ===================== TaskLists class ===================== //
function TaskLists() {
    this.tasklists = {}

    // a function to add tasklist to the tasklist 
    this.add = function (tasklist) {
        const tasklist_id = tasklist.dataset.id;
        this.tasklists[tasklist_id] = new TaskList(tasklist);
    }

    // a function to add many tasklists to the TaskLists container at once
    this.addMany = function (tasklists) {
        for (let tasklist of tasklists) {
            this.add(tasklist);
        }
    }
}


// ===================== TaskLists class ===================== //