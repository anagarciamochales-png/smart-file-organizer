from pathlib import Path
import shutil

# Creates destination folders if they do not already exist
def create_folders():
    folders = ["PDFs", "Images", "Documents", "Videos", "Archives", "PowerPoint", "Spreadsheets"]
    
    for folder_name in folders:
        folder = Path(folder_name)
        folder.mkdir(exist_ok=True)
        
        print(f" 📁 {folder_name} ready")

file_types = {
    ".pdf": "PDFs",
    ".docx": "Documents",
    ".mp4": "Videos",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".zip": "Archives",
    ".pptx": "PowerPoint",
    ".xlsx": "Spreadsheets",
    ".doc": "Documents",
    ".txt": "Documents",
    ".csv": "Spreadsheets",
    }

# Determines the category based on the file extension
def get_file_type(extension):

    extension = extension.lower()
    
    return file_types.get(extension, "Unknown")

# Move files into their corresponding folders
def move_files():

    folder = Path("TestDownloads")
    files_moved = 0 
    category_count = {}
    
    for file in folder.iterdir(): 
        file_type = get_file_type(file.suffix)

        # Skip unsupported file types
        if file_type == "Unknown":
            continue
        
        destination = Path(file_type) / file.name
        counter = 1

       # Handle duplicate file names by appending a number
        while destination.exists():
            stem = Path(file.name).stem
            suffix = Path(file.name).suffix 
            
            destination = Path(file_type) / f"{stem}_{counter}{suffix}"
            counter += 1
        
        print(f"📁 Moving {file.name} to {destination}")

        try:
            shutil.move(file, destination)
            print(f"✅ Moved {file.name}")
            files_moved += 1
            # Track how many files were moved per category
            if file_type in category_count:
                category_count[file_type] += 1
            else:
                category_count[file_type] = 1
    
        except Exception as error:
            print(f"❌ Error moving {file.name}")
            print(error)
            print()

    print("\n📊 ==== SMART FILE ORGANIZER ====")
    print(f"Total files moved: {files_moved}")
    
    for category, count in category_count.items():
        print(f"{category}: {count}")
    
    print("\n🎉 Organization Complete!")
        

create_folders()
move_files()
