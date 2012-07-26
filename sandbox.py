from lxml import etree
import sys

tree=etree.parse("/home1/srigamonti/projects/exciting_tests/runs/1341927374035/input.xml")
#print etree.tostring(tree)
root=tree.getroot()
root[1].text="hola mundo"

#print etree.tostring(tree)

for child in root:
    if child.tag=="keywords":
        print child.text

#tree.xpath('/input/keywords')[0].text="Hola mundo"

print " "
