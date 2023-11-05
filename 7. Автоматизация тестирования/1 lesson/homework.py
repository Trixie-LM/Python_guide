from selene.support.shared import browser
from selene import be, have


browser.open('https://google.com')
browser.element('#APjFqb').should(be.blank).type('yashaka/selene').press_enter()
browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))
