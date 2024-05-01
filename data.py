import random


class BurgersTestData:
    AUTH_NAME = 'Dima'
    AUTH_EMAIL = 'dima1989@yandex.ru'
    AUTH_PASSWORD = '666666'
    AUTH_RANDOM_EMAIL = f'verakuzmina7{random.randint(100, 999)}@yandex.ru'
    AUTH_PASSWORD_NEGATIVE = f'{random.randint(00000, 99999)}'
