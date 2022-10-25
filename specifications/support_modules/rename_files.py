import os
import re

os.getcwd()
# collection = "C:/Users/carur/IdeaProjects/specifications/Literature Library"

def change(filename):
    match = re.match(r"(.*?)( manual| catalogue| wiring| specs| dimensions and ratings| emmissions| heating surface| parts list| datasheet| model data| body guide| installation| data sheet| insert)(.*?)(\.pdf)", filename)
    print(match)
    if match:
        print("".join(match.group(1, 3, 2, 4)))
        return "".join(match.group(1, 3, 2, 4))
    else:
        return filename


for i, filename in enumerate(os.listdir(collection)):
    os.rename(collection + "/" + filename, collection + "/" + change(filename))
