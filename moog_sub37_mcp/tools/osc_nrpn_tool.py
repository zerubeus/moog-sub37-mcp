"""
Oscillator NRPN tools for controlling oscillator parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_osc_nrpn_tools(mcp: FastMCP, midi: MIDIManager):
    """
    Register all Oscillator NRPN tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_osc1_octave_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 OCTAVE (NRPN 479, MSB 3, LSB 95).
        Args:
            value (int): Value for OSC 1 OCTAVE (0-3).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 95, value)

    @mcp.tool()
    def set_osc1_wave_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 WAVE (NRPN 480, MSB 3, LSB 96).
        Args:
            value (int): Value for OSC 1 WAVE (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 96, value)

    @mcp.tool()
    def set_osc2_hard_sync_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 HARD SYNC (NRPN 481, MSB 3, LSB 97).
        Args:
            value (int): Value for OSC 2 HARD SYNC (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 97, value)

    @mcp.tool()
    def set_osc_kb_reset_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC KB RESET (NRPN 482, MSB 3, LSB 98).
        Args:
            value (int): Value for OSC KB RESET (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 98, value)

    @mcp.tool()
    def set_osc2_octave_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 OCTAVE (NRPN 483, MSB 3, LSB 99).
        Args:
            value (int): Value for OSC 2 OCTAVE (0-3).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 99, value)

    @mcp.tool()
    def set_osc2_wave_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 WAVE (NRPN 484, MSB 3, LSB 100).
        Args:
            value (int): Value for OSC 2 WAVE (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 100, value)

    @mcp.tool()
    def set_osc2_kb_ctrl_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 KB CTRL (NRPN 485, MSB 3, LSB 101).
        Args:
            value (int): Value for OSC 2 KB CTRL (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 101, value)

    @mcp.tool()
    def set_osc2_duo_mode_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 DUO MODE (NRPN 486, MSB 3, LSB 102).
        Args:
            value (int): Value for OSC 2 DUO MODE (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 102, value)

    @mcp.tool()
    def set_osc2_frequency_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 FREQUENCY (NRPN 487, MSB 3, LSB 103).
        Args:
            value (int): Value for OSC 2 FREQUENCY (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 103, value)

    @mcp.tool()
    def set_osc2_beat_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 BEAT (NRPN 488, MSB 3, LSB 104).
        Args:
            value (int): Value for OSC 2 BEAT (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 104, value)

    @mcp.tool()
    def set_osc1_level_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 LEVEL (NRPN 489, MSB 3, LSB 105).
        Args:
            value (int): Value for OSC 1 LEVEL (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 105, value)

    @mcp.tool()
    def set_osc1_on_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 ON (NRPN 490, MSB 3, LSB 106).
        Args:
            value (int): Value for OSC 1 ON (0-20).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 106, value)

    @mcp.tool()
    def set_sub_osc_on_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the SUB OSC ON (NRPN 491, MSB 3, LSB 107).
        Args:
            value (int): Value for SUB OSC ON (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 107, value)

    @mcp.tool()
    def set_sub_osc_level_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the SUB OSC LEVEL (NRPN 492, MSB 3, LSB 108).
        Args:
            value (int): Value for SUB OSC LEVEL (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 108, value)

    @mcp.tool()
    def set_osc2_level_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 LEVEL (NRPN 493, MSB 3, LSB 109).
        Args:
            value (int): Value for OSC 2 LEVEL (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 109, value)

    @mcp.tool()
    def set_osc2_on_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 ON (NRPN 494, MSB 3, LSB 110).
        Args:
            value (int): Value for OSC 2 ON (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 110, value)

    @mcp.tool()
    def set_noise_on_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the NOISE ON (NRPN 495, MSB 3, LSB 111).
        Args:
            value (int): Value for NOISE ON (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 111, value)

    @mcp.tool()
    def set_noise_level_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the NOISE LEVEL (NRPN 496, MSB 3, LSB 112).
        Args:
            value (int): Value for NOISE LEVEL (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 112, value)

    @mcp.tool()
    def set_fb_ext_level_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FB EXT LEVEL (NRPN 497, MSB 3, LSB 113).
        Args:
            value (int): Value for FB EXT LEVEL (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 113, value)

    @mcp.tool()
    def set_fb_ext_on_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FB EXT ON (NRPN 498, MSB 3, LSB 114).
        Args:
            value (int): Value for FB EXT ON (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 114, value)
