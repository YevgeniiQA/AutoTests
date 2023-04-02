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

    def should_be(self, *todos: str):
        self.todo_list.should(have.exact_texts(*todos))
        return self

    def start_editing(self, todo, new_text):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return self.todo_list.element_by(have.css_class('editing')).element('.edit').perform(
            command.js.set_value(new_text)).press_enter()

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def edit_by_focus_change(self, todo, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def cancel_edit(self, todo: str, new_text):
        self.start_editing(todo, new_text).press_enter()

    def toggle(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)).element('.toggle').click()
        return self

    def toggle_all(self):
        s('#toggle-all').click()
        return self

    def should_be_completed(self, *todos: str):
        self.todo_list.filtered_by(completed).should(have.exact_texts(*todos))
        return self

    def should_be_active(self, *todos: str):
        self.todo_list.filtered_by(completed.not_).should(have.exact_texts(*todos))
        return self

    def clear_completed(self):
        s('#clear-completed').click()
        return self

    def delete(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)).hover().element('.destroy').click()
        return self

    def should_be_items_left(self, count: int):
        s('#todo-count strong').should(have.exact_text(str(count)))
        return self

    def should_be_empty(self, todo: int):
        self.todo_list.should(have.size(todo))

    def active(self):
        s('[href="#/active"]').click()

    def completed(self):
        s('[href="#/completed"]').click()

    def click(self):
        s('[href="#/"]').click()
