Sure! Here's how you can split your Django HTML template into smaller components:

1. **Task List Card Template (`task_list_card.html`)**

   ```html
   <div class="task-list-card card-theme"
        style="--color:{{color_range|random}}">
       {% include 'task_list_header.html' %}
       {% include 'task_actions_body.html' %}
   </div>
   ```
2. **Task List Header Template (`task_list_header.html`)**

   ```html
   <header class="tasklist-header">
       <div class="d-flex al-center jc-between">
           <h1 class="task-list-title">{{taskList.title}}</h1>
           <form action="{% url 'delete_taskList' taskList.id %}"
                 method="POST">
               {% csrf_token %}
               <button type="submit"
                       class="task-delete-button">X</button>
           </form>
       </div>
       <div class="d-flex gap-1">
           <span class="task-list-category badge">{{taskList.category}}</span>
           <span class="task-list-category badge status-{{taskList.status}} ">{{taskList.status}}</span>
           <span class="task-list-category badge priority-{{taskList.priority}}">{{taskList.priority}}</span>
       </div>
   </header>
   ```
3. **Task Actions Body Template (`task_actions_body.html`)**

   ```html
   <div class="task-actions-body">
       {% include 'update_task_list_form.html' %}
       {% include 'task_list.html' %}
       {% include 'add_update_task_form.html' %}
   </div>
   ```
4. **Update Task List Form Template (`update_task_list_form.html`)**

   ```html
   <form action="{% url 'update_taskList_tasks' %}"
         method="POST"
         id="update-tasklist-form-{{taskList.id}}">
       {% csrf_token %}
       <input type="text"
              name="taskListId"
              value="{{taskList.id}}"
              hidden>
   </form>
   ```
5. **Task List Template (`task_list.html`)**

   ```html
   <ul id="task-list-{{taskList.id}}"
       class="task-list">
       {% for task in taskList.tasks.all %}
       <li data-id="{{task.id}}"
           class="task-list-item">
           <div>
               <input class="task-list-item-checkbox"
                      type="checkbox"
                      name="task-{{task.id}}"
                      id="task-{{task.id}}"
                      {% if task.isCompleted %}
                      checked
                      {% endif %}>
               <span class="task-list-item-title">
                   {{task}}
               </span>
           </div>
           <div class="list-item-actions">
               <a href="{% url 'update_task' task.id %}"> <i class="bi bi-pencil"></i></a>
               <a href="{% url 'delete_task' task.id %}"><i class="bi bi-x-lg"></i></a>
               <button class="delete-task-item"
                       data-id="{{task.id}}"><i class="bi bi-x-lg"></i></button>
           </div>
       </li>
       {% endfor %}
   </ul>
   ```
6. **Add Update Task Form Template (`add_update_task_form.html`)**

   ```html
   <form id="add-update-task"
         class="d-flex gap-1"
         action="{% if update.taskListId == taskList.id %}
           {% url 'update_task' update.task.id %}
           {% else %}
           {% url 'add_task' taskList.id %}
         {% endif %}"
         method="POST">
       {% csrf_token %}
       <input id="{{taskList.id}}"
              class="add-task-input"
              type="text"
              name="text"
              value="{% if update.taskListId == taskList.id %}{{update.task.text}}{% endif %}">
       <button class="update-tasklist-button"
               type="submit"
               form="update-tasklist-form-{{taskList.id}}">
           <i class="bi bi-floppy2"></i>
       </button>
   </form>
   ```

Breaking down your HTML like this makes it more modular and easier to maintain. It allows you to update individual components without touching the entire template. Let me know if you need any more help or adjustments!
