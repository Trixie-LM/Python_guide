"""
    • driver.switch_to - переключает фокус на модальное окно; • .accept() - нажимает на кнопку "OK" в модальном окне;
    • driver.dismiss() - нажимает на кнопку "Отмена" в модальном окне;
    • driver.send_keys() - отправляет текст в текстовое поле в модальном окне;
    • driver.text - возвращает title модального окна.

    prompt = driver.switch_to.alert
    prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
"""