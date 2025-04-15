"""
LFO NRPN tools for controlling LFO parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_lfo_nrpn_tools(mcp: FastMCP, midi: MIDIManager):
    """
    Register all LFO NRPN tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_lfo1_rate_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 Rate (NRPN 423, MSB 3, LSB 39).
        Args:
            value (int): Value for LFO 1 Rate (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 39, value)

    @mcp.tool()
    def set_lfo1_range_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 Range (NRPN 424, MSB 3, LSB 40).
        Args:
            value (int): Value for LFO 1 Range (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 40, value)

    @mcp.tool()
    def set_lfo1_sync_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 Sync (NRPN 425, MSB 3, LSB 41).
        Args:
            value (int): Value for LFO 1 Sync (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 41, value)

    @mcp.tool()
    def set_lfo1_kb_reset_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 KB Reset (NRPN 426, MSB 3, LSB 42).
        Args:
            value (int): Value for LFO 1 KB Reset (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 42, value)

    @mcp.tool()
    def set_lfo1_clk_div_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 Clock Divider (NRPN 427, MSB 3, LSB 43).
        Args:
            value (int): Value for LFO 1 Clock Divider (0-20).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 43, value)

    @mcp.tool()
    def set_lfo1_clk_src_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 Clock Source (NRPN 428, MSB 3, LSB 44).
        Args:
            value (int): Value for LFO 1 Clock Source (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 44, value)

    @mcp.tool()
    def set_lfo1_kb_track_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 KB Track (NRPN 430, MSB 3, LSB 46).
        Args:
            value (int): Value for LFO 1 KB Track (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 46, value)

    @mcp.tool()
    def set_lfo2_rate_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 Rate (NRPN 448, MSB 3, LSB 64).
        Args:
            value (int): Value for LFO 2 Rate (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 64, value)

    @mcp.tool()
    def set_lfo2_range_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 Range (NRPN 449, MSB 3, LSB 65).
        Args:
            value (int): Value for LFO 2 Range (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 65, value)

    @mcp.tool()
    def set_lfo2_sync_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 Sync (NRPN 450, MSB 3, LSB 66).
        Args:
            value (int): Value for LFO 2 Sync (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 66, value)

    @mcp.tool()
    def set_lfo2_kb_reset_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 KB Reset (NRPN 451, MSB 3, LSB 67).
        Args:
            value (int): Value for LFO 2 KB Reset (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 67, value)

    @mcp.tool()
    def set_lfo2_clk_div_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 Clock Divider (NRPN 452, MSB 3, LSB 68).
        Args:
            value (int): Value for LFO 2 Clock Divider (0-20).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 68, value)

    @mcp.tool()
    def set_lfo2_clk_src_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 Clock Source (NRPN 453, MSB 3, LSB 69).
        Args:
            value (int): Value for LFO 2 Clock Source (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 69, value)

    @mcp.tool()
    def set_lfo2_kb_track_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 2 KB Track (NRPN 455, MSB 3, LSB 71).
        Args:
            value (int): Value for LFO 2 KB Track (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 71, value)
