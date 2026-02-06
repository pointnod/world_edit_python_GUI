import os
import runpy


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    runpy.run_path(os.path.join(base_dir, "main.py"), run_name="__main__")


if __name__ == "__main__":
    main()
