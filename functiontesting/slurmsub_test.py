import unittest
from unittest.mock import patch
import os

def create_slurm_file(file_path):
    with open(file_path, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("#SBATCH --ntasks=1\n")
        f.write("#SBATCH --cpus-per-task=1\n")
        f.write("#SBATCH --mem-per-cpu=100M\n")
        f.write("echo 'Hello, world!'\n")

class TestSubmitSlurm(unittest.TestCase):

    @patch('builtins.input', side_effect=["nonexistent_file.sh", "/path/to/slurm.sh"])
    @patch('os.path.exists', side_effect=[False, True])
    @patch('os.system')
    def test_submit_slurm(self, mock_input, mock_exists, mock_system):
        # Call the function
        submit_slurm()
        
        # Check that os.path.exists was called with the correct argument
        mock_exists.assert_called_with("/path/to/slurm.sh")
        
        # Check that os.system was called with the correct arguments
        mock_system.assert_called_with("sbatch --job-name=MyJob --time=60 /path/to/slurm.sh ")
        
        # Check that the confirmation message was printed
        self.assertEqual("Job submitted successfully.\n", self.output.getvalue())

if __name__ == '__main__':
    unittest.main()

