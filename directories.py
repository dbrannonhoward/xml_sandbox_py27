from all_paths import output_path, xml_path
import os


# Return a list of files that end with file_ext
def filter_file_list_by_ext(file_list, file_ext):
    file_list_with_ext = list()
    try:
        for file_name in file_list:
            if str(file_name).endswith(file_ext):
                file_list_with_ext.append(file_name)
    except Exception as e:
        print str(e) + ' : could not filter file list by extension'
    return file_list_with_ext


def initialize_directories():  # initialize cdir, pdir, odir, xdir
    try:
        current_working_dir = os.getcwd()
        os.chdir('..')
        parent_working_dir = os.getcwd()
        output_dir = os.path.join(parent_working_dir, output_path)
        xml_dir = os.path.join(parent_working_dir, xml_path)
    except Exception as e:
        print str(e) + ' : could not initialize directories'
    return current_working_dir, parent_working_dir, output_dir, xml_dir


def list_of_files_in_dir(dir_path):  # print a list() of files in dir_path
    try:
        files_in_dir = os.listdir(dir_path)
    except Exception as e:
        print str(e) + ' : could not get a list of files in directory'
    return files_in_dir


def print_directories(cdir, pdir, odir, xdir):  # print cdir, pdir, odir, xdir full paths
    try:
        print 'CWD is ' + cdir  # current dir
        print 'PWD is ' + pdir  # parent dir
        print 'OWD is ' + odir  # output dir
        print 'XWD is ' + xdir  # xml dir
    except Exception as e:
        print str(e) + ' : could not print directories'

