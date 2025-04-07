# Task Tracker CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

Welcome to **Task_Tracker_CLI**, a command-line tool (CLI) for managing task lists. With this application, you can easily add, update, delete, mark (as in progress or done) and list tasks from the terminal.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributions](#contributions)
6. [License](#license)

---

## Features

- **Add task**: Add a new task with a description and is initially set to the `todo` status.
- **Update task**: Modify the description of an existing task.
- **Delete task**: Remove a task by its ID.
- **List tasks**: Display all tasks or filter by status (`todo`, `in-progress` or `done`) in a well-formatted table.
- **Mark task as in-progress**: Mark a task as `in-progress` by its ID.
- **Mark task as done**: Mark a task as `done` by its ID.
---

## Requirements

- Python 3.6 or higher.
- The `tabulate` library for formatting tables in the output.

---

## Installation

### Option 1: Use a virtal environment (recommended)

A virtual environment allows you to isolate this project's dependencies from other projects or tools installed on your system. Follow these steps to install the project in a virtual environment:

1. **Clone this repository to your local machine:**
   ```bash
   git clone https://github.com/aealvarezg/Task_Tracker_CLI.git
   cd Task_Tracker_CLI
   ```

2. **Create a virtual environment:**
   - On Linux/macOS:
     ```bash
     python3 -m venv venv
     ```
   - On Windows:
     ```bash
     python -m venv venv
     ```

   This will create a folder called `venv` in the project directory, which will contain the virtual environment.

3. **Activate the virtual environment:**
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   You'll know the virtual environment is active because you'll see `(venv)` at the beginning of the command line.

4. **Install project dependencies:**
   ```bash
   pip install .
   ```

5. **(Optional) Disable the virtual environment:**
   When you're done working on the project, you can deactivate the virtual environment by running:
   ```bash
   deactivate
   ```

### Option 2: Install directly on the system (without virtual environment)

If you prefer not to use a virtual environment, you can install the project directly into your global Python environment:

1. **Clone this repository to your local machine:**
   ```bash
   git clone https://github.com/aealvarezg/Task_Tracker_CLI.git
   cd Task_Tracker_CLI
   ```

2. **Install the project and its dependencies using `pip`:**
   ```bash
   pip install .
   ```

   > **Note:** If you are on an operating system like Linux or macOS, you may need to use `pip3` instead of `pip`:
   > ```bash
   > pip3 install .
   > ```

---

## Usage

Once installed, you can use the `task-cli` command in the terminal. Below are some usage examples:

### Add a task
```bash
task-cli add "Finish my homework"
```
**Output:**
```
╒══════╤════════════════════╤══════════╤═════════════════════╤═════════════════════╕
│   Id │ Description        │ Status   │ Created At          │ Updated At          │
╞══════╪════════════════════╪══════════╪═════════════════════╪═════════════════════╡
│    3 │ Finish my homework │ todo     │ 22:06:15 05/04/2025 │ 22:06:15 05/04/2025 │
╘══════╧════════════════════╧══════════╧═════════════════════╧═════════════════════╛
```

### List all tasks
```bash
task-cli list
```
**Output:**
```
╒══════╤════════════════════╤══════════╤═════════════════════╤═════════════════════╕
│   Id │ Description        │ Status   │ Created At          │ Updated At          │
╞══════╪════════════════════╪══════════╪═════════════════════╪═════════════════════╡
│    1 │ Buy bread          │ todo     │ 22:03:29 05/04/2025 │ 22:03:29 05/04/2025 │
├──────┼────────────────────┼──────────┼─────────────────────┼─────────────────────┤
│    2 │ Buy milk           │ todo     │ 22:04:07 05/04/2025 │ 22:04:07 05/04/2025 │
├──────┼────────────────────┼──────────┼─────────────────────┼─────────────────────┤
│    3 │ Finish my homework │ todo     │ 22:06:15 05/04/2025 │ 22:06:15 05/04/2025 │
╘══════╧════════════════════╧══════════╧═════════════════════╧═════════════════════╛
```

### Update a task
```bash
task-cli update 2 "Buy milk and coffee"
```
**Output:**
```
╒══════╤═════════════════════╤══════════╤═════════════════════╤═════════════════════╕
│   Id │ Description         │ Status   │ Created At          │ Updated At          │
╞══════╪═════════════════════╪══════════╪═════════════════════╪═════════════════════╡
│    2 │ Buy milk and coffee │ todo     │ 22:04:07 05/04/2025 │ 22:22:18 05/04/2025 │
╘══════╧═════════════════════╧══════════╧═════════════════════╧═════════════════════╛
```

### Mark a task as in-progress
```bash
task-cli mark-in-progress 3
```
**Output:**
```
╒══════╤════════════════════╤═════════════╤═════════════════════╤═════════════════════╕
│   Id │ Description        │ Status      │ Created At          │ Updated At          │
╞══════╪════════════════════╪═════════════╪═════════════════════╪═════════════════════╡
│    3 │ Finish my homework │ in-progress │ 22:06:15 05/04/2025 │ 22:12:34 05/04/2025 │
╘══════╧════════════════════╧═════════════╧═════════════════════╧═════════════════════╛
```

### Mark a task as done
```bash
task-cli mark-done 1
```
**Output:**
```
╒══════╤═══════════════╤══════════╤═════════════════════╤═════════════════════╕
│   Id │ Description   │ Status   │ Created At          │ Updated At          │
╞══════╪═══════════════╪══════════╪═════════════════════╪═════════════════════╡
│    1 │ Buy bread     │ done     │ 22:03:29 05/04/2025 │ 22:17:20 05/04/2025 │
╘══════╧═══════════════╧══════════╧═════════════════════╧═════════════════════╛
```

### List tasks by status
```bash
task-cli list --status in-progress
```
**Output:**
```
╒══════╤════════════════════╤═════════════╤═════════════════════╤═════════════════════╕
│   Id │ Description        │ Status      │ Created At          │ Updated At          │
╞══════╪════════════════════╪═════════════╪═════════════════════╪═════════════════════╡
│    3 │ Finish my homework │ in-progress │ 22:06:15 05/04/2025 │ 22:12:34 05/04/2025 │
╘══════╧════════════════════╧═════════════╧═════════════════════╧═════════════════════╛
```

### Delete a task
```bash
task-cli delete 1
```
**Output:**
```
╒══════╤═══════════════╤══════════╤═════════════════════╤═════════════════════╕
│   Id │ Description   │ Status   │ Created At          │ Updated At          │
╞══════╪═══════════════╪══════════╪═════════════════════╪═════════════════════╡
│    1 │ Buy bread     │ done     │ 22:03:29 05/04/2025 │ 22:17:20 05/04/2025 │
╘══════╧═══════════════╧══════════╧═════════════════════╧═════════════════════╛
```

---

## Contributions

Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a branch for your new feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m "Add new feature"`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request on GitHub.

Please ensure you follow good coding practices and include tests if possible.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Project source

This project is from [Roadmap](https://www.roadmap.sh). For more information, visit the [Task Tracker Project](https://roadmap.sh/projects/task-tracker).
