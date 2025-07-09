# 🔍 Port Scanner Using Python

A lightweight and fast port scanner built with Python for basic network reconnaissance and vulnerability assessment.

---

## 🧠 Problem Statement

Network ports are essential for communication between devices and services. However, open or poorly secured ports can become vulnerabilities if left unmonitored. A port scanner helps identify these open ports for security checks.

---

## 🎯 Objective

To build a Python-based command-line tool that:
- Scans a target IP or domain for open ports.
- Uses multithreading for fast scanning.
- Helps in initial vulnerability assessment.

---

## 🧰 Requirements

- Python 3.x
- `socket` (standard library)
- `threading` (standard library)
- `argparse` (standard library)

---

## 🚀 Features

- Scan a custom range of ports (default: 1–1024).
- High-speed with multithreading support.
- Resolves hostname to IP address.
- CLI with arguments for easy control.

---

## 🖥️ Usage

### ✅ Run the scanner:
```bash
python port_scanner.py target.com
