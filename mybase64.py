from PIL import Image
# Open the image file
with open("Aloe1.jpg", "rb") as f:
    image = Image.open(f)
import base64
# Convert the image to base64 format
with open("Aloe1.jpg", "rb") as f:
    encoded_image = base64.b64encode(f.read())
# Save the encoded image to a file
with open("image.txt", "w") as f:
    f.write(encoded_image.decode("utf-8"))
# Specify the file path you want to read
file_path = "image.txt"

try:
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the contents of the file and store them in a variable
        file_contents = file.read()

    # Now, file_contents contains the content of the file
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
import os

# Specify the file path you want to delete
file_path = "image.txt"

# Check if the file exists before attempting to delete it
if os.path.exists(file_path):
    os.remove(file_path)
   
else:
    print(f"{file_path}")
