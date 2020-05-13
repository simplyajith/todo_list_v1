
Steps to run test:
-----------------
1)Clone the git repo.

   git clone git@github.com:todo_list_v1.git
   
   cd todo_list_v1/
   
2)Create a python virtual environment in todo_list_v1 folder.

**For windows**
    
    python3 -m venv venv
    cd venv/Scripts
    ./activate
   
**For Mac**

    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate 
    
Install the modules in requirements.txt.
   
    pip install -r requirements.txt

Run server

```cd todo_

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata status.json

python manage.py runserver```


``**Get Requests:**``

To Lists all the tasks
 
 `http://127.0.0.1:8000/api/todo/`

To list all the completed tasks

`http://127.0.0.1:8000/api/todo/?is_completed=True`

To list all the completed tasks with label

`http://127.0.0.1:8000/api/todo/?labels=personal&is_completed=True`

To get individual details for tasks

`http://127.0.0.1:8000/api/todo/23/`

**POST Request**

To create new todo task


`http://127.0.0.1:8000/api/todo/`

    {
        "name": "ajiths task",
        "description": "To completed todo API backend",
        "labels": "personal",
        "due_date": "2020-05-14",
        "status": "In Progress"
    }

To edit task

Request:PUT

`http://127.0.0.1:8000/api/todo/23/`

    {
        "name": "ajiths task",
        "description": "To completed todo API backend",
        "labels": "personal",
        "due_date": "2020-05-14",
        "status": "In Progress"
    }











