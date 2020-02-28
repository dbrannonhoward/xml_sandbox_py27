from all_paths import output_path, xml_path
import os


def filter_file_list_by_ext(file_list, file_ext):  # remove files in file_list that aren't of type file_ext
    print 'todo'


def initialize_directories():  # initialize cdir, pdir, odir, xdir
    current_working_dir = os.getcwd()
    os.chdir('..')
    parent_working_dir = os.getcwd()
    output_dir = os.path.join(parent_working_dir, output_path)
    xml_dir = os.path.join(parent_working_dir, xml_path)
    return current_working_dir, parent_working_dir, output_dir, xml_dir


def list_of_files_in_dir(dir_path):  # print a list() of files in dir_path
    files_in_dir = os.listdir(dir_path)
    print files_in_dir


def print_directories(cdir, pdir, odir, xdir):  # print cdir, pdir, odir, xdir full paths
    print 'Current Working Dir is ' + cdir  # current_working_dir
    print 'Parent Working Dir is ' + pdir  # parent_working_dir
    print 'Output path is ' + odir  # output_path
    print 'Output Working Dir is ' + odir  # output_dir
    print 'XML path is ' + xdir  # xml_path
    print 'XML Working Dir is ' + xdir  # xml_dir

