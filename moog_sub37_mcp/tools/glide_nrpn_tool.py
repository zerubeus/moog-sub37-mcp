"""
Glide NRPN tools for controlling glide parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_glide_nrpn_tools(mcp: FastMCP, midi: MIDIManager):
    """
    Register all Glide NRPN tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_glide_time_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Time (NRPN 417, MSB 3, LSB 33).
        Args:
            value (int): Value for Glide Time (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 33, value)

    @mcp.tool()
    def set_glide_osc_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide OSC (NRPN 418, MSB 3, LSB 34).
        Args:
            value (int): Value for Glide OSC (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 34, value)

    @mcp.tool()
    def set_glide_type_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Type (NRPN 419, MSB 3, LSB 35).
        Args:
            value (int): Value for Glide Type (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 35, value)

    @mcp.tool()
    def set_glide_gate_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Gate (NRPN 420, MSB 3, LSB 36).
        Args:
            value (int): Value for Glide Gate (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 36, value)

    @mcp.tool()
    def set_glide_legato_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Legato (NRPN 421, MSB 3, LSB 37).
        Args:
            value (int): Value for Glide Legato (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 37, value)

    @mcp.tool()
    def set_glide_on_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide On (NRPN 422, MSB 3, LSB 38).
        Args:
            value (int): Value for Glide On (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 38, value)
