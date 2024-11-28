"""BMI setek"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console: Console = Console()
table: Table = Table()
width, height = console.size


def main_panel(content: Table) -> Panel:
    """Hlavni panel"""
    hlavni_panel: Panel = Panel(
        content, title="B.M.I.", width=width, height=int(height / 1.2)
    )
    return hlavni_panel


def main_table() -> Table:
    """Hlavni Table"""
    hlavni_table: Table = Table()
    hlavni_table.add_column("jmeno")
    return hlavni_table


console.clear()
console.print(main_panel(main_table()))
