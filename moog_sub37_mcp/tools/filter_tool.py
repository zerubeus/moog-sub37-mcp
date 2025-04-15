"""
Filter tools for controlling filter and filter envelope parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_filter_tools(mcp: FastMCP, midi: MIDIManager):
    """
    Register all filter and filter envelope tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_filter_multidrive(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter Multidrive with high resolution.

        Args:
            value (int): High-resolution value for Filter Multidrive (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 18, 50, value)

    @mcp.tool()
    def set_filter_cutoff(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter Cutoff with high resolution.

        Args:
            value (int): High-resolution value for Filter Cutoff (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 19, 51, value)

    @mcp.tool()
    def set_filter_resonance(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter Resonance with high resolution.

        Args:
            value (int): High-resolution value for Filter Resonance (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 21, 53, value)

    @mcp.tool()
    def set_filter_kb_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter Keyboard Amount with high resolution.

        Args:
            value (int): High-resolution value for Filter Keyboard Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 22, 54, value)

    @mcp.tool()
    def set_filter_eg_attack_time(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Attack Time with high resolution.

        Args:
            value (int): High-resolution value for Filter EG Attack Time (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 23, 55, value)

    @mcp.tool()
    def set_filter_eg_decay_time(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Decay Time with high resolution.

        Args:
            value (int): High-resolution value for Filter EG Decay Time (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 24, 56, value)

    @mcp.tool()
    def set_filter_eg_sustain_time(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Sustain Time with high resolution.

        Args:
            value (int): High-resolution value for Filter EG Sustain Time (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 25, 57, value)

    @mcp.tool()
    def set_filter_eg_release_time(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Release Time with high resolution.

        Args:
            value (int): High-resolution value for Filter EG Release Time (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 26, 58, value)

    @mcp.tool()
    def set_filter_eg_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Amount with high resolution.

        Args:
            value (int): High-resolution value for Filter EG Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 27, 59, value)

    @mcp.tool()
    def set_filter_eg_kb_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Keyboard Amount.

        Args:
            value (int): Value for Filter EG Keyboard Amount (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 79, value)

    @mcp.tool()
    def set_amp_eg_kb_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the AMP EG Keyboard Amount.

        Args:
            value (int): Value for AMP EG Keyboard Amount (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 80, value)

    @mcp.tool()
    def set_filter_eg_reset(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Reset.

        Args:
            value (int): Value for Filter EG Reset (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 82, value)

    @mcp.tool()
    def set_amp_eg_reset(value: int, channel: int = 3):  # type: ignore
        """
        Set the AMP EG Reset.

        Args:
            value (int): Value for AMP EG Reset (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 83, value)

    @mcp.tool()
    def set_filter_eg_vel_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Velocity Amount.

        Args:
            value (int): Value for Filter EG Velocity Amount (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 86, value)

    @mcp.tool()
    def set_amp_eg_vel_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the AMP EG Velocity Amount.

        Args:
            value (int): Value for AMP EG Velocity Amount (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 87, value)

    @mcp.tool()
    def set_filter_eg_delay(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Delay.

        Args:
            value (int): Value for Filter EG Delay (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 103, value)

    @mcp.tool()
    def set_amp_eg_delay(value: int, channel: int = 3):  # type: ignore
        """
        Set the AMP EG Delay.

        Args:
            value (int): Value for AMP EG Delay (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 104, value)

    @mcp.tool()
    def set_filter_eg_hold(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Hold.

        Args:
            value (int): Value for Filter EG Hold (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 105, value)
