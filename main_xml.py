from directories import *
from file_extensions import *
from xml_methods import *

filter_extension = xml_extension

# Initialize the working directories and print to console
cdir, pdir, odir, xdir = initialize_directories()
print_directories(cdir, pdir, odir, xdir)

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
# Print the contents to terminal
for filtered_file_name in filtered_file_list:
    print 'The filtered file name is ' + str(filtered_file_name)
    xml_root = get_xml_tree_root(filtered_file_name)
    print(type(xml_root))





# / eof / #