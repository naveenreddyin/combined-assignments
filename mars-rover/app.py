# imports come here
import sys, logging

from utils.parser import parse

# main function which is our entry point
def main():
    logging.info("starting...")
    # check for args and if file not specified gracefully exit
    # as not point going ahead
    if len(sys.argv) in [0, 1]:
        sys.exit("file was not passed.")
    parse(sys.argv[1])


if __name__ == "__main__":
    """
    Ye ye here we go!
    """
    main()
