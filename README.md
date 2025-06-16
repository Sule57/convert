# Universal File Converter

[![GitHub](https://img.shields.io/github/license/Sule57/convert)](https://github.com/Sule57/convert/blob/main/LICENSE)
[![GitHub](https://img.shields.io/github/stars/Sule57/convert)](https://github.com/Sule57/convert/stargazers)

A powerful command-line tool for converting files between different formats. Currently supports:
- **Markdown to PDF**: Convert markdown files to beautifully formatted PDFs
- **Image format conversion**: Convert between various image formats (PNG, JPG, JPEG, SVG, etc.)

## Features

- 🚀 **Fast and efficient**: Built with modern Python libraries
- 🎨 **Beautiful output**: Markdown PDFs with proper styling and formatting
- 🔄 **Multiple formats**: Support for various input and output formats
- 💻 **Command-line interface**: Easy to use with simple commands
- 🛠️ **Flexible options**: Customize output paths and formats

## Installation

### Step 1: Install Dependencies

#### macOS
```bash
# Install system dependencies
brew install cairo pango gdk-pixbuf libffi

# Clone and install
git clone https://github.com/Sule57/convert.git
cd convert
chmod +x install.sh
./install.sh
```

#### Linux
```bash
# Install system dependencies
sudo apt update
sudo apt install -y python3-venv python3-pip libcairo2 pango1.0-tools libgdk-pixbuf2.0-0 libffi-dev gir1.2-pango-1.0

# Clone and install
git clone https://github.com/Sule57/convert.git
cd convert
chmod +x install.sh
./install.sh
```

#### Windows
```powershell
# Install system dependencies (requires Chocolatey)
choco install -y python cairo pango gdk-pixbuf libffi

# Clone and install
git clone https://github.com/Sule57/convert.git
cd convert
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Step 2: Set Up the Alias

After running the install script, you need to manually set up the alias in your shell configuration.

#### For zsh (macOS default)
```bash
# Get the current directory path
pwd

# Add the alias to your zsh configuration
echo 'alias convert="/Users/yourusername/path/to/convert/venv/bin/python3 /Users/yourusername/path/to/convert/convert.py"' >> ~/.zshrc

# Reload your shell configuration
source ~/.zshrc
```

#### For bash on macOS
```bash
# Get the current directory path
pwd

# Add the alias to your bash configuration
echo 'alias convert="/Users/yourusername/path/to/convert/venv/bin/python3 /Users/yourusername/path/to/convert/convert.py"' >> ~/.bash_profile

# Reload your shell configuration
source ~/.bash_profile
```

#### For bash on Linux
```bash
# Get the current directory path
pwd

# Add the alias to your bash configuration
echo 'alias convert="/home/yourusername/path/to/convert/venv/bin/python3 /home/yourusername/path/to/convert/convert.py"' >> ~/.bashrc

# Reload your shell configuration
source ~/.bashrc
```

#### For PowerShell (Windows)
```powershell
# Get the current directory path
Get-Location

# Create PowerShell profile if it doesn't exist
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}

# Add the function to your PowerShell profile
Add-Content -Path $PROFILE -Value "`nfunction convert { & 'C:\path\to\convert\venv\Scripts\python.exe' 'C:\path\to\convert\convert.py' `$args }"

# Reload your PowerShell profile
. $PROFILE
```

### Step 3: Test the Installation

After setting up the alias, test that it works:
```bash
convert --help
```

You should see the help message for the convert tool. If you get a "command not found" error, make sure you:
1. Used the correct path from `pwd` in your alias
2. Reloaded your shell configuration
3. Restarted your terminal

---

### Alternative: Manual Installation

If you prefer not to use the install script:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sule57/convert.git
   cd convert
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the alias** (follow Step 2 above)

## Usage

### Markdown to PDF

```bash
# Convert markdown file to PDF
convert -f input.md -t pdf
convert -f input.md -t pdf -o output.pdf
convert -f input.md -o output.pdf

# Convert markdown text directly
convert "Your markdown text here" -t pdf
```

### Image Format Conversion

```bash
# Convert PNG to JPG
convert -f image.png -t jpg
convert -f image.png -t jpg -o new_image.jpg
convert -f image.png -o new_image.jpg

# Convert SVG to PNG
convert -f logo.svg -t png -o logo.png

# Convert between other formats
convert -f photo.jpg -t png -o photo.png
```

## Command Options

- `-f, --file`: Input file path
- `-t, --type`: Output format type (pdf, png, jpg, jpeg, svg, etc.)
- `-o, --output`: Output file path (optional)
- `-h, --help`: Show help message

## Examples

### Markdown Examples

```bash
# Basic conversion
convert -f README.md -t pdf

# With custom output
convert -f README.md -t pdf -o documentation.pdf

# Convert text directly
convert "# Hello World\nThis is a test." -t pdf -o test.pdf
```

### Image Examples

```bash
# PNG to JPG
convert -f screenshot.png -t jpg -o screenshot.jpg

# SVG to PNG with custom size
convert -f logo.svg -t png -o logo.png

# JPG to PNG
convert -f photo.jpg -t png -o photo.png
```

## Manual Setup (Alternative)

If you prefer not to use the install script, you can set up manually:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sule57/convert.git
   cd convert
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add alias to your shell config:**
   ```bash
   echo 'alias convert="/Users/yourusername/path/to/convert/venv/bin/python3 /Users/yourusername/path/to/convert/convert.py"' >> ~/.zshrc
   ```

5. **Reload shell:**
   ```bash
   source ~/.zshrc
   ```

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Supported Formats

### Input Formats
- **Markdown**: `.md`, `.markdown`
- **Images**: `.png`, `.jpg`, `.jpeg`, `.svg`, `.bmp`, `.tiff`, `.webp`

### Output Formats
- **PDF**: From markdown files
- **Images**: `.png`, `.jpg`, `.jpeg`, `.svg`, `.bmp`, `.tiff`, `.webp`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [WeasyPrint](https://weasyprint.org/) for PDF generation
- Uses [Pillow](https://python-pillow.org/) for image processing
- Powered by [Click](https://click.palletsprojects.com/) for CLI interface 