from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

browser.config.hold_browser_open = True
browser.open('http://todomvc.com/examples/emberjs/')

s('#new-todo').type('any_text1').press_enter()
s('#new-todo').type('any_text0').press_enter()
s('#new-todo').type('any_text2').press_enter()
s('#new-todo').type('any_text3').press_enter()
s('#new-todo').type('any_text4').press_enter()

ss('#todo-list>li').should(have.exact_texts('any_text1', 'any_text0', 'any_text2', 'any_text3', 'any_text4'))
