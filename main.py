"""Main app"""

import os
from dotenv import load_dotenv
import customtkinter as ctk
from rich.console import Console
from rich.traceback import install
from sqlalchemy import create_engine

load_dotenv()

install(show_locals=True)

console: Console = Console()


class App(ctk.CTk):
    """Main app"""

    def __init__(self) -> None:
        super().__init__()
        self.title("SQLAlchemy")
        self.minsize(400, 600)
        self.resizable(False, False)
        self.update_idletasks()
        width: int = 380
        height: int = 400
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()
        x: int = screen_width // 2 - width // 2
        y: int = screen_height // 2 - height // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        #
        self.header: ctk.CTkLabel = self.make_label(
            "Vypocet B.M.I.", 0, 1
        )
        self.vaha: ctk.CTkLabel = self.make_label(
            "Zadejte vahu (kg): ", 1, 0
        )
        self.vyska: ctk.CTkLabel = self.make_label(
            "Zadejte vysku (m): ", 2, 0
        )
        self.result: ctk.CTkLabel = self.make_label(
            "Ciselny vysledek: ", 4, 0
        )
        #
        self.vaha_entry: ctk.CTkEntry = self.make_entry(
            "vaha ...", 1, 1
        )
        self.vyska_entry: ctk.CTkEntry = self.make_entry(
            "vyska ...", 2, 1
        )
        self.vypocitat_btn: ctk.CTkButton = ctk.CTkButton(
            self, text="Vypocitat ", font=("Helvetica", 22)
        )
        self.vypocitat_btn.grid(
            row=3,
            column=1,
            sticky="nsew",
            pady=10,
            padx=10,
            ipady=5,
            ipadx=5,
        )

    def make_label(
        self, text: str, row: int, column: int
    ) -> ctk.CTkLabel:
        """Make Label"""
        label: ctk.CTkLabel = ctk.CTkLabel(
            self, text=text, font=("Helvetica", 20), anchor="w"
        )
        label.grid(
            row=row, column=column, sticky="nsew", pady=10, padx=10
        )
        return label

    def make_entry(
        self, text: str, row: int, column: int
    ) -> ctk.CTkEntry:
        """Make Entry"""
        entry: ctk.CTkEntry = ctk.CTkEntry(
            self, placeholder_text=text, font=("Fira code", 18)
        )
        entry.grid(
            row=row, column=column, sticky="nsew", pady=10, padx=10
        )
        return entry


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
