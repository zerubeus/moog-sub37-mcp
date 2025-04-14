"""
MCP server configuration and initialization.
"""

from mcp.server.fastmcp import FastMCP

from moog_sub37_mcp.midi.midi_manager import MIDIManager
from moog_sub37_mcp.tools.amp_tool import register_amp_tools
from moog_sub37_mcp.tools.filter_tool import register_filter_tools
from moog_sub37_mcp.tools.fx_tool import register_fx_tools
from moog_sub37_mcp.tools.lfo_tool import register_lfo_tools
from moog_sub37_mcp.tools.wavetone_tool import register_wavetone_tools

# Initialize MCP and MIDI
mcp = FastMCP('Moog Sub 37')
midi = MIDIManager('Moog Sub 37')

# Register all tools
register_wavetone_tools(mcp, midi)
register_filter_tools(mcp, midi)
register_amp_tools(mcp, midi)
register_fx_tools(mcp, midi)
register_lfo_tools(mcp, midi)

# Export the configured MCP server
__all__ = ['mcp']
