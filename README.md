<picture>
  <img alt="Open-Meteo Anywhere logo" src="custom_components/open_meteo_anywhere/brand/icon.png">
</picture>

# Open-Meteo Anywhere Home Assistant integration for zones and device trackers

[![Release](https://img.shields.io/github/v/release/natekspencer/hacs-open-meteo?style=for-the-badge)](https://github.com/natekspencer/hacs-open-meteo/releases)
[![HACS Badge](https://img.shields.io/badge/HACS-custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![Buy Me A Coffee/Beer](https://img.shields.io/badge/Buy_Me_A_☕/🍺-F16061?style=for-the-badge&logo=ko-fi&logoColor=white&labelColor=grey)](https://ko-fi.com/natekspencer)
[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor_💜-6f42c1?style=for-the-badge&logo=github&logoColor=white&labelColor=grey)](https://github.com/sponsors/natekspencer)

![Downloads](https://img.shields.io/github/downloads/natekspencer/hacs-open-meteo/total?style=flat-square)
![Latest Downloads](https://img.shields.io/github/downloads/natekspencer/hacs-open-meteo/latest/total?style=flat-square)

Based on the core [Open-Meteo integration](https://www.home-assistant.io/integrations/open_meteo/), with weather forecasts for both zones and device trackers with geolocation data in Home Assistant, installed through [HACS](https://hacs.xyz/docs/setup/download). It can run alongside the core integration.

## ⬇️ Installation

### HACS (Recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=natekspencer&repository=hacs-open-meteo&category=integration)

1. Use the **My Home Assistant** badge above, or from within Home Assistant, click on **HACS**
2. Click the vertical ellipsis (⋮) → **Custom repositories**
3. Enter `natekspencer/hacs-open-meteo` in the _Repository_ field and select `Integration` in the _Type_ dropdown
4. Click **ADD**
5. Close the _Custom repositories_ window
6. Search for `Open-Meteo Anywhere` and click on the appropriate repository
7. Click **DOWNLOAD**
8. Restart Home Assistant

### Manual

If you prefer manual installation:

1. Download or clone this repository
2. Copy the `custom_components/open_meteo_anywhere` folder to your Home Assistant `custom_components` directory
3. Restart Home Assistant

> ⚠️ Manual installation will not provide automatic update notifications. HACS installation is recommended unless you have a specific need.

## ⬆️ Upgrading from the `open_meteo` domain

This integration used to replace the core Open-Meteo integration using the `open_meteo` domain. It now uses `open_meteo_anywhere`, and existing locations don't move over automatically.

1. Make sure Home Assistant is version 2026.11.0 or later, as older versions can't install the new release
2. Note the entity IDs you use in automations and dashboards
3. Delete your Open-Meteo entries in [Settings > Devices & services](https://my.home-assistant.io/redirect/integrations/)
4. In HACS, remove the integration and its custom repository, then add the repository again and download **Open-Meteo Anywhere** using the [HACS installation steps](#hacs-recommended)
5. If the old `custom_components/open_meteo` folder is still there, delete it, as it would keep overriding the core integration
6. Restart Home Assistant
7. Add your locations again using **Open-Meteo Anywhere**
8. If you used the temperature sensor, enable it, as it's disabled by default and renaming it won't enable it
9. Rename the new entities to your old entity IDs

## ➕ Setup

Once installed, you can set up the integration by clicking on the following badge:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=open_meteo_anywhere)

Alternatively:

1. Go to [Settings > Devices & services](https://my.home-assistant.io/redirect/integrations/)
2. In the bottom-right corner, select **Add integration**
3. Type `Open-Meteo Anywhere` and select the **Open-Meteo Anywhere** integration
4. Follow the instructions to add the integration to your Home Assistant

## ❤️ Support Me

I maintain this Home Assistant integration in my spare time. If you find it useful, consider supporting development:

- 💜 [Sponsor me on GitHub](https://github.com/sponsors/natekspencer)
- ☕ [Buy me a coffee / beer](https://ko-fi.com/natekspencer)
- 💸 [PayPal (direct support)](https://www.paypal.com/paypalme/natekspencer)
- ⭐ [Star this project](https://github.com/natekspencer/hacs-open-meteo)
- 📦 If you’d like to support in other ways, such as donating hardware for testing, feel free to [reach out to me](https://github.com/natekspencer)

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=natekspencer/hacs-open-meteo)](https://www.star-history.com/#natekspencer/hacs-open-meteo)
