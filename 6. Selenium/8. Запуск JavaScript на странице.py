"""
    Синтаксис webdriver.execute_script(script, *args).
В .execute_script() можно использовать следующие полезные параметры.
Посмотреть все события можно тут и тут, ниже приведены те, которые чаще всего используются при написании парсеров.

    • .execute_script("return arguments[0].scrollIntoView(true);", element) - прокручивает родительский контейнер элемента таким образом,
    чтобы element для которого вызывается scrollIntoView , был виден пользователю ;

    • .execute_script("window.open('http://parsinger.ru', 'tab2');") - создаст новую вкладку с именем "tab2";

    • .execute_script("return document.body.scrollHeight") - вернёт значение высоты элемента<body>;

    • .execute_script("return window.innerHeight") - вернёт значение высоты окна браузера;

    • .execute_script("return window.innerWidth") - вернёт значение ширину окна браузера;

    • .execute_script("window.scrollBy(X, Y)") - прокручивает документ на заданное число пикселей;

    • X - смещение в пикселях по горизонтали; • Y - смещение в пикселях по вертикали.

    • Для того чтобы получить фокус элемента, можно использовать .execute_script("return arguments[0].scrollIntoView(true);", element)
        где element это объект webdriver'a

    • .execute_script("alert('Ура Selenium')") - вызывает модальное окно Alert;

    • .execute_script("return document.title;") - вернёт title открытого документа;

    • .execute_script("return document.documentURI;") - возвращает URL документа;

    • .execute_script("return document.readyState;") - возвращает состояние загрузки страницы, вернёт complete если страница загрузилась;

    • .execute_script("return document.anchors;") - возвращает список всех якорей;

    • [x.tag_name for x in browser.execute_script("return document.anchors;")] - такой код даст возможность получить список всех тегов c якорями.
        Очень полезная инструкция, используется если при скроллинге мы не можем найти элемент для того чтобы "зацепится" за элемент;

    • .execute_script("return document.cookie;") - возвращает список файлов cookie, разделенных точкой с запятой;

    • .execute_script("return document.domain;") - возвращает домен текущего документа;

    • .execute_script("return document.forms;") -вернёт список форм;

    • window.scrollTo(x-coord, y-coord) - прокрутка документа до указанных координат;

    • x-coord пиксель по горизонтальной оси документа, будет отображён вверху слева;

    • y-coord пиксель по вертикальной оси документа, будет отображён вверху слева.

    • .execute_script("return document.getElementsByClassName('container');") - возвращает список всех элементов с заданным классом class="container";

    • .execute_script("return getElementsByTagName('container');") - возвращает список всех элементов с заданным именем name="container".
"""