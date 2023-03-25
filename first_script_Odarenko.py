from time import sleep
from selene import have
from selene.support.shared import browser

browser.open('http://todomvc.com/examples/emberjs')

browser.element('#new-todo').type('a').press_enter()
browser.element('#new-todo').type('b').press_enter()
browser.element('#new-todo').type('c').press_enter()
sleep(2)

browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
sleep(2)
browser.element('#clear-completed').click()
sleep(2)

browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))
