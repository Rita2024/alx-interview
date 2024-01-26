#!/usr/bin/python3

import sys
import signal

def compute_metrics(lines):
    total_size = 0
    status_code_counts = {}

    for line in lines:
        parts = line.split()
        if len(parts) >= 10 and parts[5] == '"GET' and parts[7].isdigit():
            file_size = int(parts[8])
            total_size += file_size

            status_code = parts[9]
            if status_code.isdigit() and int(status_code) in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[int(status_code)] = status_code_counts.get(int(status_code), 0) + 1

    return total_size, status_code_counts

def print_metrics(total_size, status_code_counts):
    print(f'Total file size: {total_size}')

    for status_code in sorted(status_code_counts.keys()):
        print(f'{status_code}: {status_code_counts[status_code]}')

def main():
    lines = []
    total_size = 0
    status_code_counts = {}

    def signal_handler(sig, frame):
        nonlocal total_size, status_code_counts
        print_metrics(total_size, status_code_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) % 10 == 0:
                total_size, status_code_counts = compute_metrics(lines)
                print_metrics(total_size, status_code_counts)
                lines = []
    except KeyboardInterrupt:
        print_metrics(total_size, status_code_counts)

if __name__ == "__main__":
    main()
