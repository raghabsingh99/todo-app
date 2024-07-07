import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath,"r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("D:\Python Coding\app1\experiments\compressed.zip",
                    "D:\Python Coding\app1\experiments\dest")

