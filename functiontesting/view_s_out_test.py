import subprocess
import unittest
from unittest.mock import patch
from my_module import view_s_output

class TestViewSOutput(unittest.TestCase):

    @patch('builtins.input', side_effect=['12345'])
    @patch('subprocess.Popen')
    def test_view_s_output(self, mock_popen, mock_input):
        mock_process = mock_popen.return_value
        mock_process.communicate.return_value = (b'User|Start|End|Elapsed|JobID|JobName|State|ExitCode\master|2023-04-10T10:00:00|2023-04-10T11:00:00|01:00:00|77777|ethanjob|COMPLETED|0:0\n', None)
        view_s_output()
        mock_popen.assert_called_once_with(['sacct', '-o', 'User,Start,End,Elapsed,JobID,JobName,State,ExitCode', '-j', '12345'], stdout=subprocess.PIPE)
        self.assertEqual(mock_process.communicate.call_count, 1)
        self.assertEqual(mock_process.communicate.call_args_list[0][0], ())
        self.assertEqual(mock_process.returncode, 0)

if __name__ == '__main__':
    unittest.main()

