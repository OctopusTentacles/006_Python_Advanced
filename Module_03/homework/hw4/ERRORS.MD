# CORRECTION person.py

## 1. def get_age
- ERROR:
    > NameError: name 'datetime' is not defined

- FIX:
    ```python
    import datetime
    ```
    ***

- FAIL:
    > AssertionError: -24 != 24
    ```python
    return self.yob - now.year
    ```
- FIX:
    ```python
    return now.year - self.yob
    ```
    ***


