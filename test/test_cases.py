#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description: 
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
import unittest
from unittest.mock import patch
from tkinter import Tk
from code.app import ToolUpdater, is_tool_installed

class TestToolUpdater(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = ToolUpdater(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_valid_input_update(self):
        with patch('builtins.input', side_effect=['1.0.0', '1.0.0']):
            self.app.update_meson_ninja_thread('1.0.0', '1.0.0')
            self.assertIn('Meson and Ninja updated successfully!', self.app.terminal.get("1.0", tk.END))

    def test_empty_input(self):
        with patch('builtins.input', side_effect=['', '1.0.0']):
            self.app.update_meson_ninja_thread('', '1.0.0')
            self.assertIn('Please provide valid version numbers.', self.app.terminal.get("1.0", tk.END))

    def test_invalid_version_format(self):
        with patch('builtins.input', side_effect=['1.0.0', 'invalid']):
            self.app.update_meson_ninja_thread('1.0.0', 'invalid')
            self.assertIn('Invalid version format. Please provide a valid version.', self.app.terminal.get("1.0", tk.END))

    def test_update_cancel(self):
        with patch('builtins.input', side_effect=['1.0.0', '1.0.0']):
            # Start the update process and then cancel
            self.app.update_meson_ninja_thread('1.0.0', '1.0.0')
            self.app.progress_bar.stop()  # Simulate cancellation
            self.assertIn('Update process cancelled.', self.app.terminal.get("1.0", tk.END))

    def test_install_cancel(self):
        with patch('builtins.input', side_effect=['1.0.0', '1.0.0']):
            # Start the installation process and then cancel
            self.app.install_meson_ninja_thread('1.0.0', '1.0.0')
            self.app.progress_bar.stop()  # Simulate cancellation
            self.assertIn('Installation process cancelled.', self.app.terminal.get("1.0", tk.END))

    def test_check_installed(self):
        with patch('your_script.is_tool_installed', side_effect=[True, True]):
            self.app.check_meson_ninja_thread()
            self.assertIn('Meson is installed.', self.app.terminal.get("1.0", tk.END))
            self.assertIn('Ninja is installed.', self.app.terminal.get("1.0", tk.END))

    def test_check_not_installed(self):
        with patch('your_script.is_tool_installed', side_effect=[False, False]):
            self.app.check_meson_ninja_thread()
            self.assertIn('Meson is not installed.', self.app.terminal.get("1.0", tk.END))
            self.assertIn('Ninja is not installed.', self.app.terminal.get("1.0", tk.END))

    def test_multiple_operations(self):
        with patch('builtins.input', side_effect=['1.0.0', '1.0.0']):
            self.app.update_meson_ninja_thread('1.0.0', '1.0.0')
        with patch('builtins.input', side_effect=['1.0.0', '1.0.0']):
            self.app.install_meson_ninja_thread('1.0.0', '1.0.0')
        with patch('your_script.is_tool_installed', side_effect=[True, True]):
            self.app.check_meson_ninja_thread()
            self.assertIn('Meson is installed.', self.app.terminal.get("1.0", tk.END))
            self.assertIn('Ninja is installed.', self.app.terminal.get("1.0", tk.END))

    def test_open_info_placeholder(self):
        self.app.open_info()
        self.assertIn('Placeholder for additional actions or information.', self.app.terminal.get("1.0", tk.END))

if __name__ == '__main__':
    unittest.main()
