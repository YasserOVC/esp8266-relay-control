\# ESP8266 4-Relay Controller



A web-based app to control an ESP8266 WiFi 4-Channel Relay Module using PowerShell, Python, JavaScript, HTML, and CSS.



\## Overview

This project creates a browser UI to toggle 4 relays on an ESP8266 board. It uses:

\- \*\*PowerShell\*\*: Launches the Python bridge.

\- \*\*Python\*\*: WebSocket-to-TCP bridge (forwards commands to ESP).

\- \*\*HTML/JS/CSS\*\*: Responsive web interface.



Architecture:



\## Features

\- Control relays from any browser on the same network.

\- Supports ESP Mode 1 (direct AP) and Mode 2 (router).

\- Auto-installs Python dependencies.

\- Responsive UI with connection status.



\## Requirements

\- Python 3.x (with `websockets`).

\- ESP8266 4-Relay Module (configured via EspTouch\_Demo app).

\- GitHub for hosting.



\## Setup

1\. Clone the repo: `git clone https://github.com/YourUsername/esp8266-relay-control.git`

2\. Run `Start-RelayControl.ps1` in PowerShell (or `Run-RelayControl.bat`).

3\. Open `index.html` in a browser.

4\. Enter ESP IP (e.g., 192.168.1.112) and connect.

5\. Toggle relays!



\## Files

\- `Start-RelayControl.ps1`: Launcher.

\- `bridge.py`: TCP bridge.

\- `index.html`: Web UI.

\- `requirements.txt`: Python deps.

\- `Run-RelayControl.bat`: Optional batch starter.



\## Configuration

\- Edit `bridge.py` for ESP\_IP (default: 192.168.1.112).

\- Use EspTouch\_Demo Android app for ESP WiFi setup.



\## Troubleshooting

\- No connection: Check ESP green LED (should flash 2s → solid ON).

\- TCP failed: Verify IP and port 8080 open (`Test-NetConnection`).

\- Relays not responding: Ensure commands are raw HEX bytes.



\## License

MIT License — feel free to use/modify.



Built with yasser.

