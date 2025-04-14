"""
MIDI Interface

This module handles MIDI communication.
It provides functionality for connecting to MIDI devices over USB,
selecting channels, and sending control change (CC) messages
"""

import logging
from typing import Optional

import mido

logger = logging.getLogger(__name__)


class MIDIManager:
    """Interface for MIDI communication."""

    def __init__(self, port_name: str):
        """
        Initialize the MIDI interface.

        Args:
            port_name: Name of the MIDI port to use.
        """
        self.input_port: Optional[mido.ports.BaseInput] = None
        self.output_port: Optional[mido.ports.BaseOutput] = None
        self.connected = False

        if port_name:
            self.connect(port_name)

    def list_ports(self) -> list[str]:
        """List available MIDI ports."""
        inputs = mido.get_input_names()  # type: ignore[attr-defined]
        outputs = mido.get_output_names()  # type: ignore[attr-defined]
        return list(set(inputs + outputs))  # type: ignore[arg-type]

    def connect(self, port_name: str) -> bool:
        """
        Connect to the specified MIDI port.

        Args:
            port_name: Name of the MIDI port to connect to

        Returns:
            bool: True if connection successful, False otherwise.
        """
        try:
            # Close existing connections if any
            self.disconnect()

            # Open new connections
            self.output_port = mido.open_output(port_name)  # type: ignore[attr-defined]
            try:
                self.input_port = mido.open_input(port_name)  # type: ignore[attr-defined]
            except (OSError, ValueError) as e:
                logger.warning(f'Could not open input port {port_name}: {e}')

            self.connected = True
            logger.info(f'Connected to MIDI port: {port_name}')
            return True
        except (OSError, ValueError) as e:
            logger.error(f'Failed to connect to MIDI port {port_name}: {e}')
            self.disconnect()
            return False

    def disconnect(self) -> None:
        """Close all MIDI connections."""
        if self.input_port:  # type: ignore[truthy-bool]
            self.input_port.close()  # type: ignore[attr-defined]
            self.input_port = None

        if self.output_port:  # type: ignore[truthy-bool]
            self.output_port.close()  # type: ignore[attr-defined]
            self.output_port = None

        self.connected = False

    def send_cc(self, channel: int, cc: int, value: int) -> bool:
        """
        Send a Control Change (CC) message.

        Args:
            channel: MIDI channel (1-16)
            cc: Control Change number (0-127)
            value: Control Change value (0-127)

        Returns:
            bool: True if message sent successfully, False otherwise.
        """
        if not self.connected or not self.output_port:  # type: ignore[truthy-bool]
            logger.error('Not connected to any MIDI port')
            return False

        # Convert 1-indexed channel to 0-indexed
        if 1 <= channel <= 16:
            channel = channel - 1
        else:
            logger.error(f'Invalid channel: {channel}. Must be between 1-16.')
            return False

        try:
            # Create and send the CC message
            msg = mido.Message('control_change', channel=channel, control=cc, value=value)
            self.output_port.send(msg)  # type: ignore[attr-defined]
            logger.debug(f'Sent CC: channel={channel + 1}, cc={cc}, value={value}')
            return True
        except Exception as e:
            logger.error(f'Error sending CC message: {e}')
            return False
