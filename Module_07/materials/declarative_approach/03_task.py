import logging
import logging.config

from log_config import dict_config


logging.config.dictConfig(dict_config)

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
