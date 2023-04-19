from time import sleep
from selene import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

class BrainTS:
    def __init__(self):
        self.major_URL = 'https://brain.com.ua/ukr/'

    def open(self):
        browser.open('https://brain.com.ua/ukr/')
        browser.driver.maximize_window()

    def ch_city(self):
        s('.mycity_container.mycity.mycityname[data-cityid="23562"]').click()
        sleep(1)
        s('.city_selector[data-cityid="23637"]').click()
        sleep(1)

    def sh_map(self):
        s('a[href="/ukr/shops_map/"]').should(be.clickable).click()

    def st_page(self):
        s('[href="/"]').click()

    def login(self):
        s('.br-th-login ').click()
        s('#modal-login-phone-field').type('+38 (050) 929-69-73')
        s('#modal-login-password-field').type('83808057').press_enter()
        s('.user-panel-button.active').should(have.exact_text('Євгеній'))

    def search(self, brain: str):
        s('/html/body/header/div[2]/div/div/div[2]/form/input[1]').type(brain).press_enter()
        return self

    def verif(self):
        ss('div.search-wrapper').should(have.size_greater_than(0))

    def mer_obl(self):
        s('/html/body/header/div[2]/div/div/div[1]/ul/li[6]').click()

