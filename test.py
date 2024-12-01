"""test"""

from sqlalchemy import text
from modules.connection import session
from rich.console import Console

console: Console = Console()

with session.connection() as conn:
    result = conn.execute(text("SELECT * FROM bmis;"))
    console.print(result.fetchone())
