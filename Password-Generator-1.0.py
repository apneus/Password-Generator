import secrets
import string
import customtkinter as ctk 
from tkinter import messagebox

def create_pw(pw_length=18):

    # DEFINE CHARACTER SETS

    letters = string.ascii_letters  
    digits = string.digits  
    special_chars = string.punctuation  

    # Combine all character sets into one
    alphabet = letters + digits + special_chars

    # INITIALIZE VARIABLES

    # Variable to store generated password
    pwd = ''  
    # Flag to check if the generated password is strong
    pw_strong = False  

    # Loop until a password is generated
    while not pw_strong:
        # Reset password to empty before generating new one
        pwd = ''  
        # Generate password by randomly selecting characters from the combined alphabet
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        # CHECK THE GENERATED PASSWORD MEETS STRENGTH CRITERIA

        # Contains at least one special character
        if (any(char in special_chars for char in pwd) and  
                # Contains at least two digits
                sum(char in digits for char in pwd) >= 2):  
            # Set flag to True if criteria are met
            pw_strong = True  

    # Return the password
    return pwd  

def show_password():
    # Function to update the password in the Entry widget
    def update_password():
        # Get the desired length from the entry widget
        try:
            length = int(length_entry.get())
        except ValueError:
            length = 18  # Default to 18 if input is not valid
            length_entry.delete(0, 'end')
            length_entry.insert(0, "18")  # Set default value if invalid input

        # Generate a new password with the specified length
        new_password = create_pw(pw_length=length)
        # Clear the current entry
        password_entry.configure(state='normal')  # Temporarily enable editing
        password_entry.delete(0, 'end')
        # Insert the new password
        password_entry.insert(0, new_password)
        password_entry.configure(state='readonly')  # Set back to readonly

    # Function to copy the current password to clipboard
    def copy_to_clipboard():
        # Clear the clipboard
        root.clipboard_clear()  
        # Append the password to the clipboard
        root.clipboard_append(password_entry.get())  
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    # Create a new top-level window for displaying the password
    password_window = ctk.CTkToplevel()
    password_window.title("Generated Password")

    # Create an Entry widget to specify the password length
    length_label = ctk.CTkLabel(password_window, text="Password Length:")
    length_label.pack(pady=(10, 5))
    length_entry = ctk.CTkEntry(password_window, width=100)
    length_entry.insert(0, "18")  # Default length
    length_entry.pack(pady=(0, 10))

    # Create an Entry widget to display the password
    password_entry = ctk.CTkEntry(password_window, width=300, font=("Arial", 14))
    password_entry.pack(padx=10, pady=10)

    # Generate the initial password and display it
    password_entry.insert(0, create_pw())
    password_entry.configure(state='readonly')  # Set the Entry widget to readonly to prevent modifications

    # Button to generate a new password
    generate_button = ctk.CTkButton(password_window, text="Generate New Password", command=update_password)
    generate_button.pack(pady=5)

    # Button to copy the password to the clipboard
    copy_button = ctk.CTkButton(password_window, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_button.pack(pady=5)

if __name__ == '__main__':
    # Set appearance mode to 'dark'
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")  # You can choose other color themes as well

    # Initialize the customtkinter main window
    root = ctk.CTk()
    # Hide the main tkinter window since only a pop-up is needed
    root.withdraw()  

    # Call the function to generate and display the password
    show_password()  

    # Start the Tkinter event loop
    root.mainloop()
