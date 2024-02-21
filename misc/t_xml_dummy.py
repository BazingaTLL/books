import xmlschema

schema = xmlschema.XMLSchema("t_xml/data/t_xsd(2).xsd")

root_element = schema.root_elements[0]
print(root_element, root_element.type.local_name)

for item in root_element.type.attributes:
    print(item, item.type.local_name)