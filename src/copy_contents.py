import os
import shutil

def copy_content():
    source = './static/'
    public = './public/'
    listdir = os.listdir(source)
    if os.path.exists(public):
        shutil.rmtree(public)
        os.mkdir(public)
    elif not os.path.exists(public):
        os.mkdir(public)
    traverse_directory(listdir, source, public)

def traverse_directory(listdir, source, public):
    for file in listdir:
        source_filepath = os.path.join(source, file)
        if os.path.isfile(source_filepath):
            shutil.copy(source_filepath, public)
        elif os.path.isdir(source_filepath):
            newlist  = os.listdir(source_filepath)
            newdir = os.path.join(public, file)
            os.mkdir(newdir)
            traverse_directory(newlist, source_filepath, newdir)
