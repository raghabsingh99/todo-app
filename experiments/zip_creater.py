import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:

        for filepath in filepaths:
            filepaths = pathlib.Path(filepaths)
            archive.write(filepath, arcname = filepaths.name)


if __name__ == "__main__":
    make_archive(filepaths=["e.py","e1.py","e3.py"],dest_dir="dest")

