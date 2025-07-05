import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# Output folder relative to Part1_SelectionAlgorithms/
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")


def _get_timestamp() -> str:
    """Returns the current timestamp as a string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def save_dataframe_to_csv(
    df: pd.DataFrame, base_filename: str, output_dir: str = OUTPUT_DIR
) -> None:
    """
    Saves a DataFrame to a timestamped CSV file in the specified output directory.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        base_filename (str): The base name for the CSV file (without extension).
        output_dir (str, optional): Directory to save the file. Defaults to OUTPUT_DIR.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = _get_timestamp()
    filename = f"{base_filename}_{timestamp}.csv"
    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)
    print(f"CSV saved to {filepath}")


def save_plot_to_file(base_filename: str, output_dir: str = OUTPUT_DIR) -> None:
    """
    Saves the current matplotlib/seaborn plot to a timestamped file in the specified output directory.

    Args:
        base_filename (str): The base name for the image file (without extension).
        output_dir (str, optional): Directory to save the file. Defaults to OUTPUT_DIR.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = _get_timestamp()
    filename = f"{base_filename}_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)
    plt.tight_layout()
    plt.savefig(filepath)
    print(f"Plot image saved to {filepath}")
