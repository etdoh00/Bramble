import unittest
from unittest.mock import patch
import subprocess

class TestLaunchMinecraft(unittest.TestCase):
    # Define test case with mock input and subprocess run functions
    @patch('builtins.input', return_value='my-minecraft-pod')
    @patch('subprocess.run')
    def test_launch_minecraft(self, mock_run, mock_input):
        # Call the function being tested
        launch_minecraft()
        # Check if the input function was called with the correct prompt
        mock_input.assert_called_once_with("What would you like to call the pod?")
        # Check if the subprocess run function was called with the correct command and arguments
        mock_run.assert_called_once_with("helm install --version '4.6.1' --namespace minecraft --values minecraft.yaml my-minecraft-pod itzg/minecraft", shell=True)

if __name__ == '__main__':
    # Run the test case
    unittest.main()

