"""
Oscillator and Mod 2 tools for controlling oscillator and Mod 2 parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_osc_tools(mcp: FastMCP, midi: MIDIManager):
    """
    Register all oscillator and Mod 2 tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_osc1_wave(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 Wave with high resolution.

        Args:
            value (int): High-resolution value for OSC 1 Wave (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 9, 41, value)

    @mcp.tool()
    def set_osc2_freq(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 Frequency with high resolution.

        Args:
            value (int): High-resolution value for OSC 2 Frequency (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 12, 44, value)

    @mcp.tool()
    def set_osc2_beat_freq(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 Beat Frequency with high resolution.

        Args:
            value (int): High-resolution value for OSC 2 Beat Frequency (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 13, 45, value)

    @mcp.tool()
    def set_osc2_wave(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 Wave with high resolution.

        Args:
            value (int): High-resolution value for OSC 2 Wave (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 14, 46, value)

    @mcp.tool()
    def set_mod2_pitch_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 Pitch Amount with high resolution.

        Args:
            value (int): High-resolution value for MOD 2 Pitch Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 15, 47, value)

    @mcp.tool()
    def set_mod2_filter_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 Filter Amount with high resolution.

        Args:
            value (int): High-resolution value for MOD 2 Filter Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 16, 48, value)

    @mcp.tool()
    def set_mod2_pgm_dest_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 Programmable Destination Amount with high resolution.

        Args:
            value (int): High-resolution value for MOD 2 Programmable Destination Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 17, 49, value)

    @mcp.tool()
    def set_mod2_source(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 Source selection.

        Args:
            value (int): Value for source selection (0 = TRIANGLE LFO, 21 = SQUARE LFO, 43 = SAW LFO, 64 = RAMP LFO, 85 = S&H LFO, 107 = F.EG/PGM).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 72, value)

    @mcp.tool()
    def set_osc1_octave(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 Octave.

        Args:
            value (int): Value for OSC 1 Octave (0 = 16', 32 = 8', 64 = 4', 96 = 2').
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 74, value)

    @mcp.tool()
    def set_osc2_octave(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 Octave.

        Args:
            value (int): Value for OSC 2 Octave (0 = 16', 32 = 8', 64 = 4', 96 = 2').
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 75, value)

    @mcp.tool()
    def set_osc2_hard_sync(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 Hard Sync On/Off.

        Args:
            value (int): Value for OSC 2 Hard Sync (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 77, value)

    @mcp.tool()
    def set_osc_kb_reset(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC Keyboard Reset On/Off.

        Args:
            value (int): Value for OSC Keyboard Reset (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 81, value)

    @mcp.tool()
    def set_mod2_osc_1_2_sel(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 Oscillator 1/2 Selection.

        Args:
            value (int): Value for oscillator selection (0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 88, value)

    @mcp.tool()
    def set_mod2_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 Destination selection.

        Args:
            value (int): Value for destination selection (0 = LF01 Rate, 18 = VCA Level, 37 = OSC1 Wave, 55 = OSC1 + OSC2 Wave, 73 = OSC2 Wave, 91 = Noise Level, 110 = EG Time/PGM).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 92, value)

    @mcp.tool()
    def set_pitch_bend_up_amount(value: int, channel: int = 3):  # type: ignore
        """
        Set the Pitch Bend Up Amount.

        Args:
            value (int): Value for Pitch Bend Up Amount (0-24, in semitones).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 107, value)

    @mcp.tool()
    def set_pitch_bend_down_amount(value: int, channel: int = 3):  # type: ignore
        """
        Set the Pitch Bend Down Amount.

        Args:
            value (int): Value for Pitch Bend Down Amount (0-24, in semitones).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 108, value)

    @mcp.tool()
    def set_filter_slopes(value: int, channel: int = 3):  # type: ignore
        """
        Set the Filter Slopes (Poles).

        Args:
            value (int): Value for Filter Slopes (0 = -6dB, 32 = -12dB, 64 = -18dB, 96 = -24dB).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 109, value)

    @mcp.tool()
    def set_osc_duo_mode(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC Duo Mode On/Off.

        Args:
            value (int): Value for OSC Duo Mode (0 = OFF, 64 = ON).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 110, value)

    @mcp.tool()
    def set_kb_ctrl_lo_hi(value: int, channel: int = 3):  # type: ignore
        """
        Set the Keyboard Control LO/HI.

        Args:
            value (int): Value for Keyboard Control (0 = NEITHER, 32 = LO, 64 = HI).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 111, value)

    @mcp.tool()
    def set_osc1_level(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 Level.

        Args:
            value (int): Value for OSC 1 Level (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 114, value)

    @mcp.tool()
    def set_osc1_sub_level(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 1 Sub Level.

        Args:
            value (int): Value for OSC 1 Sub Level (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 115, value)

    @mcp.tool()
    def set_osc2_level(value: int, channel: int = 3):  # type: ignore
        """
        Set the OSC 2 Level.

        Args:
            value (int): Value for OSC 2 Level (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 116, value)

    @mcp.tool()
    def set_noise_level(value: int, channel: int = 3):  # type: ignore
        """
        Set the Noise Level.

        Args:
            value (int): Value for Noise Level (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 117, value)

    @mcp.tool()
    def set_feedback_ext_level(value: int, channel: int = 3):  # type: ignore
        """
        Set the Feedback/Ext Level.

        Args:
            value (int): Value for Feedback/Ext Level (0-127).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 118, value)
