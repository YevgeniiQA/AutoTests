from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

browser.config.hold_browser_open = True
browser.open('https://duckduckgo.com')

s('[name=q]').type('itstep').press_enter()
ss('.ikg2IXiCD14iVX7AdZo1')[0].element('a').click()
ss('.header__bottom')[0].element('a').click()

page_text = browser.driver.page_source
count = len([word for word in page_text.split() if 'step' in word.lower()])

print(f'Слово "step" присутствует {count} раз на сайте.')
