from datetime import datetime

from pprint import pprint as pp

from helpers import generate_id

todos = [
    {
        "id": 1,
        "title": "lear python",
        "status": False,
        "duration": 10,
        "created_date": datetime.now()
    },
    {
        "id": 5,
        "title": "lear python",
        "status": False,
        "duration": 10,
        "created_date": datetime.now()
    }
]


def add_todo(tasks, title, duration=60):
    todo = {
        "id": generate_id(tasks),
        "title": title,
        "status": False,
        "duration": duration,
        "created_date": datetime.now()
    }

    tasks.append(todo)


# add_todo(todos, "cut")
# add_todo(todos, "cut")
# add_todo(todos, "cut")
# pp(todos)