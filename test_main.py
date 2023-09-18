# Test main.py

import polars as pl
from main import load_data, calculate_stat, build_histogram


def test_calculate_stat():
    result1 = load_data["flipper_length_mm"].median()
    assert result1 == 197.0


def test_hist():
    result2 = build_histogram()
    assert result2 is not None


if __name__ == "__main__":
    test_calculate_stat()
    build_histogram()
