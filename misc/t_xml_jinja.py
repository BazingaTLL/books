"""
1. The root element should be the first element in the schema file.
2. does not support namespaces.
3. template should be defined globaly before calling recursive function.
4. Attributes can be strings only.
"""

import xmlschema

def element_details(element):
    element_name = element.local_name
    element_type = element.type

    attributes = []
    child_elements = []

    if element_type.is_complex() and element_type.is_extension():
        for i in element_type.attributes:
            attributes.append(i)
        for i in element_type.content:
            for j in i:
                child_elements.append(j)

    elif element_type.is_complex() and not element_type.is_extension():
        for i in element_type.attributes:
            attributes.append(i)
        for i in element_type.content:
            child_elements.append(i)

    return attributes, child_elements, element_name

def recursive(element, level, reference, key=None, parent=None):
    global template
    level += 1
    a, e, n = element_details(element)

    next_parent = parent + "['" + n + "']" if parent else n
    key = key + "['" + n + "']" if key else n
    
    if element.max_occurs is None:
        template += f"{{% for row{level} in {parent} %}}\n"
        key = f"row{level}"

    if element.type.is_complex():
        reference[next_parent] = "complex"
        if len(a) == 0:
            template += "  "*level + f"<{n}>\n"
        else:
            temp = ""
            for i in a:
                att_key = key + "['" + i + "']"
                reference[next_parent + "['" + i + "']"] = "string"
                temp += f'{i}="{{{{ {att_key} }}}}" '
            template += "  "*level + f"<{n} " + temp[:-1] + ">\n"
    else:
        reference[next_parent] = element.type.local_name
        template += "  "*level + f"<{n}>{{{{ {key} }}}}"

    for i in e:
        recursive(i, level, reference, key=key, parent=next_parent)

    if element.type.is_complex():
        template += "  "*level + f"</{n}>\n"
    else:
        template += f"</{n}>\n"

    if element.max_occurs is None:
        template += f"{{% endfor %}}\n"




template = """<?xml version="1.0" encoding="utf-8"?>\n"""

schema = xmlschema.XMLSchema("t_xml/data/t_xsd(2).xsd")

root_element = schema.root_elements[0]

level = -1
reference = {}
recursive(root_element, level, reference)

with open("t_xml/others/template.txt", "w") as fd:
    fd.write(template)

import json
with open("t_xml/others/t_template.json", "w") as fd:
    fd.write(json.dumps(reference))

import jinja2
import pandas as pd
from datetime import datetime as dt

df = {"id": [1, 2],
      "author": ["sivaram", "peram"],
      "title": ["go home", "the movies"],
      "price": [100, 150.12],
      "review": [5, 4.32],
      "pub_date": [dt.today().date(), dt.today().date()],
      "genre": ["drama", "crime"]}
df = pd.DataFrame(df)

data = {}
data[root_element.local_name] = df.to_dict("records")
print(data)

jinja_template = jinja2.Template(template)

with open("t_xml/data/generated(1).xml", "w") as fd:
    fd.write(jinja_template.render(data))
    