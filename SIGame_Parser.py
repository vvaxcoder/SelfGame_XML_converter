import os
import xml.etree.ElementTree as ET
import shutil

base_path = os.path.dirname(os.path.realpath(__file__))

dataDict = {}

class SIGame_Parser:
    def createXMLFromTemplate(self):
        # create xml file from template and copy it into current directory
        new_xml_file = os.path.join("parsed", "content.xml")
        # shutil.copy("template_old.xml", "parsed/content.xml")
        shutil.copy("template_old.xml", new_xml_file)


if __name__ ==  '__main__':
    parser = SIGame_Parser()

    print("start creating xml file from template and copy it into current directory...")
    parser.createXMLFromTemplate()
    print("xml file created.")