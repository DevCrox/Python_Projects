# Password Generator

A modern and customizable password generator application built with Python and CustomTkinter.

## Features

- Generate secure passwords with customizable length (8-32 characters)
- Customize password complexity with options for:
  - Uppercase letters
  - Numbers
  - Special symbols
- Modern dark/light theme support (follows system theme)
- Copy password to clipboard with one click
- Regenerate password instantly
- Clean and intuitive user interface

## Requirements

- Python 3.x
- Required packages:
  - customtkinter
  - pyperclip
  - tkinter (usually comes with Python)

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install customtkinter pyperclip
```
3. Run the application:
```bash
python CustomPassGenerator.py
```

Alternatively, you can use the provided executable file `SolXPass_Setup_V1.exe` for direct installation on Windows.

## Usage

1. Launch the application
2. Select desired password length from the dropdown menu (8-32 characters)
3. Configure password complexity by toggling:
   - Uppercase letters
   - Numbers
   - Symbols
4. Click "Regenerate" to create a new password
5. Click "Copy" to copy the password to your clipboard

## Project Structure

```
Password Generator/
│
├── CustomPassGenerator.py    # Main application file
├── Assets/                   # Application resources
│   ├── Copy.png             # Copy button icon
│   └── Regenerate.png       # Regenerate button icon
└── SolXPass_Setup_V1.exe    # Windows installer
```

## Technical Details

The application uses:
- `customtkinter` for modern UI elements
- `string` module for character sets
- `random` module for secure password generation
- `pyperclip` for clipboard operations
- Resource path handling for both development and compiled environments

## Features Explained

### Password Generation
- Lowercase letters are always included
- Optional inclusion of:
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*()_+, etc.)

### User Interface
- Centered window placement
- System-theme integration (dark/light mode)
- Responsive layout
- Clear visual feedback
- One-click copy functionality
- Easy password regeneration

## License

This project is available for use under standard open-source terms.

## Version

Current Version: 1.0 