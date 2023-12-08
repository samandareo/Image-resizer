from PIL import Image

# Open the original image
original_image_path = "path/to/your/image.png"
original_image = Image.open(original_image_path)

# Define the new size you want
new_size = (86, 128)

scaled_image = original_image.resize(new_size, resample=Image.AFFINE)

# Save the scaled image
scaled_image.save("path/to/your/image.png")
