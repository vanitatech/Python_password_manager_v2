# Password Manager

A small desktop password manager built with Python and Tkinter. It lets you enter an account name, email/username, and password, or generate a 12-character password and copy it to the clipboard.

## Features

- Generate a 12-character password using letters, digits, and punctuation.
- Copy a generated password to the clipboard.
- Save account details to a local text file after confirmation.

## Requirements

- Python 3
- Tkinter (usually included with Python; some Linux distributions package it separately)
- `pyperclip`

Install the external dependency with:

```bash
python -m pip install pyperclip
```

## Run

From this directory, run:

```bash
python main.py
```

On some systems, use `python3` instead of `python`.

## Use

1. Enter a website or service and an email/username.
2. Enter a password, or select **Generate Password**. Generated passwords are also copied to the clipboard.
3. Select **Add** and confirm the details to save them.

Saved entries are appended to `data.txt` in the project directory in the format `website | email/username | password`.

## Security note

This is an educational example, not a secure password vault. Passwords are stored in `data.txt` as plain text, and generated passwords use Python's `random` module rather than a cryptographically secure generator. Anyone who can access the file can read the saved passwords. Do not use it for real credentials; keep sensitive information out of the included data file and do not commit real secrets to source control.
