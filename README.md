# MDPDF - Markdown to PDF Converter

A simple and elegant CLI tool for converting markdown files into beautifully formatted PDFs.

[![GitHub](https://img.shields.io/github/license/Sule57/mdpdf)](https://github.com/Sule57/mdpdf/blob/main/LICENSE)
[![GitHub](https://img.shields.io/github/stars/Sule57/mdpdf)](https://github.com/Sule57/mdpdf/stargazers)

## Features

- 🎨 Beautiful PDF output with proper styling
- 📝 Support for markdown tables and code blocks
- 🚀 Simple and intuitive CLI interface
- 💻 Cross-platform support (macOS, Linux, Windows)
- 🔄 Interactive output path selection

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
echo 'alias mdpdf="$(pwd)/venv/bin/python3 $(pwd)/mdpdf.py"' >> ~/.zshrc
source ~/.zshrc

# If you use bash instead of zsh on macOS:
# echo 'alias mdpdf="$(pwd)/venv/bin/python3 $(pwd)/mdpdf.py"' >> ~/.bashrc
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
echo 'alias mdpdf="$(pwd)/venv/bin/python3 $(pwd)/mdpdf.py"' >> ~/.bashrc
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
Add-Content -Path $PROFILE -Value "`nfunction mdpdf { & '$(Get-Location)\venv\Scripts\python.exe' '$(Get-Location)\mdpdf.py' `$args }"
. $PROFILE
```

## 🔧 Troubleshooting

If you experience issues where the `mdpdf` command stops working after logging out and back in:

1. **Use the installation script**: Run `./install.sh` from the mdpdf directory
2. **Manual fix**: The issue is likely with the alias path. Remove the old alias and add a new one:
   ```bash
   # Remove old alias (if exists)
   sed -i.bak '/^alias mdpdf=/d' ~/.zshrc
   
   # Add new alias with absolute path
   echo 'alias mdpdf="/Users/yourusername/path/to/mdpdf/venv/bin/python3 /Users/yourusername/path/to/mdpdf/mdpdf.py"' >> ~/.zshrc
   source ~/.zshrc
   ```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Usage

The tool can be used in three ways:

1. Convert markdown text directly:
```bash
mdpdf "Your markdown text here"
```

2. Convert a markdown file:
```bash
mdpdf -f input.md
```

3. Convert a markdown file to a specific output file:
```bash
mdpdf -f input.md -o output.pdf
```

## Options

- `-f, --file`: Path to the input markdown file
- `-o, --output`: Path to the output PDF file

If no output file is specified and a file is provided with `-f`, the output will be created in the same directory with the same name but with a `.pdf` extension. If markdown text is provided directly, you will be prompted to enter the output file path. 