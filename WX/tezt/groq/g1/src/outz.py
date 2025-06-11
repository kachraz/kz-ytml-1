import io
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from rich import inspect as rich_inspect
from rich.console import Console
from rich.traceback import install

# Enable rich tracebacks for debugging
install()
console = Console()


def save_text_as_image(text, directory="rez", label="output"):
    """
    Saves 'text' as an image file in 'directory', using 'label' and a detailed timestamp in the filename.
    """
    try:
        dir_path = Path(directory)
        dir_path.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        file_path = dir_path / f"{label}_{timestamp}.png"

        # Create an image with the text
        font = ImageFont.load_default()
        image = Image.new('RGB', (800, 600), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Split the text into lines and draw each line
        y = 10
        for line in text.split('\n'):
            draw.text((10, y), line, fill=(0, 0, 0), font=font)
            y += 20

        image.save(file_path)
        console.print(f"[bold green]✅ Image saved to {file_path.resolve()}[/]")

    except Exception as e:
        console.print(f"[bold red]Error saving image: {e}[/]")


def inspect_and_save_as_image(var, label="inspected_object", directory="rez"):
    """
    Uses rich.inspect() to introspect 'var', captures the output,
    and saves it to an image file.
    """
    try:
        buf = io.StringIO()
        temp_console = Console(file=buf, force_terminal=True, width=120)

        rich_inspect(var, console=temp_console, methods=True, all=True)
        output_str = buf.getvalue()

        save_text_as_image(output_str, directory=directory, label=label)

    except Exception as e:
        console.print(f"[bold red]Error during inspection: {e}[/]")


#
