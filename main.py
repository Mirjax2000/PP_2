"""Main app"""

import customtkinter as ctk
from rich.console import Console
from rich.traceback import install

from modules.service import make_btn, make_entry, make_label, ctk_init
from modules.connection import DB

install(show_locals=True)
console: Console = Console()


class App(ctk.CTk):
    """Main app"""

    def __init__(self) -> None:
        super().__init__()
        ctk_init(self, 400, 400)
        #
        self.header = make_label(self, "Vypocet B.M.I.", 0, 1)
        self.vaha = make_label(self, "Zadejte vahu (kg):", 1, 0)
        self.vyska = make_label(self, "Zadejte vysku (m):", 2, 0)
        self.rslt_num = make_label(self, "Ciselny vysledek:", 4, 0)
        self.usr_rslt_num = make_label(self, "...", 4, 1)
        self.rslt_txt = make_label(self, "Textovy vysledek", 5, 0)
        self.usr_rslt_txt = make_label(self, "...", 5, 1)
        self.cnt_txt = make_label(self, "Pocet uzivatelu:", 7, 0)
        self.cnt_num = make_label(self, "...", 7, 1)
        #
        self.vaha_entry = make_entry(self, "vaha ...", 1, 1)
        self.vyska_entry = make_entry(self, "vyska ...", 2, 1)
        self.vypocitat_btn = make_btn(self, "Vypocitat ", 3, 1, None)

        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(6, weight=0, minsize=20, uniform="b")


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
