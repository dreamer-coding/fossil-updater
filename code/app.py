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
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import subprocess
import threading
from queue import Queue

def is_tool_installed(tool_name):
    try:
        subprocess.run([tool_name, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

class ToolUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Updater")
        self.root.geometry("700x400")

        self.create_widgets()

    def create_widgets(self):
        self.meson_label = ttk.Label(self.root, text="Meson Version:")
        self.meson_entry = ttk.Entry(self.root)
        self.meson_entry.insert(0, "1.0.0")

        self.ninja_label = ttk.Label(self.root, text="Ninja Version:")
        self.ninja_entry = ttk.Entry(self.root)
        self.ninja_entry.insert(0, "1.11.1")

        self.update_button = ttk.Button(self.root, text="Update Meson and Ninja", command=self.update_meson_ninja, style='Orange.TButton')
        self.install_button = ttk.Button(self.root, text="Install Meson and Ninja", command=self.install_meson_ninja, style='Orange.TButton')
        self.check_button = ttk.Button(self.root, text="Check Meson and Ninja", command=self.check_meson_ninja, style='Orange.TButton')
        self.info_button = ttk.Button(self.root, text="Open Info", command=self.open_info, style='Orange.TButton')

        self.progress_bar = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')

        self.terminal = ScrolledText(self.root, height=10, state=tk.DISABLED, wrap=tk.WORD, background="black")
        self.terminal.tag_configure("custom", background="black", foreground="light blue", font="helvetica 10 bold")

        # Set up style for Orange buttons
        ttk.Style().configure('Orange.TButton', foreground='black', background='#FFA500')

        self.meson_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.meson_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.ninja_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.ninja_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.update_button.grid(row=2, column=0, padx=5, pady=5)
        self.install_button.grid(row=2, column=1, padx=5, pady=5)
        self.check_button.grid(row=2, column=2, padx=5, pady=5)
        self.info_button.grid(row=2, column=3, padx=5, pady=5)

        self.progress_bar.grid(row=3, columnspan=4, pady=10)
        self.terminal.grid(row=4, columnspan=4, padx=5, pady=5, sticky='nsew')

    def run_command_with_progress(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        while True:
            line = process.stdout.readline()
            if not line:
                break
            self.update_terminal(line)

        process.communicate()

    def update_terminal(self, message):
        self.terminal.configure(state=tk.NORMAL)
        self.terminal.insert(tk.END, message, "custom")
        self.terminal.yview(tk.END)
        self.terminal.configure(state=tk.DISABLED)

    def update_meson_ninja(self):
        meson_version = self.meson_entry.get()
        ninja_version = self.ninja_entry.get()

        threading.Thread(target=self.update_meson_ninja_thread, args=(meson_version, ninja_version)).start()

    def update_meson_ninja_thread(self, meson_version, ninja_version):
        self.progress_bar['value'] = 0
        self.progress_bar.start()

        self.update_terminal("Updating Meson and Ninja...\n")

        self.run_command_with_progress(["pip", "install", f"meson=={meson_version}", "--upgrade"])
        self.run_command_with_progress(["pip", "install", f"ninja=={ninja_version}", "--upgrade"])

        self.progress_bar.stop()
        self.progress_bar['value'] = 100
        self.update_terminal("\nMeson and Ninja updated successfully!\n")

    def install_meson_ninja(self):
        meson_version = self.meson_entry.get()
        ninja_version = self.ninja_entry.get()

        threading.Thread(target=self.install_meson_ninja_thread, args=(meson_version, ninja_version)).start()

    def install_meson_ninja_thread(self, meson_version, ninja_version):
        self.progress_bar['value'] = 0
        self.progress_bar.start()

        self.update_terminal("Installing Meson and Ninja...\n")

        self.run_command_with_progress(["pip", "install", f"meson=={meson_version}"])
        self.run_command_with_progress(["pip", "install", f"ninja=={ninja_version}"])

        self.progress_bar.stop()
        self.progress_bar['value'] = 100
        self.update_terminal("\nMeson and Ninja installed successfully!\n")

    def check_meson_ninja(self):
        threading.Thread(target=self.check_meson_ninja_thread).start()

    def check_meson_ninja_thread(self):
        self.update_terminal("Checking Meson and Ninja...\n")

        meson_installed = is_tool_installed("meson")
        ninja_installed = is_tool_installed("ninja")

        if meson_installed:
            self.update_terminal("Meson is installed.\n")
        else:
            self.update_terminal("Meson is not installed.\n")

        if ninja_installed:
            self.update_terminal("Ninja is installed.\n")
        else:
            self.update_terminal("Ninja is not installed.\n")

    def open_info(self):
        self.update_terminal("Fossil Learning is a dynamic educational platform that prioritizes engaging learning experiences. Through innovative technologies and a user-friendly interface, it offers a diverse range of courses to equip learners with the skills needed for success in various fields. Fossil Learning stands out for its commitment to quality content and interactive tools, making education accessible and enjoyable.\n")
        # Replace this with the appropriate information or action you want to perform
