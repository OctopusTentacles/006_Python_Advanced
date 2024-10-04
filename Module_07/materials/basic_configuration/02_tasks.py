import logging


# handlers:
root_handler = logging.StreamHandler()
root_handler.setLevel(logging.DEBUG)

# sub_handler = logging.StreamHandler()
# sub_handler.setLevel(logging.DEBUG)

# formatter:
formatter = logging.Formatter(
    fmt='%(name)s || %(levelname)s || %(message)s || %(module)s,%(funcName)s:%(lineno)d'
)
root_handler.setFormatter(formatter)
# sub_handler.setFormatter(formatter)

# корневой логгер:
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(root_handler)


# логгер sub_1 с уровнем INFO:
sub_1 = logging.getLogger('sub_1')
sub_1.setLevel(logging.INFO)
# sub_1.addHandler(sub_handler)

# logger sub_2 уровень унаследует от root:
sub_2 = logging.getLogger('sub_2')
sub_2.propagate = False # Отключаем распространение для sub_2

# loger sub_sub_1 с уровнем DEBUG, наследует от sub_1 sub_handler:
sub_sub_1 = logging.getLogger('sub_1.sub_sub_1')
sub_sub_1.setLevel(logging.DEBUG)



def main():
    print("=== Логирование от корневого логгера ===")
    root.debug('This is a root debug message\n')

    print("\n=== Логирование от sub_1 ===")
    sub_1.debug('This debug message from sub_1 should not appear')
    sub_1.info('This is an info message from sub_1')

    print("\n=== Логирование от sub_2 (не должно передаваться root) ===")
    sub_2.info('This is an info message from sub_2')

    print("\n=== Логирование от sub_sub_1 ===")
    sub_sub_1.debug('This is a debug message from sub_sub_1')
    sub_sub_1.info('This is an info message from sub_sub_1')


if __name__ == '__main__':
    main()
