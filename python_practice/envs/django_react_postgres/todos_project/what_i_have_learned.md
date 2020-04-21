What I Have Learned
=====
A quick summary of things to outline some takeaways
-----

### PostGresSQL
Installing this was a b****!
#### The original problem
I was having was that I was not able to open the postgres shell. Permission was denied (which I had saved the error), but I basically couldn't get into the shell using either of the following commands: `psql postgres` or `sudo -u postgres psql`. Apparently there's a default user postgres that just gets created when you brew install, but I didn't have access to this.

#### Summary of solution
I ended up having postgres installed in two locations. I'm not sure if this was from mistakes in installing it (I tried both the web download and using homebrew) or if it was from a previous download on my computer that I forgot about, but it was in two locations. The second location that took a while to find was `/usr/local/tmp/postgres`, iirc. I went to remove that folder, and turns out I didn't have permission to do that. Somehow there was another user on my computer (named **postgres**) that had access to it. Before using sudo to destroy the directory, we wanted to see if fixing things in there would allow it to work. there was some file with the port 5432 and another lock file for that that was creating some error at that point. Ended up deleting those, still couldn't open the shell, and so we ended up just `sudo` removing those files, and then starting over with `brew install postgres` and it worked.

### Django process
I'll do a quick summary of the steps I followed to create my Todo List app. I followed a mixture of tutorials, ordered respectively by how much I used them: https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react, https://docs.djangoproject.com/en/3.0/intro/tutorial01/, https://djangocentral.com/using-postgresql-with-django/, https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/, and https://www.valentinog.com/blog/drf/.

1. There was actually quite a bit of confusion from a file structure perspective between two of the main project tutorials (https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react and https://www.valentinog.com/blog/drf/) and which commands to use (`python manage.py startapp [app_name]` vs `django-admin startapp [app_name]`), but I ended up using the first tutorial, because it aligned with the Django docs.
2. Basically followed everything from this tutorial to setup postgres with django, except for `ENGINE` I didn't include "psycopg2" at the end, so my opening line in `settings.py` was: `'ENGINE': 'django.db.backends.postgresql'`.
   * It took a while to figure out whether I should run `python manage.py migrate` right after editing these settings, because the order in the official Django docs tutorial (https://docs.djangoproject.com/en/3.0/intro/tutorial01/) does stuff with views first. But I realized I haven't set up my other personal projects with views first, and I wanted to make sure the database was working, so I ran the migration and it didn't fail, so I was in the clear.

2. Next was making and activating the models. The order shouldn't matter, but you'll need both (activate it and migrate the new models) in order to use them in the shell, which you can test out at the end.
   1. In order to include the app in the project, we need to add it to the `INSTALLED_APPS` list in `todo_list/settings.py`. There was some confusion on just adding the name of the app vs the dotted path to the config, but the Django docs tutorial explained that the `TodoListConfig` class was in the `todo_list.apps.py` file, and since I found that and it mirrored the docs tutorial, I followed that (rather than just the app name from https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react). So installed apps looked like this:
   ```
   INSTALLED_APPS = [
      'todo_list.apps.TodoListConfig', # activate the app (name comes from `todo_list/apps.py`)
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
   ]
   ```
   2. Create your model in the `models.py` file.

3. Setup the Django admin interface (not a requirement, but useful). Followed https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react here exactly.
4. Next up is APIs. I found other helpful looking tutorials (https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners because I was looking up the Python package `djangorestframework` because it appeared in all the tutorials except the django docs one, and https://medium.com/technest/build-a-crud-todo-app-with-django-and-react-redux-8ddb0b6ac2f0 because I thought I should probably use redux again). But we didn't cover APIs in Django docs, so maybe this `djangorestframework` is necessary for all of it.
5. **Serializers**: transform model instances to JSON so the frontend can easily use the JSON response.
   1. 

6. URLs and routers
   1. made urls.py file in the todo_list app (there is an existing top level urls.py file in the project directory)
   2. use the router here
   3. wire up the urls into the top level url file using include

***NOTE***: started using https://medium.com/technest/build-a-crud-todo-app-with-django-and-react-redux-8ddb0b6ac2f0 predominantly when frontend began because I didn't want to use `create-react-app` as used in https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react.

7. Frontend (following from https://medium.com/technest/build-a-crud-todo-app-with-django-and-react-redux-8ddb0b6ac2f0)
   1. Run `python manage.py startapp frontend
   2. Set up react/redux with the directories we want:
      ```
      mkdir -p ./frontend/src/{components,actions,reducers}
      $ mkdir -p ./frontend/{static,templates}/frontend
      ```
   3. `npm init -y` in top level project directory to create `package.json` file
      * So `package.json`, `frontend/`, `todo_list/`, and `todos_project/` are at same level in file tree
   6. Packages (optional in [])
      * `npm i -D webpack webpack-cli`
      * `npm i -D babel-loader @babel/core @babel/preset-env @babel/preset-react [@babel/plugin-proposal-class-properties]`
      * `npm i react react-dom react-router-dom`
      * `npm i redux react-redux redux-thunk redux-devtools-extension`
      * `npm i redux-form`
   5. Create `.babelrc` which enables us to use `Async/Await`
   6. Create `webpack.config.js`
   7. Edit scripts file in `package.json`
      * This creates scripts for `npm run dev` and `npm run build`, which both have webpack bundle the modules and output the `main.js` file for the respective environments.
   8. create first react files
      1. index.js
      2. app.js
      3. index.html in template frontend
         * in order for this file to be accessible, we need frontend views and frontend urls, and then we wire up the url in the project urls.py

         got stuck, ended uo having to add frontend to the installed apps