import xml.etree.ElementTree as ET
from datetime import date
from xml.dom import minidom
import os

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
    ET.SubElement(channel, 'link').text = 'https://raw.githubusercontent.com/rajkboddu/christmas-countdown-rss/main/christmas_countdown.xml'
    ET.SubElement(channel, 'description').text = f'{days_remaining}'

    # Countdown item
    item = ET.SubElement(channel, 'item')
    ET.SubElement(item, 'title').text = f'{days_remaining}'
    ET.SubElement(item, 'description').text = f'Countdown update: {days_remaining} days until Christmas!'
    ET.SubElement(item, 'pubDate').text = date.today().strftime('%a, %d %b %Y 00:00:00 GMT')

    # Pretty print the XML
    rough_string = ET.tostring(rss, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    
    return reparsed.toprettyxml(indent="  ")

# Main execution
def main():
    rss_content = generate_christmas_countdown_rss()
    
    # Ensure we're in the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'christmas_countdown.xml')
    
    with open(file_path, 'w') as f:
        f.write(rss_content)
    print(f"RSS feed generated successfully at {file_path}")

if __name__ == "__main__":
    main()
