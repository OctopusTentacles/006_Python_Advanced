from social_status import get_social_status


def check_if_can_get_child_status():
    age = 8
    expected_result = 'child'
    function_result = get_social_status(age)
    if function_result == expected_result:
        print('it WORKS')
    else:
        print('it DOES NOT works')


if __name__ == '__main__':
    check_if_can_get_child_status()