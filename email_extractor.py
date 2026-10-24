"""
Email Extractor - Task Automation
CodeAlpha Python Programming Internship - Task 3

Automates a repetitive task: reading a text file, finding every email address
in it, removing duplicates and saving the results to a new file.
"""

import os
import re

# Files are looked up in the same folder as this script, so the program
# works no matter which folder the terminal is opened in.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INPUT = "sample_input.txt"
OUTPUT_FILE = "extracted_emails.txt"

# Pattern: name part, "@", domain name, a dot and an ending such as com or org
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def read_file(path):
    """Return the full text of a file, or None if it cannot be read."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: the file '{os.path.basename(path)}' was not found.")
    except (OSError, UnicodeDecodeError):
        print("Error: the file could not be read as a text file.")
    return None


def extract_emails(text):
    """Find all email addresses and return them sorted, without duplicates."""
    found = re.findall(EMAIL_PATTERN, text)

    unique = {}
    for email in found:
        # Compare in lowercase so Name@Mail.com and name@mail.com count once
        unique[email.lower()] = True

    return sorted(unique)


def save_emails(emails, path):
    """Write one email per line to the output file."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
        return True
    except OSError:
        print("Error: the results could not be saved.")
        return False


def main():
    print("=== EMAIL EXTRACTOR ===")
    name = input(f"Input file name (press Enter for '{DEFAULT_INPUT}'): ").strip()
    if name == "":
        name = DEFAULT_INPUT

    # A full path is used as given; a plain file name is looked up next to the script
    input_path = name if os.path.isabs(name) else os.path.join(BASE_DIR, name)

    text = read_file(input_path)
    if text is None:
        return

    emails = extract_emails(text)

    if not emails:
        print("No email addresses were found in the file.")
        return

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print("  " + email)

    output_path = os.path.join(BASE_DIR, OUTPUT_FILE)
    if save_emails(emails, output_path):
        print(f"\nResults saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
