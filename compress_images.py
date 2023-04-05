from PIL import Image
import os

# Define the function to convert and compress images
def convert_and_compress(image_path, dest_folder_path, quality=80):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Print the original dimensions of the image
    #print('Original Dimensions:', img.size)

    # Convert the image to RGB if it's not already in that format
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Construct the destination file path with the same name as the original image
    dest_file_path = os.path.join(dest_folder_path, os.path.basename(image_path))

    MAX_SIZE = (600, 400)
    img.thumbnail(MAX_SIZE)

    # Save the image in JPEG format with the specified quality to the destination folder
    img.save(dest_file_path, 'JPEG', quality=quality, optimize=True)

    # Print the dimensions of the compressed image
    img = Image.open(dest_file_path)
    #print('Compressed Dimensions:', img.size)

    # Close the image
    img.close()

# Specify the root folder path where your images are located
root_folder_path = 'download_images'

# Specify the destination folder path where you want to save the compressed images
dest_folder_path = r'C:\Users\nello\Documents\vscode_projects\Image-Downloader\download_images_compressed'

# Iterate through all the subfolders in the root folder
for foldername in os.listdir(root_folder_path):
    folder_path = os.path.join(root_folder_path, foldername)

    # Check if the current path is a folder
    if os.path.isdir(folder_path):
        # Create the corresponding destination folder
        dest_folder = os.path.join(dest_folder_path, foldername)
        os.makedirs(dest_folder, exist_ok=True)

        # Iterate through all the files in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is an image file with a valid extension
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')):
                # Construct the full file path
                file_path = os.path.join(folder_path, filename)
                # Apply the function to the image
                convert_and_compress(file_path, dest_folder, quality=80) # You can adjust the quality value as per your requirement
    
    print("Done compressing species folder: "+foldername)