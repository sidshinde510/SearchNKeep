# SearchNKeep
A Python script that performs recursive directory scanning to find alphanumeric strings. Features robust encoding handling for binary files and exports results to a text file.

# Recursive File Content Searcher

A lightweight Python utility that recursively searches for specific alphanumeric strings or numbers within files in a directory tree. It handles various file encodings and outputs the findings to a text file for easy review.

## 🚀 Features

* **Recursive Search:** Walks through every subdirectory of the provided path.
* **Context Aware:** Captures the file path, line number, and the specific line of text where the match was found.
* **Robust Encoding Handling:** Uses `utf-8` with error ignoring to prevent crashes when reading binary or non-standard file types.
* **File Output:** Saves all results to `output.txt` rather than clogging the terminal window.

## 🛠️ Prerequisites

* Python 3.x
* No external libraries required (uses standard `os` and `re` modules).

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sidshinde510/SearchNKeep.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd SearchNKeep
    ```

## 💻 Usage

1.  Run the script:
    ```bash
    python3 searchnkeep.py
    ```
2.  **Enter the search term:** Type the string or number you want to find.
3.  **Enter the path:** Type the directory path to start the search (e.g., `.` for current directory or `C:/Users/Name/Documents`).

The script will generate an `output.txt` file in the current directory containing all matches.

## 📝 Example Output

The `output.txt` will look like this:

```text
FILE: C:\Projects\Data\logs.txt
LINE 42: Error: User 12345 failed login
----------------------------------------
FILE: C:\Projects\Data\config.json
LINE 12: "id": "12345",
----------------------------------------
