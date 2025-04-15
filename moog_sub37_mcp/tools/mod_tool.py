"""
MOD tools for controlling modulation parameters on the Moog Sub 37.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager


def register_mod_tools(mcp: FastMCP, midi: MIDIManager):  # noqa: C901
    """
    Register all MOD tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_mod1_mwhl_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 MWHL AMT (NRPN 435, MSB 3, LSB 51).
        Args:
            value (int): Value for MOD 1 MWHL AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 51, value)

    @mcp.tool()
    def set_mod1_velocity_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 VELOCITY AMT (NRPN 436, MSB 3, LSB 52).
        Args:
            value (int): Value for MOD 1 VELOCITY AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 52, value)

    @mcp.tool()
    def set_mod1_pressure_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 PRESSURE AMT (NRPN 437, MSB 3, LSB 53).
        Args:
            value (int): Value for MOD 1 PRESSURE AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 53, value)

    @mcp.tool()
    def set_mod1_ctl4_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 CTL4 AMT (NRPN 438, MSB 3, LSB 54).
        Args:
            value (int): Value for MOD 1 CTL4 AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 54, value)

    @mcp.tool()
    def set_mod1_source(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 SOURCE (NRPN 440, MSB 3, LSB 56).
        Args:
            value (int): Value for MOD 1 SOURCE (0-5).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 56, value)

    @mcp.tool()
    def set_mod1_pgm_src(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 PGM SRC (NRPN 441, MSB 3, LSB 57).
        Args:
            value (int): Value for MOD 1 PGM SRC (0-7).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 57, value)

    @mcp.tool()
    def set_mod1_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 DEST (NRPN 442, MSB 3, LSB 58).
        Args:
            value (int): Value for MOD 1 DEST (0-6).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 58, value)

    @mcp.tool()
    def set_mod1_pgm_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 PGM DEST (NRPN 443, MSB 3, LSB 59).
        Args:
            value (int): Value for MOD 1 PGM DEST (0-88).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 59, value)

    @mcp.tool()
    def set_mod1_pgm_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 PGM AMT (NRPN 444, MSB 3, LSB 60).
        Args:
            value (int): Value for MOD 1 PGM AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 60, value)

    @mcp.tool()
    def set_mod1_pitch_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 PITCH AMT (NRPN 445, MSB 3, LSB 61).
        Args:
            value (int): Value for MOD 1 PITCH AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 61, value)

    @mcp.tool()
    def set_mod1_filter_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 FILTER AMT (NRPN 446, MSB 3, LSB 62).
        Args:
            value (int): Value for MOD 1 FILTER AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 62, value)

    @mcp.tool()
    def set_mod1_pitch_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 1 PITCH DEST (NRPN 447, MSB 3, LSB 63).
        Args:
            value (int): Value for MOD 1 PITCH DEST (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 63, value)

    @mcp.tool()
    def set_mod2_mwhl_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 MWHL AMT (NRPN 460, MSB 3, LSB 76).
        Args:
            value (int): Value for MOD 2 MWHL AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 76, value)

    @mcp.tool()
    def set_mod2_velocity_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 VELOCITY AMT (NRPN 461, MSB 3, LSB 77).
        Args:
            value (int): Value for MOD 2 VELOCITY AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 77, value)

    @mcp.tool()
    def set_mod2_pressure_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 PRESSURE AMT (NRPN 462, MSB 3, LSB 78).
        Args:
            value (int): Value for MOD 2 PRESSURE AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 78, value)

    @mcp.tool()
    def set_mod2_ctl4_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 CTL4 AMT (NRPN 463, MSB 3, LSB 79).
        Args:
            value (int): Value for MOD 2 CTL4 AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 79, value)

    @mcp.tool()
    def set_mod2_source(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 SOURCE (NRPN 465, MSB 3, LSB 81).
        Args:
            value (int): Value for MOD 2 SOURCE (0-5).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 81, value)

    @mcp.tool()
    def set_mod2_pgm_src(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 PGM SRC (NRPN 466, MSB 3, LSB 82).
        Args:
            value (int): Value for MOD 2 PGM SRC (0-7).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 82, value)

    @mcp.tool()
    def set_mod2_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 DEST (NRPN 467, MSB 3, LSB 83).
        Args:
            value (int): Value for MOD 2 DEST (0-6).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 83, value)

    @mcp.tool()
    def set_mod2_pgm_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 PGM DEST (NRPN 468, MSB 3, LSB 84).
        Args:
            value (int): Value for MOD 2 PGM DEST (0-88).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 84, value)

    @mcp.tool()
    def set_mod2_pgm_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 PGM AMT (NRPN 469, MSB 3, LSB 85).
        Args:
            value (int): Value for MOD 2 PGM AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 85, value)

    @mcp.tool()
    def set_mod2_pitch_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 PITCH AMT (NRPN 470, MSB 3, LSB 86).
        Args:
            value (int): Value for MOD 2 PITCH AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 86, value)

    @mcp.tool()
    def set_mod2_filter_amt(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 FILTER AMT (NRPN 471, MSB 3, LSB 87).
        Args:
            value (int): Value for MOD 2 FILTER AMT (0-16383).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 87, value)

    @mcp.tool()
    def set_mod2_pitch_dest(value: int, channel: int = 3):  # type: ignore
        """
        Set the MOD 2 PITCH DEST (NRPN 472, MSB 3, LSB 88).
        Args:
            value (int): Value for MOD 2 PITCH DEST (0-2).
            channel (int): MIDI channel (default is 3).
        """
        midi.send_nrpn(channel, 3, 88, value)
