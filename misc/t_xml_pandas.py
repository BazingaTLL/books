import xmlschema
import pandas as pd
from datetime import datetime as dt

schema = xmlschema.XMLSchema("t_xml/data/t_xsd.xsd")

root_name = schema.root_elements[0]
root_type = root_name.type

row_name = root_type.content[0]
row_type = row_name.type

col = []

for item in row_type.content:
    col.append(item.local_name)

print(col)

att = []

for item in row_type.attributes:
    att.append(item)

print(att)

df = {"id": [1, 2],
      "author": ["sivaram", "peram"],
      "title": ["go home", "the movies"],
      "price": [100, 150.12],
      "review": [5, 4.32],
      "pub_date": [dt.today().date(), dt.today().date()],
      "genre": ["drama", "crime"]}
df = pd.DataFrame(df)
print(df)

df.to_xml("t_xml/data/generated.xml", index=False, attr_cols=att, root_name=root_name.local_name, row_name=row_name.local_name, elem_cols=col)
