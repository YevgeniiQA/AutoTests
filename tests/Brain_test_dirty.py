from time import sleep
from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

def test_e2e():
    browser.open('https://brain.com.ua/ukr/')
    browser.driver.maximize_window()

    # s('.br-th-login ').click()
    # s('#modal-login-phone-field').type('+38 (050) 929-69-73')
    # s('#modal-login-password-field').type('83808057').press_enter()
    #
    # s('body > header > div.header-top > div > div > div.user-panel-wrap.js-login-popup > button > span')\
    #     .should(have.exact_text('Євгеній'))
    # s('body > header > div.header-bottom > div > div > div.search-form.header-search-form >\
    #  form > input.quick-search-input').type('Ноутбук').press_enter()
    # ss('div.search-wrapper').should(have.size_greater_than(0))
    # s('[href="/"]').click()
    s('.mycity_container.mycity.mycityname[data-cityid="23562"]').click()
    s('.city_selector[data-cityid="23637"]').click()
    s('a:contains("Магазини")').click()

    sleep(3)

    #83808057
    # s('#new-todo').type('11').press_enter()
    # s('#new-todo').type('22').press_enter()
    # s('#new-todo').type('33').press_enter()
    # s('#new-todo').type('44').press_enter()
    # ss('#todo-list li').should(have.exact_texts('11', '22', '33', '44'))
    # ss('#todo-list li').element_by(have.exact_text('22')).element('.toggle').click()
    # ss('#todo-list li').element_by(have.exact_text('33')).element('.toggle').click()
    # ss('#todo-list li').element_by(have.exact_text('22')).element('.toggle').click()
    # s('[href="#/active"]').click()
    # ss('#todo-list li').should(have.exact_texts('11', '22', '44'))
    # s('[href="#/completed"]').click()
    # ss('#todo-list li').should(have.exact_texts('33'))
    # ss('#todo-list li').element_by(have.exact_text('33')).hover().element('.destroy').click()
    # ss('#todo-list li').should(have.size(0))
    # s('[href="#/"]').click()
    # ss('#todo-list li').element_by(have.exact_text('22')).double_click()
    # ss('#todo-list li').element_by(have.css_class('editing')).element('.edit')\
    #     .perform(command.js.set_value('1234')).press_enter()
    # sleep(3)
    # s('#toggle-all').click()
    # ss('#todo-list li').element_by(have.exact_text('11')).element('.toggle').click()
    # s('#clear-completed').click()
    # ss('#todo-list li').should(have.size(1))