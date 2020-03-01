from Constants.path_and_file_constants import *
from directories import *
import logging
import os

os.chdir(parent_path)
os.chdir(log_path)


# # initialize logging variables
# def configure_logging(log_filename, log_level):
#     logging.basicConfig(log_filename, log_level)


def record_log_message():
    logging.makeLogRecord()


def shutdown_logging():  # run at the end of a program to close log handles
    logging.shutdown()

# / eof / #