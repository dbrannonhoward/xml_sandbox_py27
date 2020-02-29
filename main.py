from directories import filter_file_list_by_ext, initialize_directories, \
    list_of_files_in_dir, print_directories
from file_extensions import *

filter_extension = xml_extension

# Initialize the working directories and print to console
cdir, pdir, odir, xdir = initialize_directories()
print_directories(cdir, pdir, odir, xdir)

# Get list() of files from directory, print it
xdir_list = list_of_files_in_dir(xdir)
print 'The file list is : ' + str(xdir_list)
# Filter files of a specific extension into a list(), print it
filtered_file_list = filter_file_list_by_ext(xdir_list, filter_extension)
print filtered_file_list

# Check to see if a file is XML


# / eof / #
