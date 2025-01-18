import os
import xml.etree.ElementTree as ET
import shutil

# create xml file from template and copy it into current directory
shutil.copy("template_old.xml", "content.xml")
