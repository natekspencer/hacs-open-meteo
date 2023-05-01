"""Config flow to configure the Open-Meteo integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.components.device_tracker import DOMAIN as DEVICE_TRACKER_DOMAIN
from homeassistant.components.zone import DOMAIN as ZONE_DOMAIN
from homeassistant.config_entries import ConfigEntry, ConfigFlow
from homeassistant.const import CONF_SCAN_INTERVAL, CONF_ZONE
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaFlowFormStep,
    SchemaOptionsFlowHandler,
)
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .const import DOMAIN

OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_SCAN_INTERVAL, default=30): int,
    }
)
OPTIONS_FLOW = {
    "init": SchemaFlowFormStep(OPTIONS_SCHEMA),
}


class OpenMeteoFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for OpenMeteo."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler:
        """Get the options flow for this handler."""
        return SchemaOptionsFlowHandler(config_entry, OPTIONS_FLOW)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initialized by the user."""
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_ZONE])
            self._abort_if_unique_id_configured()

            state = self.hass.states.get(user_input[CONF_ZONE])
            return self.async_create_entry(
                title=state.name if state else "Open-Meteo",
                data={CONF_ZONE: user_input[CONF_ZONE]},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_ZONE): EntitySelector(
                        EntitySelectorConfig(
                            domain=[ZONE_DOMAIN, DEVICE_TRACKER_DOMAIN]
                        ),
                    ),
                }
            ),
        )
