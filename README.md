# 🛡️ Python Packet Analyzer & Syslog Forwarder

A lightweight Python-based network packet analyzer designed to inspect and log traffic on a local interface using [`scapy`](https://scapy.readthedocs.io/en/latest/). Captured data includes source/destination IPs, protocols, and ports. The logs can be optionally forwarded to a remote syslog server (e.g., Splunk, Security Onion) for centralized analysis in a SOC or home lab environment.

---

## 📌 Features

- 🔍 Real-time packet sniffing using `scapy`
- 🧠 Protocol detection: TCP, UDP, ICMP
- 📁 Local logging to file
- 📡 Optional forwarding to remote syslog server (UDP)
- 🧩 Designed for integration into SIEM environments (Splunk, ELK, etc.)
- 💻 Compatible with Linux and Windows

---

## 🧪 Use Cases

- Home SOC Lab traffic analysis
- Packet enrichment for SIEM ingestion
- Lightweight network visibility tool for early detection
- Educational tool for learning about network protocols and packet structures

---

## 🛠️ Requirements

Install Python packages:

```bash
pip install scapy
