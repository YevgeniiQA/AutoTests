from time import sleep
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

def test_e2e():
    browser.open('https://brain.com.ua/ukr/')
    browser.driver.maximize_window()
    s('.mycity_container.mycity.mycityname[data-cityid="23562"]').click()
    sleep(1)
    s('.city_selector[data-cityid="23637"]').click()
    sleep(1)
    s('a[href="/ukr/shops_map/"]').should(be.clickable).click()
    s('[href="/"]').click()
    s('.cover').click()
    s('.br-th-login ').click()
    s('#modal-login-phone-field').type('+38 (050) 929-69-73')
    s('#modal-login-password-field').type('83808057').press_enter()
    s('body > header > div.header-top > div > div > div.user-panel-wrap.js-login-popup > button > span')\
        .should(have.exact_text('Євгеній'))
    s('body > header > div.header-bottom > div > div > div.search-form.header-search-form >\
     form > input.quick-search-input').type('Ноутбук').press_enter()
    ss('div.search-wrapper').should(have.size_greater_than(0))
    s('[href="/"]').click()
    s('body > header > div.header-bottom > div > div > div.main-menu-wrap > ul > li:nth-child(6) > a').click()
    s('#cat972 > div.br-category-block-right > div.br-category-block-bottom > div > ul > li:nth-child(12) > a').click()
    s('body > div.category-page-wrapper > div > div.container.br-container-main > div > div:nth-child(2) >\
     div.catalog-header > div > div.br-sort-menu > ul > li.sorm-menu-item.has-child').click()
    s('body > div.category-page-wrapper > div > div.container.br-container-main > div > div:nth-child(2) >\
     div.catalog-header > div > div.br-sort-menu > ul > li.sorm-menu-item.has-child > div > ul > li:nth-child(1) >\
      a > button').click()
    s('[data-filter="5047-86008847700"]').click()
    s('[href="/ukr/category/Wi_Fi_aksesuary-c1369-396/sortby=price;order=asc;filter=5047-86008847700/"]').click()
    s('body > div.category-page-wrapper > div > div.container.br-container-main > div > div:nth-child(2) >\
     div.row.br-row.br-row-main.br-row-main-s > div.br-sidebar > div.visible-lg.filters-lg > div >\
      div.br-si-block > div.br-sib-c > a > button').should(have.exact_text('зовнішній'))
    ss('.br-cont')[0].element('a').click()
    s('#br-pr-2').click()
    s('#checkout-modal-popup > div > div:nth-child(1) > div > div.modal-header > button').click()
    s('body > header > div.header-bottom > div > div > div.cart.js-cart.br-h-cart').click()
    s('.cart_item_amount').should(have.exact_text('1'))
    s('.clear-cart').click()
    s('.br-ch-block.br-cart-empty').should(have.exact_text('Ваш кошик порожній.'))
    s('.user-panel-button.active').click()
    s('[href="/ukr/cabinet/profile/"]').click()
    s('#profile-lastname-input').double_click().type('Тестов').press_enter()
    s('#pop_up_content > div > div > div.modal-header > button > i').click()
    s('.user-panel-button.active').click()
    s('[href="/ukr/cabinet/profile/"]').click()
    s('#profile-lastname-input').double_click().type('Тестовский').press_enter()
    s('#pop_up_content > div > div > div.modal-header > button > i').click()
    s('.user-panel-button.active').click()
    s('[href="/ukr/cabinet/profile/"]').click()
    s('#profile-lastname-input').should(have.value('Тестовский'))
