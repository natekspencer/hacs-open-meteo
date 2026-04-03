"""Support for Open-Meteo entity."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import OpenMeteoConfigEntry, OpenMeteoDataUpdateCoordinator


class OpenMeteoEntity(CoordinatorEntity[OpenMeteoDataUpdateCoordinator]):
    """Defines an Open-Meteo entity base class."""

    _attr_has_entity_name = True

    def __init__(
        self,
        *,
        entry: OpenMeteoConfigEntry,
        coordinator: OpenMeteoDataUpdateCoordinator,
    ) -> None:
        """Initialize Open-Meteo entity."""
        super().__init__(coordinator=coordinator)
        self._attr_unique_id = f"{entry.entry_id}{f'-{self.entity_description.key}' if hasattr(self, 'entity_description') else ''}"

        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, entry.entry_id)},
            manufacturer="Open-Meteo",
            name=entry.title,
        )
