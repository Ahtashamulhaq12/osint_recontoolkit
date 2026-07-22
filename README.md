# 🔍 Cyber Information Gathering Tool

> A Linux-based OSINT (Open Source Intelligence) tool developed in Python for collecting publicly available information about a target website.

**Developed by:** Ahtasham

---

## 📖 Overview

The Cyber Information Gathering Tool is designed to automate the initial reconnaissance phase of a cybersecurity assessment. It gathers publicly available information from a target domain using safe and non-intrusive techniques.

This project is intended for educational purposes and demonstrates how Python can be used to automate OSINT tasks on Linux.

---

## ✨ Features

- 🌐 Domain Name Input
- 📍 IP Address Resolution
- 📝 WHOIS Information Lookup
- 🌍 DNS Record Retrieval
- 🖥 HTTP Server Header Collection
- 💻 Basic Operating System Detection (Best Effort)
- 📧 Public Email Address Extraction
- ⚡ Fast Command-Line Interface
- 🐧 Linux Compatible

---

## 🛠 Technologies Used

- Python 3
- Linux (Kali/Debian/Ubuntu)
- socket
- requests
- re (Regular Expressions)
- whois
- dig (dnsutils)

---

## 📂 Project Structure

```
osint_recontoolkit/
│
├── osint_tool.py
├── requirements.txt
├── README.md
├── LICENSE
├── screenshots/
└── docs/
```

---

## ⚙ Prerequisites

Install the required packages:

```bash
sudo apt update

sudo apt install python3 python3-pip whois dnsutils

pip3 install -r requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Ahtashamulhaq12/osint_recontoolkit.git
```

Move into the project directory:

```bash
cd osint_recontoolkit
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

## ▶ Running the Tool

Run the application:

```bash
python3 osint_tool.py
```

Example:

```text
Enter Website:
google.com
```

---

## 📊 Sample Output

```text
============================================
 Cyber Information Gathering Tool
 Developed by Ahtasham
============================================

Target Website : google.com

IP Address : 142.251.xxx.xxx

WHOIS Information :
...

DNS Records :
...

Server : gws

Possible OS : Unknown

Public Emails :
No public email found.

Finished.
```

---

## 🔄 Workflow

```
Start
   │
   ▼
Enter Domain Name
   │
   ▼
Validate Input
   │
   ▼
Resolve IP Address
   │
   ▼
WHOIS Lookup
   │
   ▼
DNS Lookup
   │
   ▼
Collect HTTP Headers
   │
   ▼
Extract Public Emails
   │
   ▼
Display Results
   │
   ▼
End
```

---

## 📸 Screenshots

Add screenshots of:

- Tool Startup
- User Input
- WHOIS Output
- DNS Records
- Server Information
- Final Output

Store them inside the `screenshots/` folder.

---

## ⚠ Limitations

- Only collects publicly available information.
- Operating system detection is based on exposed HTTP headers and may not always be accurate.
- Many websites intentionally hide server details and public email addresses.
- The tool does not perform vulnerability scanning, exploitation, or intrusive actions.

---

## 🎯 Future Improvements

- GeoIP Lookup
- Reverse DNS Lookup
- SSL Certificate Analysis
- Security Header Analysis
- Technology Detection
- Export Results to PDF/CSV
- Improved OS Fingerprinting

---

## 📚 Educational Purpose

This project was developed as part of a cybersecurity internship/academic assignment to demonstrate the Information Gathering (Reconnaissance) phase of penetration testing using safe OSINT techniques.

---

## 👨‍💻 Author

**Ahtasham**

GitHub: https://github.com/Ahtashamulhaq12

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
