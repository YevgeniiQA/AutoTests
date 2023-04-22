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

    shop_items = ss('#shoptabs-2 .shop-item')
    assert len(shop_items) == 2
