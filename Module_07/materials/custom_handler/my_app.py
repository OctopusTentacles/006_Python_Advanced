import logging
import logging.config
import inspect  # Импортируем inspect для получения информации о текущем вызове

from my_config import dict_config


# применяем конфигурацию:
logging.config.dictConfig(dict_config)

# определить логгеры:
root = logging.getLogger()
sub_1 = logging.getLogger('sub_1')
sub_2 = logging.getLogger('sub_2')
sub_sub_1 = logging.getLogger('sub_1.sub_sub_1')

class CustomLogger(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        # Получаем информацию о текущем вызове
        frame = inspect.currentframe().f_back
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        func = frame.f_code.co_name
        
        # Создаем record для текущего сообщения
        record = self.logger.makeRecord(
            self.logger.name,
            self.logger.level,
            filename,
            lineno,
            msg,
            kwargs.pop('args', ()),
            None,  # exc_info
            func,
            # Дополнительные данные, если нужно
            **kwargs
        )
        
        # Вызов вашей функции обработки
        handle_logging(record)
        return msg, kwargs

# Создайте адаптеры для логгеров
sub_1_adapter = CustomLogger(sub_1, {})
sub_2_adapter = CustomLogger(sub_2, {})
sub_sub_1_adapter = CustomLogger(sub_sub_1, {})

def main():
    print("=== Логирование от корневого логгера ===")
    root.debug('This is a root debug message\n', extra={'very': 'much'})

    print("\n=== Логирование от sub_1 ===")
    sub_1_adapter.debug('This debug message from sub_1 should not appear', extra={'very': 'much'})
    sub_1_adapter.info('This is an info message from sub_1', extra={'very': 'much'})
    sub_1_adapter.info('This message with extra', extra={'very': 'much'})

    print("\n=== Логирование от sub_2 (не должно передаваться root) ===")
    sub_2_adapter.info('This is an info message from sub_2', extra={'very': 'much'})

    print("\n=== Логирование от sub_sub_1 ===")
    sub_sub_1_adapter.debug('This is a debug message from sub_sub_1', extra={'very': 'much'})
    sub_sub_1_adapter.info('This is an info message from sub_sub_1', extra={'very': 'much'})

def handle_logging(record):
    # Печатаем содержимое record
    print("=== Содержимое record ===")
    print(vars(record))  # Выводим все атрибуты record

if __name__ == '__main__':
    main()
