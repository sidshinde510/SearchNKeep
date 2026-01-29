import os
import re

def search_files():
    # Input field for the search term and the starting directory
    search_term = input("Enter the alphanumeric string or number to search for: ")
    root_path = input("Enter the directory path to start search (e.g., . or C:/Users): ")

    # Regex to match the exact search term within alphanumeric contexts
    # If you want to find ANY alphanumeric string, use r'[a-zA-Z0-9]+'
    pattern = re.compile(re.escape(search_term))

    output_file = "output.txt"

    print(f"Searching for '{search_term}' in {os.path.abspath(root_path)}...")

    with open(output_file, "w", encoding="utf-8") as out:
        for root, dirs, files in os.walk(root_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                try:
                    # 'rb' mode + 'latin-1' or errors='ignore' allows us to read binary files
                    # as text without crashing on non-UTF-8 characters.
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line_num, line in enumerate(f, 1):
                            if pattern.search(line):
                                result = f"FILE: {file_path}\nLINE {line_num}: {line.strip()}\n{'-'*40}\n"
                                out.write(result)
                                # Optional: print to console so you see progress
                                # print(f"Found in {file_path}")
                                
                except Exception as e:
                    # Skip files that absolutely cannot be opened (system locked, etc.)
                    continue

    print(f"\nSearch complete. Results saved to {os.getcwd()}/{output_file}")

if __name__ == "__main__":
    search_files()
