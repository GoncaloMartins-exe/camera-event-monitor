import xml.etree.ElementTree as ET

EVENTS = {
    "people": ("IsPeople", "Person detected", "Person is no longer detected"),
    "intrusion": ("IsIntrusion", "Intrusion detected", "Intrusion ended"),
    "linecross": ("IsLineCross", "Crossed Line", None),
    "motion": ("IsMotion", "Movement Detected", None),
    "tamper": ("IsTamper", "Camera blocked", None),
}

def parse_events(xml):
    root = ET.fromstring(xml)
    events = []

    for message in root.iter():
        if not message.tag.endswith("NotificationMessage"):
            continue

        topic = None
        data = {}

        for child in message:
            if child.tag.endswith("Topic"):
                topic = "".join(child.itertext()).strip()
            elif child.tag.endswith("Message"):
                for item in child.iter():
                    name = item.attrib.get("Name")
                    value = item.attrib.get("Value")
                    if name and value is not None:
                        data[name] = value

        if topic:
            events.append((topic, data))

    return events