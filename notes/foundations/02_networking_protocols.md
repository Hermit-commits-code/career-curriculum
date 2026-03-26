# 🌐 The Netrunner's Protocol Ledger

**Date:** 2026-03-26 | **Status:** Phase 1 Verified

## 🛠️ Essential Curl "ICE-Breakers"

| Flag | Name     | Function                                            |
| :--- | :------- | :-------------------------------------------------- |
| `-v` | Verbose  | See the raw handshake (The Scanner).                |
| `-I` | Head     | Get only the Metadata/Headers (The Quick Scan).     |
| `-L` | Location | Automatically follow 3xx Redirects (The Navigator). |
| `-H` | Header   | Add a label/metadata (e.g., Content-Type or Auth).  |
| `-d` | Data     | The JSON/Cargo payload for POST requests.           |
| `-m` | Max-Time | The Fail-Safe timeout (The Dead-Man's Switch).      |

## 🤝 The 3-Way Handshake (TCP)

1. **SYN** (Synchronize): "Requesting access."
2. **SYN-ACK** (Acknowledge): "Access granted, are you ready?"
3. **ACK** (Acknowledge): "Link established. Sending data."

## 🚦 The Status Code "Threat Levels"

- **200 OK:** Mission Success.
- **301/302:** Redirection (The server moved).
- **401/403:** Unauthorized (Missing the Bearer Token).
- **404:** Not Found (The ghost in the machine).
- **500:** Internal Server Error (The server flatlined).
