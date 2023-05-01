{% if prerelease %}

This integration is a pre-release version.
It may contain bugs or break functionality in addition to adding new features and fixes. Please review open issues and submit new ones to the [GitHub issue tracker](https://github.com/natekspencer/hacs-open-meteo/issues).

{% endif %}

# Open-Meteo Home Assistant integration for zones and device trackers

[![GitHub Release][releases-shield]][releases]
![GitHub all releases][download-all]
![GitHub release (latest by SemVer)][download-latest]
[![GitHub Activity][commits-shield]][commits]

Replaces the existing [Open-Meteo integration](https://www.home-assistant.io/integrations/open_meteo/) to allow weather forecasts for both zones and device trackers in Home Assistant, installed through [HACS](https://hacs.xyz/docs/setup/download).

{% if not installed %}

## Installation

1. Click install.
2. Reboot Home Assistant.
3. Hard refresh browser cache.
4. [![Add Integration][add-integration-badge]][add-integration] or in the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Open-Meteo".

{% endif %}

## Configuration

The configuration flow is as follows:

1. **Location (required)**
   - Select a location (zone or device tracker) to obtain weather information based on the latitude and longitude.

[commits-shield]: https://img.shields.io/github/commit-activity/w/natekspencer/hacs-open-meteo?style=flat-square
[commits]: https://github.com/natekspencer/hacs-open-meteo/commits/main
[releases-shield]: https://img.shields.io/github/release/natekspencer/hacs-open-meteo.svg?style=flat-square
[releases]: https://github.com/natekspencer/hacs-open-meteo/releases
[download-all]: https://img.shields.io/github/downloads/natekspencer/hacs-open-meteo/total?style=flat-square
[download-latest]: https://img.shields.io/github/downloads/natekspencer/hacs-open-meteo/latest/total?style=flat-square
[add-integration]: https://my.home-assistant.io/redirect/config_flow_start?domain=open_meteo
[add-integration-badge]: https://my.home-assistant.io/badges/config_flow_start.svg
