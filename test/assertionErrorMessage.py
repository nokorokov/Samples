# Assert expected and actual result and modify error text
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f"Expected {expected_result}, got {actual_result}"