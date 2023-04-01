from time import sleep
from selene import have, command
from selene.support.shared.jquery_style import s, ss
from todomvc_testings.Model import todos


def test_e2e():
    todos.given_opened('11', '22', '33', '44')
    ss('#todo-list li').should(have.exact_texts('11', '22', '33', '44'))
    ss('#todo-list li').element_by(have.exact_text('22')).element('.toggle').click()
    ss('#todo-list li').element_by(have.exact_text('33')).element('.toggle').click()
    ss('#todo-list li').element_by(have.exact_text('22')).element('.toggle').click()
    s('[href="#/active"]').click()
    ss('#todo-list li').should(have.exact_texts('11', '22', '44'))
    s('[href="#/completed"]').click()
    ss('#todo-list li').should(have.exact_texts('33'))
    ss('#todo-list li').element_by(have.exact_text('33')).hover().element('.destroy').click()
    ss('#todo-list li').should(have.size(0))
    s('[href="#/"]').click()
    ss('#todo-list li').element_by(have.exact_text('22')).double_click()
    ss('#todo-list li').element_by(have.css_class('editing')).element('.edit')\
        .perform(command.js.set_value('1234')).press_enter()
    sleep(3)
    s('#toggle-all').click()
    ss('#todo-list li').element_by(have.exact_text('11')).element('.toggle').click()
    s('#clear-completed').click()
    ss('#todo-list li').should(have.size(1))
