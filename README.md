# Universal File Converter

A powerful and elegant CLI tool for converting files between different formats. Currently supports markdown to PDF conversion and image format conversions.

[![GitHub](https://img.shields.io/github/license/Sule57/mdpdf)](https://github.com/Sule57/mdpdf/blob/main/LICENSE)
[![GitHub](https://img.shields.io/github/stars/Sule57/mdpdf)](https://github.com/Sule57/mdpdf/stargazers)

## Features

- 🎨 **Markdown to PDF**: Beautiful PDF output with proper styling
- 🖼️ **Image Format Conversion**: Convert between PNG, JPG, WebP, and SVG formats
- 📝 Support for markdown tables and code blocks
- 🚀 Simple and intuitive CLI interface
- 💻 Cross-platform support (macOS, Linux, Windows)
- 📁 Automatic output naming (same location, new extension)

## 🚀 Quick Install

### macOS (with Homebrew)
```bash
# Install system dependencies
brew install cairo pango gdk-pixbuf libffi gobject-introspection

# Clone the repo and enter the directory
git clone https://github.com/Sule57/mdpdf.git
cd mdpdf

# Run the installation script (recommended)
./install.sh

# OR manually install:
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip3 install -r requirements.txt

# Add alias to your shell config (zsh is default on newer macOS):
echo 'alias convert="$(pwd)/venv/bin/python3 $(pwd)/convert.py"' >> ~/.zshrc
source ~/.zshrc

# If you use bash instead of zsh on macOS:
# echo 'alias convert="$(pwd)/venv/bin/python3 $(pwd)/convert.py"' >> ~/.bashrc
# source ~/.bashrc
```

### Ubuntu/Debian Linux
```bash
# Install system dependencies
sudo apt update
sudo apt install -y python3-venv python3-pip libcairo2 pango1.0-tools libgdk-pixbuf2.0-0 libffi-dev gir1.2-pango-1.0

# Clone the repo and enter the directory
git clone https://github.com/Sule57/mdpdf.git
cd mdpdf

# Run the installation script (recommended)
./install.sh

# OR manually install:
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip3 install -r requirements.txt

# Add alias to your shell config (this will work permanently)
echo 'alias convert="$(pwd)/venv/bin/python3 $(pwd)/convert.py"' >> ~/.bashrc
source ~/.bashrc
```

### Windows (PowerShell)
```powershell
# Install system dependencies using Chocolatey (requires admin)
choco install -y python cairo pango gdk-pixbuf libffi

# Clone the repo and enter the directory
git clone https://github.com/Sule57/mdpdf.git
cd mdpdf

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install Python dependencies
python -m pip install -r requirements.txt

# Add alias to PowerShell profile (creates if doesn't exist)
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value "`nfunction convert { & '$(Get-Location)\venv\Scripts\python.exe' '$(Get-Location)\convert.py' `$args }"
. $PROFILE
```

## 🔧 Troubleshooting

If you experience issues where the `convert` command stops working after logging out and back in:

1. **Use the installation script**: Run `./install.sh` from the converter directory
2. **Manual fix**: The issue is likely with the alias path. Remove the old alias and add a new one:
   ```bash
   # Remove old alias (if exists)
   sed -i.bak '/^alias convert=/d' ~/.zshrc
   
   # Add new alias with absolute path
   echo 'alias convert="/Users/yourusername/path/to/mdpdf/venv/bin/python3 /Users/yourusername/path/to/mdpdf/convert.py"' >> ~/.zshrc
   source ~/.zshrc
   ```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Usage

## Markdown to PDF Conversion

Convert markdown files to PDF:

1. **Convert with automatic output naming:**
```bash
convert -f input.md -t pdf
```

2. **Convert with custom output path:**
```bash
convert -f input.md -t pdf -o output.pdf
```

3. **Convert with format detected from output file:**
```bash
convert -f input.md -o output.pdf
```

## Image Format Conversion

Convert images between different formats:

1. **Convert with automatic output naming:**
```bash
convert -f image.png -t jpg
```

2. **Convert with custom output path:**
```bash
convert -f image.png -t jpg -o new_image.jpg
```

3. **Convert with format detected from output file:**
```bash
convert -f image.png -o new_image.jpg
```

4. **Convert SVG to other formats:**
```bash
convert -f logo.svg -t png -o logo.png
convert -f icon.svg -o icon.webp
```

## Options

- `-f, --file`: Path to the input file (required)
- `-t, --target`: Target format (optional if -o is provided)
  - For markdown: `pdf`
  - For images: `png`, `jpg`, `webp`
- `-o, --output`: Path to the output file (optional)

## Supported Formats

### Input Formats
- **Markdown**: `.md`, `.markdown`
- **Images**: `.png`, `.jpg`, `.jpeg`, `.webp`, `.svg`

### Output Formats
- **Markdown**: `.pdf`
- **Images**: `.png`, `.jpg`, `.webp`

## Default Behavior

- If no output file is specified with `-o`, the output will be created in the same directory with the same name but with the appropriate extension
- The target format can be specified with `-t` or automatically detected from the output file extension with `-o`
- When both `-t` and `-o` are provided, the tool validates that they are consistent
- Markdown files can only be converted to PDF format 