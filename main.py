"""Main app"""

import customtkinter as ctk
from rich.console import Console
from rich.traceback import install

from modules.service import make_btn, make_entry, make_label
from modules.service import bmi_calc, ctk_init

from modules.connection import engine

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
        self.vypocitat_btn = make_btn(
            self,
            "Vypocitat ",
            3,
            1,
            lambda: self.bmi(
                self.vaha_entry.get(), self.vyska_entry.get()
            ),
        )

        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(6, weight=0, minsize=20, uniform="b")

    def bmi(self, vaha: str, vyska: str):
        """prenesene volani na bmi_calc v service"""
        vaha_kg: float = float(vaha)
        vyska_m: float = float(vyska)
        result_num, result_txt = bmi_calc(vaha_kg, vyska_m)
        self.usr_rslt_num.configure(text=result_num)
        self.usr_rslt_txt.configure(text=result_txt)


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
