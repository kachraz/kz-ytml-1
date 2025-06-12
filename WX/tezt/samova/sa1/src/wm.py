from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Union


def save_to_markdown(
    content: Union[str, List, Dict, Any],
    prefix: str = "output",
    directory: str = ".",
    header_level: int = 1,
    include_time: bool = True
) -> Path:
    """
    Saves content to a markdown file with date and optionally time appended to the filename.

    Args:
        content: Content to save (str, list, dict, or any object with __str__)
        prefix: Filename prefix before the date
        directory: Output directory
        header_level: Markdown header level (1-6) if content needs a title
        include_time: Whether to include time in filename (default: True)

    Returns:
        Path to the created markdown file

    Example:
        save_to_markdown(["Item 1", "Item 2"], "my_list")
        # Creates: my_list_2024-02-20_14-30-45.md
    """
    # Create directory if needed
    Path(directory).mkdir(parents=True, exist_ok=True)

    # Convert content to proper Markdown format
    markdown_content = _convert_to_markdown(content, header_level)

    # Generate filename with date and time
    now = datetime.now()
    date_part = now.strftime("%Y-%m-%d")
    if include_time:
        time_part = now.strftime("%H-%M-%S")
        filename = f"{prefix}_{date_part}_{time_part}.md"
    else:
        filename = f"{prefix}_{date_part}.md"

    filepath = Path(directory) / filename

    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    return filepath


def _convert_to_markdown(content: Any, header_level: int = 1) -> str:
    """Helper function to convert different types to Markdown"""
    if isinstance(content, str):
        return content
    elif isinstance(content, (list, tuple, set)):
        return "\n".join(f"- {item}" for item in content)
    elif isinstance(content, dict):
        return "\n".join(f"- **{k}**: {v}" for k, v in content.items())
    else:
        # Fallback for other types
        header = "#" * header_level
        return f"{header} Report\n\n{str(content)}"
