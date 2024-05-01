# Sprint_5
Данный проект тестирует UI интерфейс сайта: https://stellarburgers.nomoreparties.site/

Проект содержит в себе папку tests с файлами тестов, файл локаторов [locators.py](locators.py), файл фикстур [conftest.py](conftest.py), файл с авторизационными данными [data.py](data.py)  и [.gitignore](.gitignore)

Описание тестов из папки tests:

+ test_1_registration.py - Файл с тестами на Регистрацию <br>
        1. <font color="yellow">test_registration_positive</font> - проверка успешной регистрации<br>
        2. <font color="yellow">test_registration_negative</font> - проверка ошибки для некорректного пароля<br>
+ test_2_login.py - Файл с тестами на Вход<br>
        1. <font color="yellow">test_login_enter_button</font> - проверка входа по кнопке «Войти в аккаунт» на главной<br>
        2. <font color="yellow">test_login_lk_button</font> - проверка входа через кнопку «Личный кабинет»<br>
        3. <font color="yellow">test_login_link_enter_in_registration</font> - проверка входа через кнопку в форме регистрации<br>
        4. <font color="yellow">test_login_link_enter_in_password_recovery</font> - проверка входа через кнопку в форме восстановления пароля<br>
+ test_3_go_to_lk.py - Файл с тестами на Переход в личный кабинет<br>
        1. <font color="yellow">test_go_to_lk</font> - проверка перехода по клику на «Личный кабинет»<br>
+ test_4_transition_from_lk_to_construct.py - Файл с тестами на Переход из личного кабинета в конструктор<br>
        1. <font color="yellow">test_transition_from_lk_to_construct_button</font> - проверка перехода по клику на «Конструктор»<br>
        2. <font color="yellow">test_transition_from_lk_to_logo</font> - проверка перехода по клику на логотип Stellar Burgers<br>
+ test_5_logout.py - Файл с тестами на Выход из аккаунта<br>
        1. <font color="yellow">test_logout</font> - проверка выхода по кнопке «Выйти» в личном кабинете<br>
+ test_6_construct_transition_to_sections.py - Файл с тестами на Раздел "Конструктор"<br>
        1. <font color="yellow">test_transition_sauces</font> - проверка перехода на раздел «Булки»<br>
        2. <font color="yellow">test_transition_fillings</font> - проверка перехода на раздел «Соусы»<br>
        3. <font color="yellow">test_transition_rolls</font> - проверка перехода на раздел «Начинки»<br>