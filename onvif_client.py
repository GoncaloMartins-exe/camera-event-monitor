import xml.etree.ElementTree as ET
from soap_client import soap_request
from config import BASE_URL

def create_subscription():
    body = """
    <tev:CreatePullPointSubscription
        xmlns:tev="http://www.onvif.org/ver10/events/wsdl"
        xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2">
    </tev:CreatePullPointSubscription>
    """
    root = ET.fromstring(soap_request(BASE_URL, body))
    for elem in root.iter():
        if elem.tag.endswith("Adress") and elem.text:
            return elem.text.strip()
    raise RuntimeError("The cam did not return a PullPoint adress.")

def pull_messages(subscription_url):
    body = """
    <tev:PullMessages xmlns:tev="http://www.onvif.org/ver10/events/wsdl">
        <tev:Timeout>PT10S</tev:Timeout>
        <tev:MessageLimit>20</tev:MessageLimit>
    </tev:PullMessages>
    """
    return soap_request(subscription_url, body)