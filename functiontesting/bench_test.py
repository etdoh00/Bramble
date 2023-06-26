# Test for benchmark function
def test_benchmark():
    # Test valid inputs
    with patch('builtins.input', side_effect=['p1, p2', '4']):
        benchmark()

    # Test invalid inputs for hosts
    with patch('builtins.input', side_effect=['p1, $%^&', '4', 'p3, p4']):
        benchmark()

    # Test invalid inputs for number of tasks
    with patch('builtins.input', side_effect=['p1, p2', 'abcd', '4']):
        benchmark()

    # Test invalid inputs for both hosts and number of tasks
    with patch('builtins.input', side_effect=['$%^&', 'abcd', 'p1, p2', '4']):
        benchmark()

