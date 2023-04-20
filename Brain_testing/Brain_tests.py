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

    def verif_sch(self):
        ss('div.search-wrapper').should(have.size_greater_than(0))

    def mer_obl(self):
        s('/html/body/header/div[2]/div/div/div[1]/ul/li[6]').click()

    def sh_ant_wf(self):
        s('a[href="/ukr/category/Wi_Fi_aksesuary-c1369-396/"]').click()

    def sort_price(self):
        s('.sorm-menu-item.has-child').click()
        s('a[href="/ukr/category/Wi_Fi_aksesuary-c1369-396/order=asc;sortby=price/"]').click()

    def filter(self):
        s('[data-filter="5047-86008847700"]').click()
        s('[href="/ukr/category/Wi_Fi_aksesuary-c1369-396/sortby=price;order=asc;filter=5047-86008847700/"]').click()

    def verif_ftr(self):
        s('.br-sib-c').should(have.exact_text('зовнішній'))

    def shoose_fst_g(self):
        ss('.br-cont')[0].element('a').click()

    def buy(self):
        s('#br-pr-2').click()

    def close_buy_win(self):
        s('//*[@id="checkout-modal-popup"]/div/div[1]/div/div[1]/button/i').click()

    def sh_basket(self):
        s('.cart-button.user-cart-count.cart_custom_styles.not_empty').click()

    def verif_count_g(self):
        s('.cart_item_amount').should(have.exact_text('1'))

    def clear_bas(self):
        s('.clear-cart').click()

    def verif_empty_bas(self):
        s('.br-ch-block.br-cart-empty').should(have.exact_text('Ваш кошик порожній.'))

    def user_pers_data(self):
        s('.user-panel-button.active').click()
        s('[href="/ukr/cabinet/profile/"]').click()

    def ch_us_ln(self, brain: str):
        s('#profile-lastname-input').double_click().type(brain).press_enter()
        s('.text-center').click()

    def



