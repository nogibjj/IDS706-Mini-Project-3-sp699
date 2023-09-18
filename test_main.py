# Test main.py

import polars as pl
from main import calculate_stat, build_histogram


def test_calculate_stat():
    result1 = calculate_stat()
    assert result1 is not None


def test_hist():
    result2 = build_histogram()
    assert result2 is not None


if __name__ == "__main__":
    test_calculate_stat()
    build_histogram()
