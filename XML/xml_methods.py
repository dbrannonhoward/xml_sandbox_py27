import xml.etree.ElementTree as ET
from Constants.file_extension_constants import xml_extension
import os


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


# Print elements in the xml tree with the tag_string
def print_elements_by_tag(xml_root, tag_string):
    print 'Searching xml_root for ' + str(tag_string)
    for tag in xml_root.iter(tag_string):
        print tag.attrib


def print_by_iter(xml_root, iter_string):
    print 'Printing by iter : ' + str(iter_string)
    for some_iter in xml_root.iter(iter_string):
        print some_iter.tag  # this is a str
        print ' is of type ' + str(type(some_iter.tag))
        print some_iter.attrib  # this is a dict
        print ' is of type ' + str(type(some_iter.attrib))


def print_all_values_with_key(xml_root, iter_string, key_filter):
    print 'Printing all dict values where key is : ' + str(key_filter)
    for some_iter in xml_root.iter(iter_string):
        attrib_dict = some_iter.attrib  # this is a dict
        for key in attrib_dict:
            if key == key_filter:
                print attrib_dict[key]


def print_root_attrib(xml_root):
    print 'Printing root attributes'
    print xml_root.attrib


def print_root_children(xml_root):
    print 'Printing root children tags'
    for child in xml_root:
        print child.tag


def print_root_children_attribs(xml_root):
    print 'Printing root children attributes'
    for child in xml_root:
        print child.attrib


def print_root_tag(xml_root):
    print 'Printing root tag'
    print xml_root.tag


# / eof / #
