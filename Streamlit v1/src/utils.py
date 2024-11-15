from typing import Tuple

def parse_resolution(resolution: str) -> Tuple[int, int]:
    """Parse resolution string into width and height."""
    try:
        width, height = map(int, resolution.split('x'))
        return width, height
    except ValueError:
        raise ValueError(f"Invalid resolution format: {resolution}")

def calculate_ppi(resolution: str, screen_size: float) -> float:
    """Calculate the PPI (Pixels Per Inch) for a given resolution and screen size."""
    if screen_size <= 0:
        raise ValueError("Screen size must be greater than 0")
        
    width, height = parse_resolution(resolution)
    return ((width**2) + (height**2))**0.5/screen_size