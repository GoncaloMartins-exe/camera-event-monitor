import requests
from requests.auth import HTTPDigestAuth
from config import USER, PASSWORD, REQUEST_TIMEOUT

session = requests.Session()
session.auth = HTTPDigestAuth(USER, PASSWORD)
session.headers.update({
    "Content-Type": "application/soap+xml; charset=utf-8"
})

def soap_request(url, body):
    envelope = f"""<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
    <s:Body>
        {body}
    </s:Body>
</s:Envelope>"""

    response = session.post(
        url,
        data=envelope.encode("utf-8"),
        timeout=REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.text