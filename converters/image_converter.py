#!/usr/bin/env python3

import os
from PIL import Image
import cairosvg

def convert_image(input_path, output_path, target_format):
    """Convert image from one format to another."""
    target_format = target_format.upper()
    
    # Handle SVG to other formats
    if input_path.lower().endswith('.svg'):
        return convert_svg_to_image(input_path, output_path, target_format)
    
    # Handle other image formats
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if saving as JPG
            if target_format == 'JPG' and img.mode in ('RGBA', 'LA', 'P'):
                # Create a white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Map JPG to JPEG for Pillow
            pillow_format = 'JPEG' if target_format == 'JPG' else target_format
            
            # Save with the target format
            img.save(output_path, format=pillow_format)
            return True
    except Exception as e:
        raise Exception(f"Error converting image: {str(e)}")

def convert_svg_to_image(input_path, output_path, target_format):
    """Convert SVG to other image formats using cairosvg."""
    try:
        if target_format == 'PNG':
            cairosvg.svg2png(url=input_path, write_to=output_path)
        elif target_format == 'JPG':
            cairosvg.svg2png(url=input_path, write_to=output_path.replace('.jpg', '.png'))
            # Convert PNG to JPG
            with Image.open(output_path.replace('.jpg', '.png')) as img:
                # Convert to RGB if needed
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                img.save(output_path, format='JPEG')
            # Remove temporary PNG file
            os.remove(output_path.replace('.jpg', '.png'))
        elif target_format == 'WEBP':
            cairosvg.svg2png(url=input_path, write_to=output_path.replace('.webp', '.png'))
            # Convert PNG to WebP
            with Image.open(output_path.replace('.webp', '.png')) as img:
                img.save(output_path, format='WEBP')
            # Remove temporary PNG file
            os.remove(output_path.replace('.webp', '.png'))
        else:
            raise Exception(f"Unsupported target format: {target_format}")
        return True
    except Exception as e:
        raise Exception(f"Error converting SVG: {str(e)}")

def get_default_output_path(input_file, target_format):
    """Get default output path for image file (same name, new extension)."""
    base, _ = os.path.splitext(input_file)
    return base + '.' + target_format.lower()

def is_supported_input_format(file_path):
    """Check if the input file format is supported."""
    supported_formats = {'.png', '.jpg', '.jpeg', '.webp', '.svg'}
    _, ext = os.path.splitext(file_path.lower())
    return ext in supported_formats

def is_supported_target_format(target_format):
    """Check if the target format is supported."""
    supported_formats = {'png', 'jpg', 'jpeg', 'webp'}
    return target_format.lower() in supported_formats 