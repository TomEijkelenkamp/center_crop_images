import os
from PIL import Image, ImageOps

def crop_center(img, desired_size):
    """
    Crop the image from the center to the desired size.
    """
    delta_w = img.width - desired_size[0]
    delta_h = img.height - desired_size[1]
    
    left = delta_w // 2
    upper = delta_h // 2
    right = img.width - delta_w // 2
    lower = img.height - delta_h // 2
    
    return img.crop((left, upper, right, lower))

def process_folder(src_folder, dest_folder, crop_size=(1024, 1024)):
    """
    Process the source folder and save the cropped images in the destination folder.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for img_file in os.listdir(src_folder):
        if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            src_img_path = os.path.join(src_folder, img_file)
            dest_img_path = os.path.join(dest_folder, img_file)

            with Image.open(src_img_path) as img:
                cropped_img = crop_center(img, crop_size)
                cropped_img.save(dest_img_path)

if __name__ == '__main__':
    SOURCE_FOLDER = 'c:\\Users\\tomei\\Documents\\Python\\Internship\\test_week_3\\blender_images\\generated_renders\\render_8'
    DESTINATION_FOLDER = 'c:\\Users\\tomei\\Documents\\Python\\Internship\\test_week_3\\blender_images\\generated_renders\\render_8_cropped'
    
    process_folder(SOURCE_FOLDER, DESTINATION_FOLDER)