"""Traffic enforcement system entrypoint.

This project scaffold contains folders for configuration, models,
video assets, detectors, tracking, violation rules, dashboard, and tests.
"""

from pathlib import Path


def main():
    print("Traffic enforcement scaffold is ready.")
    print(f"Project root: {Path(__file__).parent.resolve()}")


if __name__ == "__main__":
    main()
