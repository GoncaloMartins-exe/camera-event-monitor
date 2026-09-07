import time
import requests
import traceback 
import xml.etree.ElementTree as ET

from config import IP, RECONNECT_DELAY
from onvif_client import create_subscription, pull_messages
from events import parse_events, display_event

def monitor():
    subscription_url = None

    while True:
        try:
            if subscription_url is None:
                print("Creating subscription ONVIF...", flush=True)
                subscription_url = create_subscription()
                print("Subscrition created", flush=True)
                print("Waiting for events...", flush=True)
                print("_________________________________", flush=True)

            for topic, data in parse_events(pull_messages(subscription_url)):
                display_event(topic, data)

        except requests.RequestException:
            print("[WARNING] Subscription lost. Renewing...", flush=True)
            subscription_url = None
            time.sleep(RECONNECT_DELAY)

        except ET.ParseError:
            print("[WARNING] Invalid answer from camera. Renewing..", flush=True)
            subscription_url = None
            time.sleep(RECONNECT_DELAY)

        except Exception as e:
            traceback.print_exc()
            subscription_url = None
            time.sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    print("------------------------")
    print("  C240I EVENT MONITOR")
    print("------------------------")
    print(f"Camera: {IP}")
    print("------------------------")

    try:
        monitor()
    except KeyboardInterrupt:
        print("\nMonitor terminated")