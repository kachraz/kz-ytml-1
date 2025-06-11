import io
from datetime import datetime
from pathlib import Path

from rich import inspect as rich_inspect
from rich.console import Console
from rich.pretty import pretty_repr
from rich.traceback import install

install()
console = Console()


def save_output_to_markdown(output, directory="rez", label="output"):
    try:
        # Create the 'rez' directory if it doesn't exist
        dir_path = Path(directory)
        dir_path.mkdir(parents=True, exist_ok=True)

        # Generate unique timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        file_path = dir_path / f"{label}_{timestamp}.md"

        # Handle serialization
        try:
            content = pretty_repr(output)
        except Exception:
            content = repr(output)

        # Markdown content
        md = f"# {label}\n\n**Timestamp:** {timestamp}\n\n```\n{content}\n```\n"

        with file_path.open("w", encoding="utf-8") as f:
            f.write(md)

        console.print(f"[bold green]✅ Wrote:[/] {file_path.resolve()}")

    except Exception:
        console.print_exception(show_locals=True)


def inspect_and_save_to_markdown(var, label="inspected_object", directory="rez"):
    try:
        # Capture output using an in-memory string buffer
        buffer = io.StringIO()
        temp_console = Console(file=buffer, force_terminal=True, width=100)

        # Do the inspection (to buffer)
        rich_inspect(var, console=temp_console, all=True, methods=True)

        # Get string output
        output_str = buffer.getvalue()

        # Save to Markdown using earlier function
        save_output_to_markdown(output_str, directory=directory, label=label)

    except Exception:
        Console().print_exception(show_locals=True)
