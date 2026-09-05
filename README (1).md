

## Project Overview

This project is a command-line To-Do List application developed in
Python as part of the SYNENT Technology Internship.

The application allows users to add tasks, view existing tasks, delete
tasks by number, and exit the program.

## Objective

The objective of this task is to demonstrate practical Python
programming concepts including: - Lists - Functions - Loops -
Conditional statements - User input - Exception handling - Basic input
validation

## Features

-   Add new tasks
-   View all tasks with task numbers
-   Delete a selected task by number
-   Prevent empty tasks
-   Handle invalid menu choices
-   Handle invalid task numbers
-   Simple and user-friendly command-line interface

## Technologies Used

-   Python 3
-   Command Line Interface (CLI)

## Methodology

1.  A Python list is used to store tasks.
2.  A menu is displayed repeatedly using a `while` loop.
3.  The user selects an action from options 1--4.
4.  Separate functions handle adding, deleting, and viewing tasks.
5.  Task numbers are displayed using `enumerate()`.
6.  When deleting a task, the entered number is validated before
    removing the corresponding list item.
7.  `try-except` prevents the program from crashing when a non-numeric
    task number is entered.
8.  The program continues until the user selects Exit.

## Code Improvements

The uploaded initial version supported the main operations but had
limited validation and relied on task text for deletion. The reviewed
version improves it by: - Organizing logic into reusable functions -
Deleting tasks by task number instead of exact task text - Preventing
empty task entries - Handling invalid numeric input safely - Displaying
tasks in a numbered format - Adding a clear `main()` entry point -
Improving prompts and overall CLI presentation

## How to Run

1.  Install Python 3.
2.  Open the project folder in VS Code or a terminal.
3.  Run:

``` bash
python todo_list.py
```

4.  Choose an option from the menu.

## Example Output

``` text
===================================
           TO-DO LIST
===================================
1. Add Task
2. Delete Task
3. View Tasks
4. Exit
===================================
Enter your choice (1-4): 1
Enter your task: Complete Python assignment
Task added successfully!

Enter your choice (1-4): 3

Your Tasks:
1. Complete Python assignment
```

## Screenshots

Add screenshots to the `screenshots` folder showing: - Task added
successfully - Multiple tasks displayed - Task deleted successfully -
Invalid input handling

## Project Structure

``` text
Task-3-To-Do-List/
│
├── todo_list.py
├── screenshots/
│   ├── task_added.png
│   ├── view_tasks.png
│   ├── task_deleted.png
│   └── invalid_input.png
├── report/
│   └── To_Do_List_Report.pdf
└── README.md
```

## Result

The application successfully manages a list of tasks through a simple
command-line interface. Users can add, view, and delete tasks while
invalid inputs are handled without terminating the program.

## Conclusion

This project demonstrates practical Python programming using lists,
functions, loops, conditional logic, input validation, and exception
handling. The improved structure also makes the code easier to read,
maintain, and extend.
