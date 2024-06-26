import os
import json


class ClassGen():
    def __init__(self):
        all_classes = []
        for entry in os.listdir("data"):
            print(entry)
            with open(f"data/{entry}") as values:
                files = json.load(values)

            all_file_data = {}
            all_file_attributes = []

            for file in files:
                all_file_data[file["index"].replace("-","_")] = file
                for file_attribute in file.keys():
                    if file_attribute not in all_file_attributes:
                        all_file_attributes.append(file_attribute)

            entry = entry.replace("-", "_")
            all_file_data.update(
                {"entries": list(all_file_data.keys()), "attributes": all_file_attributes})
            top_class = type(entry, (object,), all_file_data)
            self.__setattr__(entry, top_class)
            all_classes.append(entry)

        self.all_classes = all_classes

init_file = "from . import entry_builder\n"

AllEntries = ClassGen()
for clas in AllEntries.all_classes:
    Output_file = ""
    names = clas.split("_")
    for index, name in enumerate(names):
        names[index] = name.capitalize()

    clas_name = "".join(names).replace(".json","")

    sub_class: object = AllEntries.__getattribute__(clas)

    Output_file += f"from . import entry_builder\nentries = {sub_class.entries}\nattributes = {sub_class.attributes}\n"
    init_file += f"from . import {clas_name}\n"

    for entry in sub_class.entries:
        data: dict = sub_class.__dict__[entry]

        Output_file += f"{entry} = entry_builder.entry_builder("
        tmp_data = []

        for key in data:
            str_format = str(data[key]).replace("\n", "\\n").replace("\\u2019","\'").strip()
            tmp_data.append(f"{key if key != 'class' else 'class_'} = {f"\'{str_format.replace("'","\\'")}\'" if isinstance(data[key], str) else str_format}")

        Output_file += f"{','.join(tmp_data)})\n"

    with open(f"dnd_api/{clas_name}.py","w") as out:
        out.write(Output_file)
with open("dnd_api/__init__.py", "w") as ini:
    ini.write(init_file)