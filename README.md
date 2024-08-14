# CryptoWalletFinder

CryptoWalletFinder is a Python application designed to scan Linux systems for potential cryptocurrency wallet files. It identifies, catalogues, and reports on possible wallet files while providing comprehensive metadata about each file.

## Features

- Scans the entire filesystem for potential wallet files
- Identifies various types of cryptocurrency wallets
- Collects metadata such as file size, creation date, and last modified date
- Attempts to fingerprint files to distinguish between similar wallet types
- Generates a detailed report of all findings

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/KaladinB4/CryptoWalletFinder.git
   ```
2. Change to the project directory:
   ```
   cd CryptoWalletFinder
   ```
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script with sudo privileges to scan the entire filesystem:

```
sudo python3 main.py
```

You can specify a different root directory to scan and output file:

```
sudo python3 main.py --root /path/to/scan --output report.json
```

## Project Structure

```
CryptoWalletFinder/
│
├── main.py
├── wallet_finder/
│   ├── __init__.py
│   ├── scanner.py
│   ├── fingerprinter.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_scanner.py
│   └── test_fingerprinter.py
├── README.md
└── requirements.txt
```

## Testing

To run the tests, use pytest:

```
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and recovery purposes only. Always prioritize the security of your cryptocurrency wallets. Never share your private keys or wallet files with anyone. The authors of this tool are not responsible for any loss of funds or privacy breaches resulting from the use of this software.
