"""Краткая шпаргалка по основным командам Selene

browser.element(selector) - находит элемент по селектору
- element.element(selector) находит внутренний элемент внутри другого элемента обозначенного как element (например сохраненного как element = browser.element(selector))
- element.all(selector) находит внутреннюю коллекцию элементов
browser.all(selector) - находит коллекцию элементов по селектору
- collection.by(condition) - фильтрует коллекцию по кондишену (где collection - сохраненная коллекция например через collection = browser.all(selector); condition – что либо из be.* или have.*)
- collection.element_by(condition) - находит элемент коллекции по кондишену
- collection[index] или collection.element(index) - выбирает элемент из коллекции по индексу (есть шорткаты – .first для [0] и .second для [1])
- collection[start:stop:step] - делает срез коллекции начиная со start, заканчивая перед stop, с шагом step (есть шорткаты – .odd для [::2] и .even для [1::2]; есть алиас sliced(start, stop, step) для [start:stop:step])

(element | collection| browser).should(condition) - ждет до выполнения условия и падает если не проходит
(element | collection | browser).wait_until(condition) - ждет до выполнения условия и возвращает false если не проходит, иначе true
(element | collection | browser).matching(condition) - сразу проверяет условие и возвращает false если не проходит, иначе true

Команды типа ...
* collection.by_their(selector, condition)
* collection.element_by_its(selector, condition)
* collection.all(selector)
* collection.all_first(selector)
... – используются реже, и доки на них можно почитать провалившись в их реализацию (там есть детальные docstrings). Также ниже можно найти примеры и разборы этих команд в FAQ в прикрепленном сообщении в этом чате как ответ на вопрос «Как найти нужною строку в таблице по условию ...»

P.S. Чуть более продвинутые вещи...

В Selene нельзя просто так вытащить из элемента текст или какой то атрибут. Это сделано специально, потому что Selene ставит за цель – способствовать реализации эффективных тестов. Хорошие тесты - это такие в которых тестировщик знает на перед что будет на UI в каждый из момент времени, поэтому ему не нужно спрашивать у элемента его текст либо значение определенного атрибута, он либо знает его, либо совершает проверку через .should(have.text('something')) или .should(have.attribute('data').value('bar'). А если ты не знаешь что у тебя на UI значит ты пишешь костыль :) А для костылей - Selene добавляет "экстра API" которое менее лаконичное, и заставляет писать костыли более осознанно. Для этих костылей могут быть в помощь следующие команды...

* element.locate() - вернет чистый selenium-webdriver-овский webelement, из которого можно потом достать кастомные атрибуты например element.locate().get_attribute('src')
* element() - шорткат на .locate(), то есть в реальном коде может выглядеться как browser.element('#foo')().get_attribute('src')
* element.get(query.*) дождется прохождения команды-запроса над элементом и вернет результат, например: browser.element('#foo').get(query.attribute('src')), в отличии от browser.element('#foo').locate().get_attribute('src')) – дождется появления элемента как минимум в DOM и вернет значение атрибута 'src' у этого элемента.
* collection.locate() либо collection() вернет список чистых webelement-ов
* collection.get(query.*) тоже есть, если среди * найдешь запрос для работы конкретно с коллекцией
* browser.get(query.*) тоже есть, например browser.get(query.title) должен вернуть заголовок страницы (текст внутри тега title внутри HTML)
* (element | collection | browser).perform(command.*) дождется прохождения команды, например browser.element('#approve').perform(command.js.click) или browser.all('.addvertisment').perform(command.js.remove)"""