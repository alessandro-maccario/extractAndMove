# --- IMPORT PACKAGES --- #
import os
import sys
# import hupper  # for interactive update of the tkinter window after every changes to the code

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.UI import ExtractAndMoveUI


# def start_reloader():
#     """Reload the app at every changes in the code"""
#     hupper.start_reloader("app.main")


# ---------------------------- UI SETUP ------------------------------- #


def main():
    # instantiate the class ExtractAndMoveUI
    ui = ExtractAndMoveUI()


if __name__ == "__main__":
    main()
    # start_reloader()
