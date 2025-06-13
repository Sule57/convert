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

# Install Python dependencies
pip3 install -r requirements.txt

# Make the CLI globally available
ln -sf "$(pwd)/mdpdf.py" /usr/local/bin/mdpdf
```

### Ubuntu/Debian Linux
```bash
# Install system dependencies
sudo apt update
sudo apt install -y python3-pip libcairo2 pango1.0-tools libgdk-pixbuf2.0-0 libffi-dev gir1.2-pango-1.0

# Clone the repo and enter the directory
git clone https://github.com/Sule57/mdpdf.git
cd mdpdf

# Install Python dependencies
pip3 install -r requirements.txt

# Make the CLI globally available
sudo ln -sf "$(pwd)/mdpdf.py" /usr/local/bin/mdpdf
```

### Windows (PowerShell)
```powershell
# Install system dependencies using Chocolatey (requires admin)
choco install -y python cairo pango gdk-pixbuf libffi

# Clone the repo and enter the directory
git clone https://github.com/Sule57/mdpdf.git
cd mdpdf

# Install Python dependencies
python -m pip install -r requirements.txt

# Add the CLI to your PATH for this session
$env:Path += ";$(Get-Location)"

# (Optional) Add an alias for easier use
Set-Alias mdpdf $(Get-Location)\mdpdf.py
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

If no output file is specified, you will be prompted to enter the output file path. 