"""
LFO tools for controlling LFO parameters on the Digitone.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_lfo_tools(mcp: FastMCP, midi: MIDIManager):  # noqa: C901
    """
    Register all LFO tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_clock_divider_4_whole_notes(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for 4 whole notes.

        Args:
            value (int): The clock divider value (0-6, default 6).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_3_whole_notes(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for 3 whole notes.

        Args:
            value (int): The clock divider value (7-12, default 10).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_2_whole_notes(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for 2 whole notes.

        Args:
            value (int): The clock divider value (13-18, default 16).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_whole_note_half(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for whole note and a half.

        Args:
            value (int): The clock divider value (19-24, default 22).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_whole_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for whole note.

        Args:
            value (int): The clock divider value (25-40, default 32).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_dotted_half_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for dotted half note.

        Args:
            value (int): The clock divider value (31-36, default 34).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_whole_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for whole note triplet.

        Args:
            value (int): The clock divider value (37-42, default 40).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_half_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for half note.

        Args:
            value (int): The clock divider value (43-48, default 46).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_dotted_quarter_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for dotted quarter note triplet.

        Args:
            value (int): The clock divider value (49-54, default 52).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_half_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for half note triplet.

        Args:
            value (int): The clock divider value (55-60, default 58).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_quarter_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for quarter note.

        Args:
            value (int): The clock divider value (61-67, default 64).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_dotted_eighth_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for dotted eighth note.

        Args:
            value (int): The clock divider value (68-73, default 70).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_quarter_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for quarter note triplet.

        Args:
            value (int): The clock divider value (74-79, default 76).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_eighth_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for eighth note.

        Args:
            value (int): The clock divider value (80-85, default 82).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_dotted_sixteenth_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for dotted sixteenth note.

        Args:
            value (int): The clock divider value (86-91, default 88).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_eighth_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for eighth note triplet.

        Args:
            value (int): The clock divider value (92-97, default 94).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_sixteenth_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for sixteenth note.

        Args:
            value (int): The clock divider value (98-103, default 100).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_sixteenth_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for sixteenth note triplet.

        Args:
            value (int): The clock divider value (104-109, default 106).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_thirtysecond_note(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for thirty-second note.

        Args:
            value (int): The clock divider value (110-115, default 112).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_thirtysecond_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for thirty-second note triplet.

        Args:
            value (int): The clock divider value (116-121, default 118).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_clock_divider_sixtyfourth_note_triplet(value: int, channel: int = 3):  # type: ignore
        """
        Set the clock divider for sixty-fourth note triplet.

        Args:
            value (int): The clock divider value (122-127, default 124).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 3, value)

    @mcp.tool()
    def set_lfo_rate(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO rate with high resolution.

        Args:
            value (int): High-resolution value for LFO rate (0-16383, default 9984).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 3, 34, value)

    @mcp.tool()
    def set_mod1_pitch_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 Pitch Amount with high resolution.

        Args:
            value (int): High-resolution value for MOD 1 Pitch Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 4, 36, value)

    @mcp.tool()
    def set_mod1_filter_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 Filter Amount with high resolution.

        Args:
            value (int): High-resolution value for MOD 1 Filter Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 11, 43, value)

    @mcp.tool()
    def set_mod1_pgm_dest_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 Programmable Destination Amount with high resolution.

        Args:
            value (int): High-resolution value for MOD 1 Programmable Destination Amount (0-16383).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_high_res_cc(channel, 20, 52, value)

    @mcp.tool()
    def set_mod1_osc_1_2_sel(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 Oscillator 1/2 Selection.

        Args:
            value (int): Value for oscillator selection (0 = OSC1 + OSC2, 43 = OSC1, 85 = OSC2).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 70, value)

    @mcp.tool()
    def set_mod1_source(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 Source selection.

        Args:
            value (int): Value for source selection (0 = TRIANGLE LFO, 21 = SQUARE LFO, 43 = SAW LFO, 64 = RAMP LFO, 85 = S&H LFO, 107 = F.EG/PGM).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 71, value)

    @mcp.tool()
    def set_lfo1_range(value: int, channel: int = 3):  # type: ignore
        """
        Set the LFO 1 Range selection.

        Args:
            value (int): Value for range selection (0 = Low Range, 43 = Med Range, 85 = Hi Range).
            channel (int): MIDI channel (default is 3 if not specified).
        """
        midi.send_cc(channel, 76, value)
