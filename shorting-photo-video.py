import os
import shutil
import time

# Additional message
print("📌 Code by Yodha Ardiansyah")
print("📷 Follow Instagram: @yodhaar_\n")

# Folder configuration (Modify as needed)
source_folder = "E:\\Backup\\Foto\\pindah"  # Source folder
destination_folder = "E:\\Backup\\Sorting"  # Destination folder

# File extensions for each category
photo_ext = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
video_ext = {".mp4", ".avi", ".mov", ".mkv", ".flv"}

# Category folders inside the destination folder
photo_folder = os.path.join(destination_folder, "Photos")
video_folder = os.path.join(destination_folder, "Videos")
screenshot_folder = os.path.join(destination_folder, "Screenshots")  # Special folder for screenshots

# Create destination folders if they don't exist
os.makedirs(photo_folder, exist_ok=True)
os.makedirs(video_folder, exist_ok=True)
os.makedirs(screenshot_folder, exist_ok=True)

print("🔄 Continuously monitoring folders and subfolders...\n")

# Infinite loop to keep the program running
while True:
    moved_files = []  # Reset the list of moved files

    # Iterate through all files in the source folder & subfolders
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)  # Full file path
            ext = os.path.splitext(file)[1].lower()

            # Move Screenshot files to the Screenshots folder
            if "screenshot" in file.lower() or file.lower().startswith("screenshot_"):
                shutil.move(file_path, os.path.join(screenshot_folder, file))
                moved_files.append(f"{file} ➝ Screenshots")
            
            # Move Photo files to the Photos folder
            elif ext in photo_ext:
                shutil.move(file_path, os.path.join(photo_folder, file))
                moved_files.append(f"{file} ➝ Photos")
            
            # Move Video files to the Videos folder
            elif ext in video_ext:
                shutil.move(file_path, os.path.join(video_folder, file))
                moved_files.append(f"{file} ➝ Videos")

    # Display results if any files were moved
    if moved_files:
        print("\n📂 Files moved:")
        for f in moved_files:
            print(f"- {f}")
        print("\n✅ All files have been moved.")
    
    # Wait 10 seconds before checking again (can be adjusted)
    time.sleep(10)
