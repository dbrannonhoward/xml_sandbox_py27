from gnosis.xml.pickle import XML_Pickler
import json
import os
import xmltodict

xml_files_dir = '/home/airquality/PycharmProjects/xml_files'
xml_filename = 'simple.xml'
xml_file_full_path = os.path.join(xml_files_dir, xml_filename)
# print xml_file_full_path

os.chdir(xml_files_dir)
print os.getcwd()

with open('simple.xml') as x_file:
    doc = xmltodict.parse(x_file.read())
    output_file = open('output.txt', 'a')
    output_file.write(str(doc))
    output_file.close()
