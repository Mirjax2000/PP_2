"""Main app"""

import customtkinter as ctk
from rich.console import Console
from rich.traceback import install

from modules.service import make_btn, make_entry, make_label
from modules.connection import DB

install(show_locals=True)
console: Console = Console()


class App(ctk.CTk):
    """Main app"""

    def __init__(self) -> None:
        super().__init__()
        self.title("SQLAlchemy")
        self.minsize(400, 400)
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
        self.header: ctk.CTkLabel = make_label(
            self, "Vypocet B.M.I.", 0, 1
        )
        self.vaha: ctk.CTkLabel = make_label(
            self, "Zadejte vahu (kg):", 1, 0
        )
        self.vyska: ctk.CTkLabel = make_label(
            self, "Zadejte vysku (m):", 2, 0
        )
        self.result: ctk.CTkLabel = make_label(
            self, "Ciselny vysledek:", 4, 0
        )
        #
        self.vaha_entry: ctk.CTkEntry = make_entry(
            self, "vaha ...", 1, 1
        )
        self.vyska_entry: ctk.CTkEntry = make_entry(
            self, "vyska ...", 2, 1
        )
        self.vypocitat_btn: ctk.CTkButton = make_btn(
            self, "Vypocitat ", 3, 1, None
        )

        self.columnconfigure((0, 1), weight=1, uniform="a")


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
