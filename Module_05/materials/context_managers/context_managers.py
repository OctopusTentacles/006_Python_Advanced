import contextlib


class SavedFile():
    def __init__(self, path: str, mode='r') -> None:
        self.name = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file
    
    def __exit__(self, type, value, traceback):
        if self.file:
            self.file.close()


if __name__ == '__mane__':
    with SavedFile('some', 'w') as f:
        f.undefined('hello')