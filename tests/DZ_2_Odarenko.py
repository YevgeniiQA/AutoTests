from time import sleep
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

browser.open('https://www.ecosia.org')

s('[name=q]').type('yashaka selene').press_enter()
ss('.result__body')[0].element('a').click()

sleep(2)

ss('[href="/yashaka/selene"]').should(have.size(3))
