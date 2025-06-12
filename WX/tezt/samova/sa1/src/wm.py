# ??????????????????????????????????????????????????????
# writes output to markdown file
# ??????????????????????????????????????????????????????

from datetime import datetime
from pathlib import Path


def save_to_markdown(content, prefix: str = "output", directory: str = ".") -> Path:
    """
    Saves content to a markdown file with today's date appended to the filename.

    Args:
        content (str): The markdown content to save
        prefix (str): Filename prefix before the date (default: "output")
        directory (str): Output directory (default: current directory)

    Returns:
        Path: Path to the created markdown file

    Example:
        save_to_markdown("# My Data\n\n- Item 1\n- Item 2", "my_report")
        # Creates: ./my_report_2024-02-20.md
    """
    # Create directory if it doesn't exist
    Path(directory).mkdir(parents=True, exist_ok=True)

    # Generate filename with today's date
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{prefix}_{today}.md"
    filepath = Path(directory) / filename

    # Write content to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath
