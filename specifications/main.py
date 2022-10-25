import os
import shutil

from specifications.items.plant import Plant
from specifications.items.fuse_model import FuseModel
from specifications.items.fuse import Fuse

from specifications.item import Item
from specifications.support_modules.html import HTML

dirname = os.path.dirname(__file__)
docs_folder = os.path.join(dirname, "..", "docs")
website_folder = os.path.join(dirname, "..", "website")

for subclass in Item.__subclasses__():

    # Skip unused Item Subclass
    if not hasattr(subclass, "items"):
        continue

    # Create Individual Item Pages
    for item in list(subclass.items):
        os.makedirs(os.path.join(website_folder, item.class_kebab()), exist_ok=True)
        with open(os.path.join(website_folder, item.class_kebab(), f'{item.item_kebab()}.html'),
                  "w") as f:
            f.write(HTML.item_html(item))

    # Copy Docs for Subclass
    os.makedirs(os.path.join(website_folder, subclass.class_kebab()), exist_ok=True)
    for doc in subclass.docs:
        if not os.path.exists(os.path.join(website_folder, subclass.class_kebab(), doc.filename)):
            shutil.copy(os.path.join(docs_folder, doc.filename), os.path.join(dirname, "..", website_folder, subclass.class_kebab(), doc.filename))

    # Create Subclass Page
    with open(os.path.join(website_folder, subclass.class_kebab(), f'{subclass.class_kebab()}.html'),
              "w") as f:
        f.write(HTML.class_html(subclass))

# Create Index Page
with open(os.path.join(website_folder, 'index.html'), "w") as f:
    f.write(HTML.index_html())
