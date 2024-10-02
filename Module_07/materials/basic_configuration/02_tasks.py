import logging


# корневой логгер:
root = logging.getLogger()

# логгер sub_1 с уровнем INFO:
sub_1 = logging.getLogger('sub_1')
sub_1.setLevel(logging.INFO)

# logger sub_2 уровень унаследует от root:
sub_2 = logging.getLogger('sub_2')

# loger sub_sub_1 с уровнем DEBUG:
sub_sub_1 = logging.getLogger('sub_2.sub_sub_1')
sub_sub_1.setLevel(logging.DEBUG)



def main():
    ...


if __name__ == '__main__':
    main()
