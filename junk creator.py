import os
import random
import string

# Choose where to create the test folder
test_folder = "C:/Users/Owner/Desktop/TestFolder"

# Create the folder if it doesn't exist
os.makedirs(test_folder, exist_ok=True)

# Define possible file types
file_types = [".txt", ".pdf", ".jpg", ".png", ".py", ".zip", ""]  # "" = no extension

def random_filename(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate 100 random files
for _ in range(100):
    ext = random.choice(file_types)
    filename = random_filename() + ext
    file_path = os.path.join(test_folder, filename)
    # Write random content to the file
    with open(file_path, "w") as f:
        f.write(f"This is a test file named {filename}")

print(f"Test folder created at {test_folder} with 100 random files.")
