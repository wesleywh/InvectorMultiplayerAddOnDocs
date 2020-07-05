import sys 
import os
from optparse import OptionParser
from MDParser import MDParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "--folder","-f",
        dest="folder",
        help="Path to the folder you want to build to docs for"
    )
    parser.add_option(
        "--dest","-d",
        dest="destination",
        help="Path to the output destination"
    )
    parser.add_option(
        "--ignoredir",
        dest="ignoredirs",
        nargs="*",
        default=[],
        help="The directory names to exclude."
    )
    (args, options) = parser.parse_args()
    mdparser = MDParser(args.folder, args.ignoredirs)
    mdparser.write_contents_to_files(mdparser.get_parsed_contents(), args.destination)
    mdparser.write_index_file(mdparser.get_parsed_contents(), args.destination)