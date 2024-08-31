DISCLAIMER: The description below explains my process while working through and improving 
the code best I can as a beginner. Clearly, experienced programmers will know this from a
quick glance at the code, but for beginners, I hope this, along with the many comments in 
the code helps in some way.

## PASSWORD GENERATOR WORKING BETA

### Initial code worked perfectly:

This is a simple program to generate a strong password of specified length (default is 18 characters).
The password includes a mix of uppercase letters, lowercase letters, digits, and special characters.
Also ensures that the password contains at least one special character and at least two digits.
Password is then output to user

Initially, used a simple message box but was unable to copy the generated password, this would get old quickly.

So, instead used a tkinter 'entry' widget which worked perfectly.

Was even able to add a 'Copy to Clipboard' button on the output message.

----------------------------------------------------------------------------------

## PASSWORD GENERATOR 1.0 USABILITY IMPROVEMENTS

### Code completely re-written to implement customtkinter 

1. Import customtkinter instead of tkinter.
2. Use CTk and other customtkinter widgets for a consistent dark theme.

### Main Changes:

1. Replaced tkinter imports with customtkinter (ctk).
2. Used CTk, CTkToplevel, CTkEntry, and CTkButton for the GUI components.
3. Added ctk.set_appearance_mode("dark") and ctk.set_default_color_theme("dark-blue") for dark mode appearance settings.



### Added a button that calls a function to generate a new password.

1. Add a button that calls the function to generate a new password.
2. The function generates and displays the new password in the existing password entry field.

### Main Changes:

1. update_password() Function: A new function that generates a new password and updates the password_entry field.
2. generate_button: A new button labelled "Generate New Password" that triggers update_password() when clicked.
3. Refactored copy_to_clipboard(): Now copies the password from the password_entry widget.



### Added option for user to specify the number of characters in password

1. Added an Entry widget for the user to input the desired password length.
2. Modified the password generation function to use the specified length from the Entry widget.
3. Updated the UI to include this new input field and ensure the password updates accordingly when the length is changed.

### Main Changes:

1. Password Length Input: Added a CTkEntry widget (length_entry) for users to input the desired password length.
2. Validation and Default Length: When generating a new password, the update_password() function checks if the user input is a valid integer. If not, it defaults to a length of 18.
3. Dynamic Password Generation: The password is dynamically generated based on the user-specified length.

----------------------------------------------------------------------------------

## PASSWORD GENERATOR 2.0 USABILITY IMPROVEMENTS

### Changed the password length input box to a dropdown menu (combobox)

### Main Changes:

1. Combobox for Password Length:
     - Replaced the Entry widget for password length with a CTkComboBox widget
     - Populated the combobox with values ranging from 10 to 30 using a list comprehension

2. Set Default Length:
     - Set the default selected value in the combobox to "18" (Just a starting default)

3. Use Combobox Value for Length:
     - In the update_password() function, retrieve the selected length using length_combobox.get() and convert it to an integer.

----------------------------------------------------------------------------------

## PASSWORD GENERATOR 3.0 USABILITY IMPROVEMENTS

### Replaced (annoying) messagebox with password copied to clipboard on bottom of main window

### Main Changes:

1. Status Label (status_label):
     - A CTkLabel widget named status_label is added to the bottom of the window. This label is initially empty and is used to display messages like "Password copied to clipboard!".

2. Updating the Status Label:
     - In the copy_to_clipboard() function, the text of status_label is updated to "Password copied to clipboard!" whenever the password is successfully copied to the clipboard.
     - In the update_password() function, the status_label text is cleared each time a new password is generated.
  



```python:
import customtkinter as ctk
from tkinter import filedialog, Tk, Listbox
import pygame
import os

# Initialize Pygame Mixer for audio playback
pygame.mixer.init()

# Set the appearance mode for CustomTkinter
ctk.set_appearance_mode("dark")  # Set to 'dark' mode
```

Test text
