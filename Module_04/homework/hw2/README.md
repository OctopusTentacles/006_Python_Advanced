## Задача 2. Валидаторы. Создание
### Что нужно сделать
Довольно неудобно использовать встроенный валидатор `NumberRange` для ограничения числа по его длине. Создадим свой для поля phone.<br>
По своей сути валидатор — это функция, которая на вход принимает форму и поле, а в случае ошибки валидации выкидывает `ValidationError`.

```python
def number_length(form: FlaskForm, field: Field):
    if ...:
        raise ValidationError

number = IntegerField(validators=[InputRequired(), number_length])
```

Также можно реализовать его с помощью класса:

```python
class NumberLength:
    def __call__(self, form: FlaskForm, field: Field):
        if ...:
            raise ValidationError

number = IntegerField(validators=[InputRequired(), NumberLength()])
```

Создайте валидатор обоими способами. Валидатор должен принимать на вход параметры `min` и `max` — минимальная и максимальная длина, а также опциональный параметр `message` (см. рекомендации к предыдущему заданию).
### Советы и рекомендации
- Чтобы функциональный валидатор мог принимать параметры, саму функцию нужно декорировать:

```python
def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if ...:
            raise ValidationError

    return _number_length
```

### Что оценивается
- Валидатор создан как на основе функции, так и на основе класса.
- Валидатор принимает параметры `min`, `max` и `message`.
- Корректно обрабатывается длина числа.
