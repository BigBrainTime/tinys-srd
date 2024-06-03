import os
import json

class ClassGen():
    def __init__(self):
        all_classes = []
        for entry in os.listdir("data"):
            files = os.listdir(f"data/{entry}")

            all_file_data = {}
            all_file_attributes = []

            for file in files:
                with open(f"data/{entry}/{file}") as data:
                    file_data = json.load(data)

                file = file.replace(".json", "").replace("-", "_")

                all_file_data[file] = file_data
                for file_attribute in file_data.keys():
                    if file_attribute not in all_file_attributes:
                        all_file_attributes.append(file_attribute)

            entry = entry.replace("-", "_")
            all_file_data.update({"entries": list(all_file_data.keys()), "attributes": all_file_attributes})
            top_class = type(entry, (object,), all_file_data)
            self.__setattr__(entry, top_class)
            all_classes.append(entry)

        self.classes = all_classes

AllEntries = ClassGen()
for clas in AllEntries.classes:
    names = clas.split("_")
    for index, name in enumerate(names):
        names[index] = name.capitalize()
    clas_name = "".join(names)
    globals()[clas_name] = AllEntries.__getattribute__(clas)