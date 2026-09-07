# C240I ONVIF Event Monitor

Monitor ONVIF events (people detection, intrusion, movement, etc.)
of a camera IP through PullPoint Subscription.

## Configuration

1. Create and activate the venv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. `pip install -r requirements.txt`
3. `python monitor.py`

## Structure

- `config.py`        - Environment variables
- `soap_client.py`   - client HTTP/SOAP with digest authentication
- `onvif_client.py`  - subscription and pull of messages ONVIF
- `events.py`        - exhibition and parsing of events
- `monitor.py`       - main loop with automatic reconnection