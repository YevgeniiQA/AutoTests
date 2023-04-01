from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

completed = have.css_class('completed')

class TodoMVC:
    def __init__(self):
        self.todo_list = ss('#todo-list li')

    def open(self):
        browser.open('http://todomvc.com/examples/emberjs')
        return self

    def add(self, *todos: str):
        for todo in todos:
            s('#new-todo').type(todo).press_enter()
        return self

    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)
