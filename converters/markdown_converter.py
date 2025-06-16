#!/usr/bin/env python3

import os
import markdown
from weasyprint import HTML
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.validation import Validator, ValidationError

class OutputPathValidator(Validator):
    def validate(self, document):
        text = document.text
        if not text:
            raise ValidationError(message='Output path cannot be empty')
        if not text.endswith('.pdf'):
            raise ValidationError(message='Output file must end with .pdf')
        
        # Check if directory exists
        directory = os.path.dirname(text)
        if directory and not os.path.exists(directory):
            raise ValidationError(message=f'Directory {directory} does not exist')

def get_output_path():
    """Prompt user for output PDF path with validation and completion."""
    completer = PathCompleter()
    validator = OutputPathValidator()
    
    while True:
        try:
            path = prompt(
                'Enter output PDF path: ',
                completer=completer,
                validator=validator
            )
            return path
        except ValidationError as e:
            print(f'Error: {e.message}')

def convert_markdown_to_pdf(markdown_content, output_path):
    """Convert markdown content to PDF."""
    # Convert markdown to HTML
    html_content = markdown.markdown(
        markdown_content,
        extensions=['tables', 'fenced_code']
    )
    
    # Add some basic styling
    html_content = f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                code {{ background-color: #f5f5f5; padding: 2px 4px; border-radius: 4px; }}
                pre {{ background-color: #f5f5f5; padding: 16px; border-radius: 4px; overflow-x: auto; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f5f5f5; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
    </html>
    """
    
    # Convert HTML to PDF
    html = HTML(string=html_content)
    html.write_pdf(output_path)

def get_default_output_path(input_file):
    """Get default output path for markdown file (same name, .pdf extension)."""
    base, _ = os.path.splitext(input_file)
    return base + '.pdf' 