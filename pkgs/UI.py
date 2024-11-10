import os
import sys
import customtkinter as ctk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.extract import ExtractSourceDestination
from pkgs.pdf2md import Pdf2MD
from pkgs.constants import (
    WIDTH_WINDOW_SIZE,
    HEIGHT_WINDOW_SIZE,
    RED,
    BLUE,
    ORANGE,
    FONT_NAME,
)


class ExtractAndMoveUI:
    def __init__(self) -> None:
        # define a JSON as default theme
        # ctk.set_default_color_theme("dark-blue.json")
        self.setup_window()
        self.setup_buttons()
        self.window.mainloop()

    def setup_window(self):
        """Initializes the main window settings."""
        self.window = ctk.CTk()
        self.window.title("Extract & Move")
        self.window.config(padx=40, pady=30)
        # Change the background color using configure
        self.window.configure(fg_color=BLUE)

        # position the Tkinter window at the center of the screen
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry("+%d+%d" % (x, y))
        self.window.geometry(f"{WIDTH_WINDOW_SIZE}x{HEIGHT_WINDOW_SIZE}")

    def setup_buttons(self):
        """Create the Search source folder button"""

        # instantiate the search and extract button (search and extract files from folders)
        self.source_folder = ExtractSourceDestination()
        # instantiate the search and convert button (search and convert the PDF to markdown)
        self.source_filename = Pdf2MD()

        self.source_folder_button = ctk.CTkButton(
            self.window,
            text="Browse Source Folder",
            command=self.source_folder.search_source,
            fg_color=RED,
            bg_color=BLUE,
            hover_color=ORANGE,
            border_width=1,
            border_color="black",
            font=ctk.CTkFont(family=FONT_NAME, weight="bold"),
            text_color="white",
        )
        self.source_folder_button.grid(row=3, column=2)

        self.source_folder_button = ctk.CTkButton(
            self.window,
            text="Browse PDF File",
            command=self.source_filename.search_filename,
            fg_color=RED,
            bg_color=BLUE,
            hover_color=ORANGE,
            border_width=1,
            border_color="black",
            font=ctk.CTkFont(family=FONT_NAME, weight="bold"),
            text_color="white",
        )
        self.source_folder_button.grid(row=4, column=2, pady=10)
