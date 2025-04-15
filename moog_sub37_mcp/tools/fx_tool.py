"""
FX and Misc tools for controlling FX, arpeggiator, and other parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_fx_tools(mcp: FastMCP, midi: MIDIManager):
    """
    Register all FX, arpeggiator, and misc tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_glide_time(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Time with high resolution.

        Args:
            value (int): High-resolution value for Glide Time (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 5, 37, value)

    @mcp.tool()
    def set_master_volume(value: int, channel: int = 3):  # type: ignore
        """
        Set the Master Volume with high resolution.

        Args:
            value (int): High-resolution value for Master Volume (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 7, 39, value)

    @mcp.tool()
    def set_hold_pedal(value: int, channel: int = 3):  # type: ignore
        """
        Set the Hold Pedal/Sustain.

        Args:
            value (int): Value for Hold Pedal (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 64, value)

    @mcp.tool()
    def set_glide(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide On/Off.

        Args:
            value (int): Value for Glide (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 65, value)

    @mcp.tool()
    def set_arpeggiator_latch(value: int, channel: int = 3):  # type: ignore
        """
        Set the Arpeggiator Latch.

        Args:
            value (int): Value for Arpeggiator Latch (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 69, value)

    @mcp.tool()
    def set_arp_on_off(value: int, channel: int = 3):  # type: ignore
        """
        Set the Arpeggiator On/Off.

        Args:
            value (int): Value for Arpeggiator (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 73, value)

    @mcp.tool()
    def set_glide_type(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Type.

        Args:
            value (int): Value for Glide Type (0 = LCR, 43 = LCT, 85 = EXP).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 85, value)

    @mcp.tool()
    def set_glide_legato(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Legato On/Off.

        Args:
            value (int): Value for Glide Legato (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 94, value)

    @mcp.tool()
    def set_glide_dest_osc(value: int, channel: int = 3):  # type: ignore
        """
        Set the Glide Destination OSC 1/2/BOTH.

        Args:
            value (int): Value for Glide Destination (0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 102, value)

    @mcp.tool()
    def set_kb_octave(value: int, channel: int = 3):  # type: ignore
        """
        Set the Keyboard Octave.

        Args:
            value (int): Value for Keyboard Octave (0 = -2 Oct, 26 = -1 Oct, 51 = +0 Oct, 77 = +1 Oct, 102 = +2 Oct).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 89, value)

    @mcp.tool()
    def set_filter_eg_multi_trig(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter EG Multi Trig.

        Args:
            value (int): Value for Filter EG Multi Trig (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 112, value)

    @mcp.tool()
    def set_amp_eg_multi_trig(value: int, channel: int = 3):  # type: ignore
        """
        Set the AMP EG Multi Trig.

        Args:
            value (int): Value for AMP EG Multi Trig (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 113, value)

    @mcp.tool()
    def set_local_control(value: int, channel: int = 3):  # type: ignore
        """
        Set Local Control On/Off.

        Args:
            value (int): Value for Local Control (0 = OFF, 127 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 122, value)

    @mcp.tool()
    def set_bank_select(value: int, channel: int = 3):  # type: ignore
        """
        Set the Bank Select (MSB).

        Args:
            value (int): Value for Bank Select (should always be 0).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 0, value)

    @mcp.tool()
    def set_bank_select_lsb(value: int, channel: int = 3):  # type: ignore
        """
        Set the Bank Select (LSB).

        Args:
            value (int): Value for Bank Select LSB (0 = Banks 1–8, 1 = Banks 9–16).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 32, value)

    @mcp.tool()
    def set_mod_wheel(value: int, channel: int = 3):  # type: ignore
        """
        Set the Mod Wheel (normal resolution).

        Args:
            value (int): Value for Mod Wheel (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 1, value)

    @mcp.tool()
    def set_mod_wheel_high_res(value: int, channel: int = 3):  # type: ignore
        """
        Set the Mod Wheel (high resolution).

        Args:
            value (int): High-resolution value for Mod Wheel (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 1, 33, value)
