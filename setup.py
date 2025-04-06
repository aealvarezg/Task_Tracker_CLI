from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="task-cli",
    version="1.0.0",
    author="Alejandro Alvarez",
    author_email="alealvarezgarnica98@gmail.com",
    description="A command-line tool (CLI) for managing task lists.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aealvarezg/Task_Tracker_CLI.git",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "task-cli=taskcli.taskcli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)