"""Service module"""

import customtkinter as ctk


def make_label(
    self, text_l: str, row: int, column: int
) -> ctk.CTkLabel:
    """Make Label"""
    label: ctk.CTkLabel = ctk.CTkLabel(
        self,
        text=text_l,
        font=("Helvetica", 20),
        bg_color="#434343",
        corner_radius=10,
    )
    label.grid(
        row=row,
        column=column,
        sticky="nsew",
        pady=5,
        padx=5,
        ipady=5,
        ipadx=5,
    )
    return label


def make_entry(
    self, text_p: str, row: int, column: int
) -> ctk.CTkEntry:
    """Make Entry"""
    entry: ctk.CTkEntry = ctk.CTkEntry(
        self,
        placeholder_text=text_p,
        font=("Fira code", 18),
    )
    entry.grid(
        row=row,
        column=column,
        sticky="nsew",
        pady=5,
        padx=5,
        ipady=5,
        ipadx=5,
    )
    return entry


def make_btn(
    self, text_btn: str, row: int, col: int, command=None
) -> ctk.CTkButton:
    """make btn"""
    btn: ctk.CTkButton = ctk.CTkButton(
        self, text=text_btn, font=("Helvetica", 22), command=command
    )
    btn.grid(
        row=row,
        column=col,
        sticky="nsew",
        pady=10,
        padx=10,
        ipady=5,
        ipadx=5,
    )
    return btn


if __name__ == "__main__":
    pass