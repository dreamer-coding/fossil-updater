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
from setuptools import setup, find_packages


setup(
    name="fossil-updater",
    version="0.1.0",
    author="Michael Gene Brockus (Dreamer)",
    author_email="michaelbrockus@gmail.com",
    description="Fossil Logic tool updater",
    long_description="Fossil Logic Updater tool, this allows you to manage your Meson and Ninja tools from a Tk interface allowing a user-friendly approach to getting the tools for anything Meson Build",
    url="https://github.com/dreamer-coding-555/fossil-updater",
    packages=find_packages(),  # Automatically find and include all packages
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apchie 2.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires=">=3.7",  # Specify the minimum Python version required
)
