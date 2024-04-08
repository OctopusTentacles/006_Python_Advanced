# CORRECTION person.py

## 1. def get_age
- ERROR:
    > NameError: name 'datetime' is not defined

- FIXED:
    ```python
    import datetime
    ```
    ***

- FAIL:
    > AssertionError: -24 != 24
    ```python
    return self.yob - now.year
    ```
- FIXED:
    ```python
    return now.year - self.yob
    ```
    ***

## 2. def get_name
- OK



