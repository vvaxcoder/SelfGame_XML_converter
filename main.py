import os
import xml.etree.ElementTree as ET
import shutil

base_path = os.path.dirname(os.path.realpath(__file__))

dataDict = {}

# create xml file from template and copy it into current directory
new_xml_file = os.path.join("parsed", "content.xml")
# shutil.copy("template_old.xml", "parsed/content.xml")
shutil.copy("template_old.xml", new_xml_file)

xml_file1 = os.path.join(base_path, "content_new.xml")
print("base_path = ", base_path)
print("xml_file1 = ", xml_file1)

ET.register_namespace("", "https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xsd")

# read content_new.xml
tree1 = ET.parse(xml_file1)

root1 = tree1.getroot()
# print("root1 = ", root1.attrib)

# find info tag
for child in root1.find(".//{https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xsd}info"):
    # print(child.tag)

    if child.tag == "{https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xsd}authors":
        # print(child[0].text)
        dataDict["author"] = child[0].text

ET.register_namespace("", "http://vladimirkhil.com/ygpackage3.0.xsd")

# read content.xml
tree2 = ET.parse(new_xml_file)

root2 = tree2.getroot()
# print("root2 = ", root2.attrib)

# fill content.xml root tag
root2.attrib['name'] = root1.attrib['name']
root2.attrib['id'] = root1.attrib['id']
root2.attrib['date'] = root1.attrib['date']
root2.attrib['difficulty'] = root1.attrib['difficulty']
root2.attrib['logo'] = root1.attrib['logo']

for child in root2.find(".//{http://vladimirkhil.com/ygpackage3.0.xsd}info"):
    print(child.tag)

    if child.tag == "{http://vladimirkhil.com/ygpackage3.0.xsd}authors":
        # print(child[0].text)
        child[0].text = dataDict["author"]

# count rounds
# for child in root1:
#     if child.tag == "{https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xsd}rounds":
#         dataDict["round_count"] = len(child)
#
#         for rounds_child in child:
#             print("rounds_child = ", rounds_child.tag)

# count rounds
rounds_count = root1.find("rounds", {'': "https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xsd"})
print("rounds_count = ", len(rounds_count))
dataDict["round_count"] = len(rounds_count)

# for child in root1.find("rounds", {'': "https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xsd"}):
#     print("child = ", child.tag)

print("root2 = ", root2)
rounds_from_parsed = root2.find("rounds", {"": "http://vladimirkhil.com/ygpackage3.0.xsd"})
print("rounds_from_parsed = ", rounds_from_parsed)
round_from_parsed = rounds_from_parsed.find("round", {"": "http://vladimirkhil.com/ygpackage3.0.xsd"})
print("round_from_parsed = ", round_from_parsed)

loop_counter = dataDict["round_count"] - 1
print("loop_counter = ", loop_counter)

for i in range(0, loop_counter):
    rounds_from_parsed.append(round_from_parsed)

print("rounds_from_parsed len = ", len(rounds_from_parsed))
# root2.append(rounds_from_parsed)

tree2.write(new_xml_file)
