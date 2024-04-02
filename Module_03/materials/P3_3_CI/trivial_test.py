from social_status import get_social_status


def check_if_can_get_child_status():
    age = 33
    expected_result = 'child'
    function_result = get_social_status(age)
    # if function_result == expected_result:
    #     print('it WORKS')
    # else:
    #     print('it DOES NOT works')
    assert function_result == expected_result, 'Not matched'


def check_if_can_get_adult_status():
    age = 33
    expected_result = 'adult'
    function_result = get_social_status(age)
    # if function_result == expected_result:
    #     print('it WORKS')
    # else:
    #     print('it DOES NOT works')
    assert function_result == expected_result, 'Not matched'



if __name__ == '__main__':
    check_if_can_get_child_status()
    check_if_can_get_adult_status()