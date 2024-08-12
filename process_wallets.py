import subprocess
import os
import time

def is_likely_wallet_file(filename):
    wallet_extensions = ['.dat', '.wallet', '.aes.json']
    excluded_patterns = ['icudtl', 'minecraft', 'chrome', 'brave']
    return (any(filename.lower().endswith(ext) for ext in wallet_extensions) and
            not any(pattern in filename.lower() for pattern in excluded_patterns))

def run_btcrecover(wallet_file, log_file):
    if not is_likely_wallet_file(wallet_file):
        log_file.write(f"Skipping non-wallet file: {wallet_file}\n")
        return False

    command = [
        "python3", "btcrecover.py",
        "--wallet", wallet_file,
        "--passwordlist", "passwords.txt",
        "--dump-privkeys", f"private_keys_{os.path.basename(wallet_file)}.txt",
        "--tokenlist", "To/token.txt"
    ]
    
    log_file.write(f"Processing potential wallet file: {wallet_file}\n")
    log_file.flush()
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        output = []
        for line in process.stdout:
            print(line, end='')  # Print to console
            log_file.write(line)  # Write to log file
            output.append(line)
            log_file.flush()
        process.wait()
        
        output_text = ''.join(output)
        if "Error: unrecognized wallet format" in output_text:
            log_file.write(f"Unrecognized wallet format: {wallet_file}\n")
            return False
        if "Starting btcrecover" in output_text and "Error:" not in output_text:
            log_file.write(f"Potentially valid wallet file: {wallet_file}\n")
            return True
        
    except Exception as e:
        log_file.write(f"Error processing {wallet_file}: {str(e)}\n")
        return False
    
    log_file.write(f"Finished processing: {wallet_file}\n\n")
    log_file.flush()
    return False

# Read wallet files from list
with open('wallet_files_list.txt', 'r') as f:
    wallet_files = f.read().splitlines()

# Create a single log file for the entire process
log_filename = f"btcrecover_log_{time.strftime('%Y%m%d_%H%M%S')}.txt"
with open(log_filename, 'w') as log_file:
    total_files = len(wallet_files)
    processed_files = 0
    potential_wallets = 0
    for index, wallet_file in enumerate(wallet_files, 1):
        print(f"Checking file {index} of {total_files}: {wallet_file}")
        if run_btcrecover(wallet_file, log_file):
            potential_wallets += 1
        processed_files += 1
        
        #
