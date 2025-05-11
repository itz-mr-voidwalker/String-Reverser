import tkinter as tk
import logging
from tkinter import messagebox
from tkinter import PhotoImage


class StringReverserApp:
    """A GUI application to reverse a given string input by the user."""

    def __init__(self, root):
        """Initialize the application with root window and configure its properties."""
        self.root = root
        self.colors = self.define_colors()
        self.setup_logging()
        self.window_config()
        self.create_widgets()

        # Bind Return key and Escape key to respective functions
        self.root.bind("<Return>", self.reverse_string_event)
        self.root.bind("<Escape>", self.on_escape)
        
        
    #Logging Setup
    def setup_logging(self):
        """Configure logging settings to track user actions and errors."""
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler("app.log", mode='w')
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        
    #Color Palatte
    def define_colors(self):
        """Define and return the color scheme for the app."""
        return {
            "bg": "#2E3440",
            "fg": "#D8DEE9",
            "entry_bg": "#3B4252",
            "entry_fg": "#ECEFF4",
            "btn_bg": "#5E81AC",
            "btn_fg": "#ECEFF4",
            "result_fg": "#A3BE8C",
        }

    #Window Configuration
    def window_config(self):
        """Configure the window properties like title, size, and background color."""
        self.root.title("String Reverser")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg=self.colors["bg"])
        icon = PhotoImage(file='icon.png')
        self.root.iconphoto(True, icon)


    #Creates Tkinter Widgets
    def create_widgets(self):
        """Create and configure all the necessary widgets for the application."""
        tk.Label(self.root, text="String Reverser", font=('Segoe UI', 20, 'bold'),
                 bg=self.colors["bg"], fg=self.colors["fg"]).pack(pady=20)

        self.entry_box = tk.Entry(self.root, bd=0, width=25, font=('Consolas', 16),
                                  bg=self.colors["entry_bg"], fg=self.colors["entry_fg"],
                                  insertbackground=self.colors["entry_fg"],
                                  highlightthickness=2, highlightbackground="#FFFFFF",
                                  highlightcolor="#FFFFFF")
        self.entry_box.pack(pady=10)
        self.entry_box.focus_set()

        self.result_label = tk.Label(self.root, text="", font=('Consolas', 14),
                                     fg=self.colors["result_fg"], bg=self.colors["bg"])
        self.result_label.pack(pady=30)

        submit_btn = tk.Button(self.root, text="Submit", command=self.reverse_string,
                               bg=self.colors["btn_bg"], fg=self.colors["btn_fg"],
                               font=('Segoe UI', 14), bd=0, activebackground="#81A1C1",
                               activeforeground=self.colors["fg"], padx=20, pady=5)
        submit_btn.pack()


    #Main Logic of reversing a string
    def reverse_string(self):
        """Reverse the string entered in the Entry box and display it."""
        user_input = self.entry_box.get().strip()

        # Input validation
        if not user_input:
            self.display_error("Input cannot be empty!")
            return

        # Reverse and display result
        try:
            reversed_string = user_input[::-1]
            self.logger.info(f"Reversed String: {reversed_string}")
            if len(reversed_string)>10:
                messagebox.showinfo('Reversed String', reversed_string) 
            else:
                self.result_label.config(text=f"Reversed String: {reversed_string}", fg=self.colors["result_fg"])
        except Exception as e:
            self.logger.error(f"Error while reversing string: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")


    #Keystrokes Handling
    def reverse_string_event(self, event=None):
        """Handle the event triggered by Return key or button click to reverse the string."""
        self.reverse_string()
    def on_escape(self, event=None):
        """Exit the application when Escape key is pressed."""
        self.logger.info("Escape key pressed. Closing the application.")
        self.root.quit()

    #Error Handling
    def display_error(self, message):
        """Display an error message in the result label."""
        self.result_label.config(text=message, fg="red")
        self.entry_box.focus_set()  # Focus back to the input field


# Main function to run the App
def main():
    """Initialize the Tkinter root window and run the String Reverser application."""
    root = tk.Tk()
    app = StringReverserApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
