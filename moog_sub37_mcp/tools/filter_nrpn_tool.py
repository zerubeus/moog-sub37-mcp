"""
Filter NRPN tools for controlling filter parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_filter_nrpn_tools(mcp: FastMCP, midi: MIDIManager):  # noqa: C901
    """
    Register all Filter NRPN tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_filter_cutoff_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FILTER CUTOFF (NRPN 499, MSB 3, LSB 115).
        Args:
            value (int): Value for FILTER CUTOFF (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 115, value)

    @mcp.tool()
    def set_filter_resonance_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FILTER RESONANCE (NRPN 500, MSB 3, LSB 116).
        Args:
            value (int): Value for FILTER RESONANCE (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 116, value)

    @mcp.tool()
    def set_filter_drive_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FILTER DRIVE (NRPN 501, MSB 3, LSB 117).
        Args:
            value (int): Value for FILTER DRIVE (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 117, value)

    @mcp.tool()
    def set_filter_slope_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FILTER SLOPE (NRPN 502, MSB 3, LSB 118).
        Args:
            value (int): Value for FILTER SLOPE (0-3).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 118, value)

    @mcp.tool()
    def set_filter_eg_amt_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FILTER EG AMT (NRPN 503, MSB 3, LSB 119).
        Args:
            value (int): Value for FILTER EG AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 119, value)

    @mcp.tool()
    def set_filter_kb_amt_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the FILTER KB AMT (NRPN 504, MSB 3, LSB 120).
        Args:
            value (int): Value for FILTER KB AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 120, value)

    @mcp.tool()
    def set_f_eg_attack_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG ATTACK (NRPN 505, MSB 3, LSB 121).
        Args:
            value (int): Value for F EG ATTACK (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 121, value)

    @mcp.tool()
    def set_f_eg_decay_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG DECAY (NRPN 506, MSB 3, LSB 122).
        Args:
            value (int): Value for F EG DECAY (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 122, value)

    @mcp.tool()
    def set_f_eg_sustain_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG SUSTAIN (NRPN 507, MSB 3, LSB 123).
        Args:
            value (int): Value for F EG SUSTAIN (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 123, value)

    @mcp.tool()
    def set_f_eg_release_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG RELEASE (NRPN 508, MSB 3, LSB 124).
        Args:
            value (int): Value for F EG RELEASE (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 124, value)

    @mcp.tool()
    def set_f_eg_delay_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG DELAY (NRPN 509, MSB 3, LSB 125).
        Args:
            value (int): Value for F EG DELAY (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 125, value)

    @mcp.tool()
    def set_f_eg_hold_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG HOLD (NRPN 510, MSB 3, LSB 126).
        Args:
            value (int): Value for F EG HOLD (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 126, value)

    @mcp.tool()
    def set_f_eg_vel_amt_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG VEL AMT (NRPN 511, MSB 3, LSB 127).
        Args:
            value (int): Value for F EG VEL AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 127, value)

    @mcp.tool()
    def set_f_eg_kb_track_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG KB TRACK (NRPN 512, MSB 4, LSB 0).
        Args:
            value (int): Value for F EG KB TRACK (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 0, value)

    @mcp.tool()
    def set_f_eg_multi_trig_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG MULTI TRIG (NRPN 513, MSB 4, LSB 1).
        Args:
            value (int): Value for F EG MULTI TRIG (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 1, value)

    @mcp.tool()
    def set_f_eg_reset_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG RESET (NRPN 514, MSB 4, LSB 2).
        Args:
            value (int): Value for F EG RESET (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 2, value)

    @mcp.tool()
    def set_f_eg_sync_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG SYNC (NRPN 515, MSB 4, LSB 3).
        Args:
            value (int): Value for F EG SYNC (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 3, value)

    @mcp.tool()
    def set_f_eg_loop_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG LOOP (NRPN 516, MSB 4, LSB 4).
        Args:
            value (int): Value for F EG LOOP (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 4, value)

    @mcp.tool()
    def set_f_eg_latch_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG LATCH (NRPN 517, MSB 4, LSB 5).
        Args:
            value (int): Value for F EG LATCH (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 5, value)

    @mcp.tool()
    def set_f_eg_clk_div_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG CLK DIV (NRPN 518, MSB 4, LSB 6).
        Args:
            value (int): Value for F EG CLK DIV (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 6, value)

    @mcp.tool()
    def set_f_eg_attk_exp_nrpn(value: int, channel: int = 3):  # type: ignore
        """
        Set the F EG ATTK EXP (NRPN 520, MSB 4, LSB 8).
        Args:
            value (int): Value for F EG ATTK EXP (0-1).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 4, 8, value)
