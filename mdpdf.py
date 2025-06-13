#!/usr/bin/env python3

import os
import sys
import click
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

@click.command()
@click.argument('markdown_text', required=False)
@click.option('-f', '--file', help='Path to the input markdown file')
@click.option('-o', '--output', help='Path to the output PDF file')
def main(markdown_text, file, output):
    """Convert markdown to PDF."""
    if not markdown_text and not file:
        click.echo('Error: Either provide markdown text or use -f option to specify a file')
        sys.exit(1)
    
    if file and not os.path.exists(file):
        click.echo(f'Error: File {file} does not exist')
        sys.exit(1)
    
    # Get markdown content
    if file:
        with open(file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    else:
        markdown_content = markdown_text
    
    # Get output path
    if not output:
        output = get_output_path()
    
    try:
        convert_markdown_to_pdf(markdown_content, output)
        click.echo(f'Successfully created PDF at: {output}')
    except Exception as e:
        click.echo(f'Error creating PDF: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main() 