import xml.etree.ElementTree as ET
from all_paths_all_files import *
from directories import *
from file_extensions import xml_extension
import os

os.chdir(parent_path)
os.chdir(xml_path)


def change_cwd_to_xml_dir(xml_files_dir):
    os.chdir(xml_files_dir)


def get_xml_tree_root(xml_file_name):
    xml_root = ET.parse(xml_file_name).getroot()
    return xml_root


def is_xml_file(file_name):
    try:
        if str(file_name).endswith(xml_extension):
            # print file_name + ' IS an XML file'
            return True
        else:
            # print file_name + ' IS NOT an XML file'
            return False
    except Exception as e:
        print str(e) + ' : could not determine if file is XML file'


def output_xml_contents_to_console(xml_file_name):
    print str(os.getcwd())
    with open(xml_file_name) as xml_file:
        print xml_file.read()


def print_root_children_to_console(xml_root):
    for child in xml_root:
        print 'child.tag is : ' + str(child.tag)
        print 'child.attrib is ' + str(child.attrib)



# / eof / #