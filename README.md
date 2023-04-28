# 🚀 Plex Monitoring

## 📝 Overview
The Plex Monitoring add-on is designed to extract data from the Plex API and index it in Splunk. It allows users to monitor and analyze various metrics and events from their Plex server.

## 💻 Installation
1. Install Plex Monitoring via the `tar.gz`.
2. Open the app and navigate to **Configuration** > **Add-on Settings**.
3. Fill in the required information. Please note that you can visit [this documentation](https://www.plexopedia.com/plex-media-server/general/plex-token/) for information on retrieving your Plex token.

## 🎬 Getting Started
To start ingesting data, simply navigate to the **Inputs** tab of the app, click **Create New Input**, and populate the necessary information. From there, you can start exploring your Plex data in the Splunk platform.

## 🤝 Contributing
Please feel free to contribute to the Source Scout project by creating pull requests, filing bug reports, or providing feedback.

## 📈 Metrics and Data
Here are the data sets that can be extracted from the Plex API with the Plex Monitoring add-on currently (Visit [this documentation](https://www.plexopedia.com/plex-media-server/api/) for more information regarding the API):
- Server Identity
- Server Preferences
- Server Capabilities
- Accounts
- Devices
- Library Sections
- Scheduled Tasks
- Transcode Sessions *(Work-in-Progress)*
- Sessions History *(Work-in-Progress)*
- All Activity *(Work-in-Progress)*

## 📝 To-Do
- [ ] Implement script logging to Splunk with log-levels
- [ ] Improve plex:sessions-history by implementing check pointing and filtering so that old logs aren't re-indexed
- [ ] Fix logging on plex:all-activity and plex:transcode-sessions
- [ ] Add API filtering capabilities
- [ ] Pull all available media statistics
- [ ] Add alert actions:
  - [ ] Stop an activity
  - [ ] Terminate a session
  - [ ] Scan libraries
  - [ ] Refresh metadata for a library
  - [ ] Update media play progress
  - [ ] Empty trash
  - [ ] Clean bundles
  - [ ] Optimize database
  - [ ] Run backup database task
  - [ ] Run optimize database task
  - [ ] Run clean old bundles task
  - [ ] Run clean old cache files task