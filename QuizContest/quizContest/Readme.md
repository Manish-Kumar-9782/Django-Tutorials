# Setup the Django Request

Project Name: `quizContest`

1. First we will make a new app, app name `Teacher`
2. Now we will make a `urls.py` inside the `Teacher` Directory.
3. After this register this application inside our Project `settings.py` file, inside `INSTALLED_APPS` add this value as string. `Teacher.apps.TeacherConfig`
4. Now add a `urlpatterns` list object and import the `path` form `django.urls` module.
5. Now we will shift our focus on the `views.py` inside the `Teacher` app.
6. add a two function for views named as `login` and `home`, and return some `HttpResponse` message.
7. Now Connect these views with the `Teacher`'s views by using the urls.
8. add two `path(url_address, view, view_name).`

## Making Queries

1. `Model.object.all()` : to get all object
2. `Model.object.get(pk=id)` : to get single object associated with given id
3. `Model.save()` : to save the changes
4. `Model.object.values().all()` : first get the QuerySet in the dict format then get all object's values
