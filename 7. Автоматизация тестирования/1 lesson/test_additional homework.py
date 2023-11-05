from selene.support.shared import browser


def test_authorization():
    browser.open('https://demoqa.com/text-box')

    browser.element('#userName').type('Trixie')
    browser.element('#userEmail').type('qwerty@bk.ru')
    browser.element('#currentAddress').type('Moscow')
    browser.element('#permanentAddress').type('New-York')

    browser.element('#submit').type('yashaka/selene').click()
