from unittest.mock import patch
import io
import pytest
import os

def test_view_jobs_valid_input():
    # Simulate user input and expected output
    input_values = ['RUNNING', 'exit']
    expected_output = '1234 | my_job | RUNNING | 0:0 | 2022-01-01T00:00:00 | 2022-01-01T00:00:00 | 2022-01-01T00:00:00\n'
    
    # Mock the input() function to return pre-defined values
    with patch('builtins.input', side_effect=input_values):
        # Redirect stdout to a buffer to capture the output
        with io.StringIO() as buffer:
            # Call the function and capture the output
            with patch('sys.stdout', buffer):
                view_jobs()
                output = buffer.getvalue()

    # Assert that the output matches the expected output
    assert output == expected_output

def test_view_jobs_invalid_input():
    # Simulate user input and expected output
    input_values = ['INVALID', 'COMPLETED', 'exit']
    expected_output = 'Invalid job status. Please try again.\n'
    
    # Mock the input() function to return pre-defined values
    with patch('builtins.input', side_effect=input_values):
        # Redirect stdout to a buffer to capture the output
        with io.StringIO() as buffer:
            # Call the function and capture the output
            with patch('sys.stdout', buffer):
                view_jobs()
                output = buffer.getvalue()

    # Assert that the output matches the expected output
    assert output == expected_output


