import xml.etree.ElementTree as ET
from datetime import date
from xml.dom import minidom

def generate_christmas_countdown_rss():
    """
    Generate a simple, static RSS feed for Christmas 2024 countdown
    compatible with web hosting.
    """
    # Calculate days to Christmas
    christmas_2024 = date(2024, 12, 25)
    today = date.today()
    days_remaining = (christmas_2024 - today).days

    # Create RSS root
    rss = ET.Element('rss', {'version': '2.0'})
    channel = ET.SubElement(rss, 'channel')

    # Channel metadata
    ET.SubElement(channel, 'title').text = 'Christmas 2024 Countdown'
    ET.SubElement(channel, 'link').text = 'https://raw.githubusercontent.com/YOUR_USERNAME/christmas-countdown-rss/main/christmas_countdown.xml'
    ET.SubElement(channel, 'description').text = f'{days_remaining} days to Christmas 2024'

    # Countdown item
    item = ET.SubElement(channel, 'item')
    ET.SubElement(item, 'title').text = f'{days_remaining} Days to Christmas 2024'
    ET.SubElement(item, 'description').text = f'Countdown update: {days_remaining} days until Christmas!'
    ET.SubElement(item, 'pubDate').text = date.today().strftime('%a, %d %b %Y 00:00:00 GMT')

    # Pretty print the XML
    rough_string = ET.tostring(rss, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    
    return reparsed.toprettyxml(indent="  ")
