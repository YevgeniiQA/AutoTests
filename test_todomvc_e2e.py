from time import sleep
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

browser.open('http://todomvc.com/examples/emberjs')

def test_e2e():
    s('#new-todo').type('11').press_enter()
    s('#new-todo').type('22').press_enter()
    s('#new-todo').type('33').press_enter()
    s('#new-todo').type('44').press_enter()
    ss('#todo-list li').should(have.exact_texts('11', '22', '33', '44'))
    sleep(1)
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
    ss('#todo-list li').element_by(have.exact_text('22')).double_click().type('edited').press_enter()
    ss('#todo-list li').element_by(have.css_class('.editing'))#.element('.edit')
    # s('#new-todo').type('11').press_enter()
    sleep(2)

    1235456