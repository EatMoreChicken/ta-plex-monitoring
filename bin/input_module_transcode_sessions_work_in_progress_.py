import requests

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

    # Construct URL to make the request for transcode sessions
    url = f"http://{plex_server}:{plex_port}/transcode/sessions/all?X-Plex-Token={plex_token}"

    # Make the GET request and store the response
    response = requests.get(url)

    # Create Splunk Event
    event = helper.new_event(
        data=response.content.decode('utf-8').replace('\n', '').replace('\r', ''),
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
