from _datetime import datetime
import os


def logger(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.now().strftime('%d-%m-%Y время %H:%M:%S')
        old_func_name = old_function.__name__
        res = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'Время вызова функции - {call_time}, '
                       f'имя функции - {old_func_name}, '
                       f'аргументы функции - {args, kwargs}, '
                       f'значение функции - {res}')
        return res
    return new_function


def logger_func(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.now().strftime('%d-%m-%Y время %H:%M:%S')
            old_func_name = old_function.__name__
            res = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Время вызова функции - {call_time}, '
                           f'имя функции - {old_func_name}, '
                           f'аргументы функции - {args, kwargs}, '
                           f'значение функции - {res}')
            return res
        return new_function
    return __logger



def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(a=4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

