# First checck if config.yaml is in the current directory
# Opening a file that doesn't exist will show if it is in the dir
try:
    catch = open("config.yaml")
    catch.close()
except:
    print("WARNING: config.yaml is not found in the current directory. Exiting...")
    exit(1)

from argparse import ArgumentParser
from os import getcwd                                                                                   
from os.path import isdir, isfile
from shutil import move, rmtree
from subprocess import call
from sys import exit
from tkinter import filedialog

from config_handling import citra_path, default_file_name, in_path, out_path

STREETPASS_LOCATION = r"\nand\data\00000000000000000000000000000000\sysdata\00010026\00000000"
EVENT_LOG_LOCATION = r"\nand\data\00000000000000000000000000000000\sysdata\00010026"
# Unused but will be used for future Citra config file edits
CITRA_CONFIG = r"\config"

if citra_path is None:
    print("WARNING: The path for your Citra installation is not set.")
    print("You can use the -setpath argument to set the path via command line")
    print("Or manually edit config.yaml and enter the path in the variable citra_path")

arguments = ArgumentParser()

# Command line arguments
arguments.add_argument(
    "-extract", help="Extract a cecd file. Useful for debugging.", action="store_true"
)
arguments.add_argument(
    "-streetpass",
    help="Initiate a Streetpass. Requires a cecd file from the Streetpass 2, Rise From The Ashes in this current directory or one specified in config.",
    action="store_true",
)
arguments.add_argument(
    "-set_path",
    help="Set the path of your Citra Location.",
    action="store_true",
)

parsed_args = arguments.parse_args()

# Command line variables
extract = parsed_args.extract
streetpass = parsed_args.streetpass
set_path = parsed_args.set_path


# Yaml module isn't used here although it probably should be
# I Haven't yet figured out how to edit specific variables
if set_path:
    path = input("\nSet your Citra Installation path. ")
    with open("config.yaml", "r+") as f:
        # This is not the most efficent way to read lines from a file
        # Memory managment isn't of a concern so for now it is fine
        lines = f.readlines()
        lines[5] = f"citra_path: {path}\n"
        f.truncate(0)
        # Seeking to the start of the file will prevent a ton of nulls from being written
        f.seek(0)
        for line in lines:
            f.write(line)
        print("Set path complete!")

# TODO: Edit Citra's config to automatically enable LLE cecd services
# TODO: Edit disa-extract.py to remove the need for absolute file paths
# TODO: Implement random auto-downloading of cecd files from the spreadsheet 
if streetpass:
    print("Running command...\n")
    call(
        ["python", "disa-extract.py", rf"{getcwd()}\{default_file_name}", getcwd()],
        cwd="Extractors",
    )
    print("Checking if path exists")
    if isdir(rf"{citra_path}{STREETPASS_LOCATION}\CEC"):
        rmtree(rf"{citra_path}{STREETPASS_LOCATION}\CEC")
    print("Moving CEC")
    move("CEC", rf"{citra_path}{STREETPASS_LOCATION}")


    print("\nStreetpass complete!")


if extract:
    if in_path is not None and out_path is not None:
        call(["python", "disa-extract.py", in_path, out_path], cwd="Extractors")
        print("Extraction process completed")
    else:
        # tkinter pop ups will be used if no constant path is set in config
        # By default pop ups will be used 
        in_path = filedialog.askopenfilename(title="Select the 0000000 File.")
        out_path = filedialog.askdirectory(title="Select the output directory.")
        call(["python", "disa-extract.py", in_path, out_path], cwd="Extractors")
        print("Extraction process completed")
