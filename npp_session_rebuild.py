import os
import argparse
import xml.etree.ElementTree as ET

def create_session_xml(backup_path, sort_method):
    root = ET.Element("NotepadPlus")
    session = ET.SubElement(root, "Session", {"activeView": "0"})
    main_view = ET.SubElement(session, "mainView", {"activeIndex": "1"})

    # Read files in the backup directory
    backup_files = [(filename, os.path.getmtime(os.path.join(backup_path, filename)))
                    for filename in os.listdir(backup_path) if "@" in filename]

    # Sort files
    if sort_method == "name":
        sorted_backup_files = sorted(backup_files, key=lambda x: x[0])
    elif sort_method == "size":
        sorted_backup_files = sorted(backup_files, key=lambda x: os.path.getsize(os.path.join(backup_path, x[0])))
    else:  # Standard: Sortieren nach Änderungsdatum
        sorted_backup_files = sorted(backup_files, key=lambda x: x[1])

    # Insert sorted files into the XML structure
    for filename, _ in sorted_backup_files:
        file_path = os.path.join(backup_path, filename)
        file_attrib = {
            "firstVisibleLine": "0",
            "xOffset": "0",
            "scrollWidth": "0",
            "startPos": "0",
            "endPos": "0",
            "selMode": "0",
            "lang": "Normal Text",
            "encoding": "-1",
            "userReadOnly": "no",
            "filename": filename.split('@')[0],
            "backupFilePath": file_path,
            "originalFileLastModifTimestamp": "0",
            "originalFileLastModifTimestampHigh": "0",
            "mapFirstVisibleDisplayLine": "-1",
            "mapFirstVisibleDocLine": "-1",
            "mapLastVisibleDocLine": "-1",
            "mapNbLine": "-1",
            "mapHigherPos": "-1",
            "mapWidth": "-1",
            "mapHeight": "-1",
            "mapKByteInDoc": "0",
            "mapWrapIndentMode": "-1",
            "mapIsWrap": "no"
        }
        ET.SubElement(main_view, "File", file_attrib)

    # Add an empty subView node
    ET.SubElement(session, "subView", {"activeIndex": "0"})

    # Convert XML structure to string and write to file
    session_xml_string = ET.tostring(root, encoding='unicode', method='xml')
    with open("session.xml", "w") as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write(session_xml_string)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Creates a Notepad++ session.xml from backup files.")
    parser.add_argument("--sort-by-date", action="store_true", help="Sorts the files according to the last modification date.")
    parser.add_argument("--sort-by-name", action="store_true", help="Sorts the files alphabetically by name.")
    parser.add_argument("--sort-by-size", action="store_true", help="Sorts the files according to their size.")
    args = parser.parse_args()

    # Automatically determine backup directory
    username = os.environ.get("USERNAME")
    backup_path = fr"C:\Users\{username}\AppData\Roaming\Notepad++\backup"
    print(f"Backup Directory: {backup_path}")

    # Determine sorting method
    sort_method = "date"
    if args.sort_by_name:
        sort_method = "name"
    elif args.sort_by_size:
        sort_method = "size"

    # Create session.xml
    create_session_xml(backup_path, sort_method)
    print("session.xml wurde erfolgreich erstellt in: " + os.path.join(os.getcwd(), "session.xml"))

if __name__ == "__main__":
    main()
