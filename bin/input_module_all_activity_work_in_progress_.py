import requests
import xml.etree.ElementTree as ET

def validate_input(helper, definition):
    pass

def collect_events(helper, ew):
    # Get global settings
    unique_account_name = helper.get_global_setting("unique_account_name")
    plex_server = helper.get_global_setting("plex_server")
    plex_port = helper.get_global_setting("plex_port")
    plex_token = helper.get_global_setting("plex_token")

    # Check if all required settings are available
    if not unique_account_name or not plex_server or not plex_port or not plex_token:
        raise ValueError('One or more required global settings are missing or empty')

    # Construct URL to make the request for activities
    url = f"http://{plex_server}:{plex_port}/activities/?X-Plex-Token={plex_token}"

    # Make the GET request and store the response
    response = requests.get(url)

    # Parse the XML response using ElementTree
    response_xml = ET.fromstring(response.content)

    # Loop through the activity elements in the XML and create an event for each one
    for child in response_xml:
        xml_item = ET.tostring(child, encoding='unicode')

        # Create Splunk Event
        event = helper.new_event(
            data=xml_item.replace('\n', '').replace('\r', ''),
            time=None,
            host=plex_server,
            index=helper.get_output_index(),
            source=helper.get_input_type(),
            sourcetype=helper.get_sourcetype(),
            done=True,
            unbroken=True
        )

        # Write the event to Splunk
        ew.write_event(event)
