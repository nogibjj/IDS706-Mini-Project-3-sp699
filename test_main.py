# Test main.py

from main import calculate_stat, build_histogram


def test_calculate_stat():
    calculate_stat()


def test_hist():
    build_histogram()


if __name__ == "__main__":
    test_calculate_stat()
    build_histogram()
