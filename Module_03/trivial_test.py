from social_status import get_social_status


def check_if_can_get_child_status():
    age = 8
    expected_result = 'child'
    function_result = get_social_status(age)