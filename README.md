Alright, let’s turn this into **resume-grade, recruiter-bait material** 🧲
The goal here is:

> “This person understands networking, tradeoffs, and can build clean tools — not just run nmap.”

---

# 🔥 Recruiter-Optimized README

You can paste this directly as `README.md`.

---

# Python Port Scanner with TTL-Based OS Fingerprinting

A **multi-threaded TCP port scanner** written in **pure Python (standard library only)** that performs **basic OS fingerprinting using IP TTL analysis**.

This project demonstrates practical understanding of:

* TCP/IP networking
* Port scanning techniques
* OS fingerprinting heuristics
* Cross-platform tooling
* Clean Python project structure and CLI design

Designed for **educational use and authorized security testing**.

---

## 🧩 Technical Highlights

* **TCP Connect Scanning**

  * Reliable, portable scanning using Python `socket`
  * No raw sockets or elevated privileges required

* **Concurrent Scanning**

  * Threaded execution using `concurrent.futures`
  * Efficient scanning of large port ranges

* **TTL-Based OS Fingerprinting**

  * Infers operating system based on observed IP TTL values
  * Cross-platform TTL extraction using system `ping`
  * Explicitly documents assumptions and limitations

* **Zero Dependencies**

  * Uses **only Python standard library**
  * Easy to run, audit, and deploy

---

## 🧠 OS Fingerprinting via TTL

Operating systems often use different **initial TTL values** when sending IP packets:

| Platform        | Typical Initial TTL |
| --------------- | ------------------- |
| Linux / macOS   | 64                  |
| Windows         | 128                 |
| Network devices | 255                 |

Because TTL decreases by one per hop, the observed TTL can be rounded **up** to the nearest known baseline to infer the OS.

### Example

* Observed TTL `117` → inferred initial TTL `128` → **Windows**
* Observed TTL `51` → inferred initial TTL `64` → **Linux / macOS**

⚠️ This technique is **heuristic**, not definitive. NAT, firewalls, routing paths, and ICMP filtering may affect results.

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/python-port-scanner.git
cd python-port-scanner
```

No dependencies required.
Python **3.8+** recommended.

---

## ▶️ Usage

### Scan default ports (1–1024)

```bash
python main.py --target 192.168.1.1
```

### Scan a specific port

```bash
python main.py --target 192.168.1.1 --ports 443
```

### Scan a custom range with OS detection

```bash
python main.py --target 192.168.1.1 --ports 1-1000 --os-detect
```

### Sample Output

```text
[+] Scanning 192.168.1.1...
[+] Open ports: [22, 80, 443]
[+] Observed TTL: 117
[+] OS Guess: Windows
```

---

## 📁 Project Structure

```
python-port-scanner/
├── scanner/
│   ├── __init__.py
│   ├── port_scanner.py        # TCP connect scan logic
│   ├── ttl_fingerprint.py     # TTL extraction and OS inference
│   └── utils.py               # Threading utilities
├── main.py                    # CLI entry point
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚠️ Limitations

* TCP connect scan only (no SYN scanning)
* TTL-based fingerprinting is approximate
* ICMP may be blocked by some hosts
* Accuracy depends on network topology

---

## 🔭 Future Enhancements

* Service/banner detection
* JSON / CSV output support
* CIDR range scanning
* Rate limiting and stealth scanning
* Optional SYN scan mode

---

## ⚖️ Ethical Use

This tool is intended for **educational purposes** and **authorized testing only**.
Unauthorized scanning may be illegal.

---

## 📜 License

MIT License

