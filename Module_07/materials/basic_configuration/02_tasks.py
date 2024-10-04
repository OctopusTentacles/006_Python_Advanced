import logging


# корневой логгер:
root = logging.getLogger()
root.setLevel(logging.DEBUG)

# handlers:

sub_handler = logging.StreamHandler()
sub_handler.setLevel(logging.DEBUG)

# formatter:
formatter = logging.Formatter(
    fmt='%(name)s || %(levelname)s || %(message)s || %(module)s,%(funcName)s:%(lineno)d'
)
sub_handler.setFormatter(formatter)

# логгер sub_1 с уровнем INFO:
sub_1 = logging.getLogger('sub_1')
sub_1.setLevel(logging.INFO)
sub_1.addHandler(sub_handler)

# logger sub_2 уровень унаследует от root:
sub_2 = logging.getLogger('sub_2')

# loger sub_sub_1 с уровнем DEBUG, наследует от sub_1 sub_handler:
sub_sub_1 = logging.getLogger('sub_1.sub_sub_1')
sub_sub_1.setLevel(logging.DEBUG)



def main():
    print(root.handlers)
    root.debug('This is a root debug message\n')

    print(sub_1.handlers)
    sub_1.debug('This debug message from sub_1 should not appear')
    sub_1.info('This is an info message from sub_1')

    print(sub_2.handlers)
    sub_2.info('This is an info message from sub_2')

    print(sub_sub_1.handlers)
    sub_sub_1.debug('This is a debug message from sub_sub_1')
    sub_sub_1.info('This is an info message from sub_sub_1')


if __name__ == '__main__':
    main()
