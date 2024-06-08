"""
Реализуйте контекстный менеджер, который будет игнорировать 
переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, 
то он прокидывается выше.

"""

from typing import Collection, Type, Literal
from types import TracebackType


class BlockErrors:
    """
    В конструкторе мы будем принимать коллекцию типов исключений, 
    которые необходимо игнорировать.
    """
    def __init__(self, errors: Collection) -> None:
        self.errors = errors

    def __enter__(self) -> None:
        """
        в данном случае ничего не делает, 
        но он необходим для корректного использования контекстного менеджера
        """

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        """
        Если тип исключения находится в списке игнорируемых (self.errors),
        метод возвращает True, что указывает на успешную обработку 
        исключения и его игнорирование. Если исключение 
        не из списка игнорируемых, метод возвращает None, 
        и исключение прокидывается выше по стеку вызовов.
        """
