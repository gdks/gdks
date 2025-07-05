#!/usr/bin/env python3
"""
Script to crop an image into a banner format.
Removes top 30% and bottom 10% of the image.
"""

import sys
from PIL import Image
import os

def crop_image_to_banner(input_path, output_path):
    """
    Crop an image to banner format by removing top 30% and bottom 10%.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the cropped banner
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get original dimensions
            width, height = img.size
            
            # Calculate crop dimensions
            # Remove top 30% and bottom 10%
            top_crop = int(height * 0.30)  # Remove top 30%
            bottom_crop = int(height * 0.90)  # Keep up to 90% (remove bottom 10%)
            
            # Crop the image (left, top, right, bottom)
            cropped_img = img.crop((0, top_crop, width, bottom_crop))
            
            # Save the cropped image
            cropped_img.save(output_path, quality=95)
            
            print(f"✅ Banner created successfully!")
            print(f"📏 Original size: {width}x{height}")
            print(f"📏 Banner size: {width}x{bottom_crop - top_crop}")
            print(f"💾 Saved to: {output_path}")
            
    except Exception as e:
        print(f"❌ Error processing image: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 crop_banner.py <input_image> <output_image>")
        print("Example: python3 crop_banner.py cityscape.jpg banner.jpg")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        sys.exit(1)
    
    crop_image_to_banner(input_path, output_path)

if __name__ == "__main__":
    main()