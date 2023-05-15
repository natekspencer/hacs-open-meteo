"""Support for Open-Meteo entity."""
from __future__ import annotations

from open_meteo import Forecast

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import DOMAIN


class OpenMeteoEntity(CoordinatorEntity[DataUpdateCoordinator[Forecast]]):
    """Defines an Open-Meteo entity base class."""

    _attr_has_entity_name = True

    def __init__(
        self, *, entry: ConfigEntry, coordinator: DataUpdateCoordinator[Forecast]
    ) -> None:
        """Initialize Open-Meteo weather entity."""
        super().__init__(coordinator=coordinator)
        self._attr_unique_id = f"{entry.entry_id}{f'-{self.entity_description.key}' if hasattr(self, 'entity_description') else ''}"

        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, entry.entry_id)},
            manufacturer="Open-Meteo",
            name=entry.title,
        )
