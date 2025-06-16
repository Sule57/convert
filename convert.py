#!/usr/bin/env python3

import os
import sys
import click
from converters.markdown_converter import (
    convert_markdown_to_pdf, 
    get_output_path as get_md_output_path,
    get_default_output_path as get_md_default_output_path
)
from converters.image_converter import (
    convert_image,
    get_default_output_path as get_img_default_output_path,
    is_supported_input_format,
    is_supported_target_format
)

def print_banner():
    """Print ASCII art banner."""
    banner = r"""
     _____                            _   
    /  __ \                          | |  
    | /  \/ ___  _ __   ___ _ __ __ _| |_ 
    | |    / _ \| '_ \ / _ \ '__/ _` | __|
    | \__/\ (_) | | | |  __/ | | (_| | |_ 
     \____/\___/|_| |_|\___|_|  \__,_|\__|
    
    Universal File Converter
    Created by Sule57
    """
    click.echo(banner)

def detect_conversion_type(input_file):
    """Detect the type of conversion based on file extension."""
    if not input_file:
        return None
    
    _, ext = os.path.splitext(input_file.lower())
    
    if ext in {'.md', '.markdown'}:
        return 'markdown'
    elif ext in {'.png', '.jpg', '.jpeg', '.webp', '.svg'}:
        return 'image'
    else:
        return None

def detect_target_format_from_output(output_file):
    """Detect target format from output file extension."""
    if not output_file:
        return None
    
    _, ext = os.path.splitext(output_file.lower())
    
    if ext == '.pdf':
        return 'pdf'
    elif ext in {'.png', '.jpg', '.jpeg', '.webp'}:
        return ext[1:]  # Remove the dot
    else:
        return None

def is_supported_markdown_target_format(target_format):
    """Check if the target format is supported for markdown."""
    return target_format.lower() == 'pdf'

def validate_target_format(conversion_type, target_format, output_file):
    """Validate and resolve target format, potentially detecting it from output file."""
    if target_format:
        # If target format is provided, validate it
        if conversion_type == 'markdown':
            if not is_supported_markdown_target_format(target_format):
                return None, f'Unsupported target format for markdown: {target_format}. Only "pdf" is supported.'
        elif conversion_type == 'image':
            if not is_supported_target_format(target_format):
                return None, f'Unsupported target format: {target_format}. Supported formats: png, jpg, webp'
        return target_format.lower(), None
    else:
        # If no target format provided, try to detect from output file
        if output_file:
            detected_format = detect_target_format_from_output(output_file)
            if detected_format:
                if conversion_type == 'markdown' and detected_format != 'pdf':
                    return None, f'Cannot convert markdown to {detected_format}. Only "pdf" is supported.'
                elif conversion_type == 'image' and not is_supported_target_format(detected_format):
                    return None, f'Unsupported target format: {detected_format}. Supported formats: png, jpg, webp'
                return detected_format, None
            else:
                return None, f'Could not detect target format from output file: {output_file}'
        else:
            return None, 'Please specify target format using -t option or provide output file with -o option'

@click.command(
    help="""Universal file converter supporting markdown to PDF and image format conversions.
    
    Examples:
        # Markdown to PDF
        convert -f input.md -t pdf
        convert -f input.md -t pdf -o output.pdf
        convert -f input.md -o output.pdf
        
        # Image format conversion
        convert -f image.png -t jpg
        convert -f image.png -t jpg -o new_image.jpg
        convert -f image.png -o new_image.jpg
        convert -f logo.svg -t png -o logo.png
    """,
    add_help_option=True,
    no_args_is_help=True
)
@click.option('-f', '--file', help='Path to the input file', required=True)
@click.option('-t', '--target', help='Target format (pdf for markdown, png/jpg/webp for images)')
@click.option('-o', '--output', help='Path to the output file')
def main(file, target, output):
    """Universal file converter."""
    print_banner()
    
    if not os.path.exists(file):
        click.echo(f'Error: File {file} does not exist')
        sys.exit(1)
    
    # Detect conversion type
    conversion_type = detect_conversion_type(file)
    
    if not conversion_type:
        click.echo(f'Error: Unsupported file type. Supported formats: .md, .png, .jpg, .jpeg, .webp, .svg')
        sys.exit(1)
    
    # Validate and resolve target format
    resolved_target, error_msg = validate_target_format(conversion_type, target, output)
    if error_msg:
        click.echo(f'Error: {error_msg}')
        sys.exit(1)
    
    # Determine output path
    if not output:
        if conversion_type == 'markdown':
            output = get_md_default_output_path(file)
        else:
            output = get_img_default_output_path(file, resolved_target)
    
    # Perform conversion
    if conversion_type == 'markdown':
        try:
            with open(file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            convert_markdown_to_pdf(markdown_content, output)
            click.echo(f'Successfully created PDF at: {output}')
        except Exception as e:
            click.echo(f'Error creating PDF: {str(e)}')
            sys.exit(1)
    
    elif conversion_type == 'image':
        try:
            convert_image(file, output, resolved_target)
            click.echo(f'Successfully converted {file} to {output}')
        except Exception as e:
            click.echo(f'Error converting image: {str(e)}')
            sys.exit(1)

if __name__ == '__main__':
    main() 