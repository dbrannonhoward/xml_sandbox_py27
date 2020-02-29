from all_paths_all_files import xml_sandbox_log_file, xml_sandbox_log_level
from directories import *
from file_extensions import *
from log_methods import shutdown_logging
# from log_methods import configure_logging
from xml_methods import *

filter_extension = xml_extension

# Initialize the working directories and print to console
cdir, pdir, odir, xdir, ldir = initialize_directories()
print_directories(cdir, pdir, odir, xdir, ldir)

# # Configure logging
# configure_logging(xml_sandbox_log_file, xml_sandbox_log_level)

# Get list() of files from directory, print it
xdir_list = list_of_files_in_dir(xdir)
print 'The unfiltered file list in ' + str(xdir) + ' is : ' + str(xdir_list)
# Filter files of a specific extension into a list(), print it
filtered_file_list = filter_file_list_by_ext(xdir_list, filter_extension)
print 'The filtered file list from ' + str(xdir) + ' is : ' + str(filtered_file_list)

# Change working dir to XML dir
change_cwd_to_xml_dir(xdir)
print 'The current working directory is : ' + str(os.getcwd())

# Check to see if any file in the dir is an XML file
# Iterates over the existing XML files in the working directory
for filtered_file_name in filtered_file_list:
    print 'The filtered file name is ' + str(filtered_file_name)
    xml_root = get_xml_tree_root(filtered_file_name)
    # print(type(xml_root))
    # print_root_children_to_console(xml_root)
    print_elements_by_tag(xml_root, 'country')
    print_elements_by_tag(xml_root, 'neighbor')
    print_elements_by_tag(xml_root, 'rank')


shutdown_logging()
# / eof / #
