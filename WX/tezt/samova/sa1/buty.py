# /////////////////////////////////////////////////////////////////////////////
# Main entrypoint for the sa1 module.
# /////////////////////////////////////////////////////////////////////////////

# --- Imports ---

from rich import print as rpr

from src.s1 import s1_file


# --- Funcz ---
def buty():
    s1_file()


if __name__ == "__main__":
    buty()
    rpr("[red]Sniffo... [/red]")
