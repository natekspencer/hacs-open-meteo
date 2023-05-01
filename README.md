# Open-Meteo Home Assistant integration for zones and device trackers

[![GitHub Release][releases-shield]][releases]
![GitHub all releases][download-all]
![GitHub release (latest by SemVer)][download-latest]
[![GitHub Activity][commits-shield]][commits]

Replaces the existing [Open-Meteo integration](https://www.home-assistant.io/integrations/open_meteo/) to allow weather forecasts for both zones and device trackers in Home Assistant, installed through [HACS](https://hacs.xyz/docs/setup/download).

## Installation

1. Use [HACS](https://hacs.xyz/docs/setup/download). In HACS add a custom repository by going to `HACS > Integrations > 3 dots > custom repositories` and add this github repo `https://github.com/natekspencer/hacs-open-meteo`. Now skip to 7.
2. If no HACS, use the tool of choice to open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
3. If you do not have a `custom_components` directory (folder) there, you need to create it.
4. In the `custom_components` directory (folder) create a new folder called `open_meteo`.
5. Download _all_ the files from the `custom_components/open_meteo/` directory (folder) in this repository.
6. Place the files you downloaded in the new directory (folder) you created.
7. Restart Home Assistant.
8. [![Add Integration][add-integration-badge]][add-integration] or in the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Open-Meteo".

## Configuration

The configuration flow is as follows:

1. **Location (required)**
   - Select a location (zone or device tracker) to obtain weather information based on the latitude and longitude.

---

[commits-shield]: https://img.shields.io/github/commit-activity/w/natekspencer/hacs-open-meteo?style=flat-square
[commits]: https://github.com/natekspencer/hacs-open-meteo/commits/main
[releases-shield]: https://img.shields.io/github/release/natekspencer/hacs-open-meteo.svg?style=flat-square
[releases]: https://github.com/natekspencer/hacs-open-meteo/releases
[download-all]: https://img.shields.io/github/downloads/natekspencer/hacs-open-meteo/total?style=flat-square
[download-latest]: https://img.shields.io/github/downloads/natekspencer/hacs-open-meteo/latest/total?style=flat-square
[add-integration]: https://my.home-assistant.io/redirect/config_flow_start?domain=open_meteo
[add-integration-badge]: https://my.home-assistant.io/badges/config_flow_start.svg
