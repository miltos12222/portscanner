## Author
**Miltos12222** – Pentester, Programmer, Hacker Enthusiast


# Python Port Scanner

A fast, lightweight, multithreaded TCP port scanner written in Python.  
Designed for learning purposes, internal network auditing, and basic penetration testing workflows.

---

## Features

- Multithreaded TCP port scanning
- Scans common ports (20–1024)
- Uses Python sockets (no external libraries)
- Simple and readable codebase
- Cross-platform (Windows / Linux / macOS)

---

## How It Works

The scanner attempts to establish TCP connections to target ports using Python's `socket` module.  
Each port is scanned in a separate thread to significantly improve performance compared to sequential scanning.

---


## Usage

Basic scan:
```bash
python scanner.py 127.0.0.1

Custom port range and timeout: python scanner.py 192.168.1.1 -s 1 -e 500 -t 0.3

