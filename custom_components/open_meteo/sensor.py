"""Support for Open-Meteo weather."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .entity import OpenMeteoEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Open-Meteo weather entity based on a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([OpenMeteoSensorEntity(entry=entry, coordinator=coordinator)])


TEMPERATURE_SENSOR = SensorEntityDescription(
    "temperature", name="Temperature", entity_registry_enabled_default=False
)


class OpenMeteoSensorEntity(OpenMeteoEntity, SensorEntity):
    """Defines an Open-Meteo sensor entity."""

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 0
    entity_description = TEMPERATURE_SENSOR

    @property
    def native_value(self) -> float | None:
        """Return the value reported by the sensor."""
        if not self.coordinator.data.current_weather:
            return None
        return self.coordinator.data.current_weather.temperature
