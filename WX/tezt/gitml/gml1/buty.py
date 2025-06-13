# /////////////////////////////////////////////////////////////
# Ver1 - Testing gh models code and gradio
# /////////////////////////////////////////////////////////////

# --- Imports ---

from rich.console import Console
from rich.rule import Rule

from src.utz import header1

console = Console()

# --- Helper Function ---

# This just draws a top line


def tline():
    console.print(Rule(title="[green]Execution Section[/green]",
                  characters="┉", style="bold green"))


def eline():
    console.print(Rule(title="[green] END[/green]",
                  characters="┉", style="bold red"))


# --- Main Function ---
def buty():
    header1("giml testing")


if __name__ == "__main__":
    tline()
    buty()
    eline()
