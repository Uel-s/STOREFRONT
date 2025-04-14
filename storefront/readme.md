# Django installation.

- Open cmd and enter the following commands.

```py
1. $ pip install pipenv
2. $ mkdir project-name && cd project-name
3. $ pipenv install django
4. $ pipenv shell
5. $ django-admin startproject project-name .
6. $ code .
```

## Debugging

- Google `django debug toolbar`

Run:

```py
pipenv install django-debug-toolbar
```
- In settings,py under INSTALLED_APPS add;

`debug_toolbar`

- In the main urls.py file add the following:

```py
from django.urls import include, path
import debug_toolbar_urls

path("__debug__/", include(debug_toolbar.urls)),
```

- In settings.py file under MIDDLEWARE add at the top list;

```py
    "debug_toolbar.middleware.DebugToolbarMiddleware",
```

- Add this to settings.py file;
```py
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```