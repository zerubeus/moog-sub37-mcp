# Moog Sub37 MCP

A Model Context Protocol (MCP) server that allows Claude and other MCP-compatible LLMs to interact with and control the Moog Sub37/Subsequent37 analog synthesizer via MIDI. This integration enables AI-assisted sound design and parameter control of this legendary Moog synthesizer.

## About the Moog Sub37/Subsequent37

The Moog Sub37/Subsequent37 is a powerful analog synthesizer featuring:

- 2 oscillators with sub oscillators
- Classic Moog ladder filter
- Dual LFOs
- Extensive modulation options
- 256 preset memory
- 37-key keyboard with velocity and aftertouch
- Mono and Duo (paraphonic) modes
- Built-in arpeggiator and step sequencer

# Prompt Examples

```
"Design a deep, resonant bass patch using the Moog filter's self-oscillation"
"Create an evolving pad sound using both oscillators in Duo mode"
"Program a sequence that showcases the Sub37's classic Moog lead sound"
"Design a dark atmospheric sound using the Sub37's modulation capabilities"
"Create a punchy bass sound perfect for techno using the multidrive circuit"
```

## Features

- [x] Complete MIDI control interface for all Sub37/Subsequent37 parameters
- [x] Support for both Sub37 and Subsequent37 models
- [x] Access to all synthesis parameters:
  - Oscillator controls (waveform, pitch, sync)
  - Filter controls (cutoff, resonance, envelope amount)
  - Envelope generators
  - LFO settings
  - Modulation routing
  - Arpeggiator/Sequencer parameters
- [x] Preset management
- [x] Real-time parameter automation

## Demo

Watch Claude control the Moog Sub37/Subsequent37 in real-time:

[![Claude controlling Moog Sub37](https://img.youtube.com/vi/EXf6lOTjla8/0.jpg)](https://www.youtube.com/watch?v=EXf6lOTjla8)

## Installation and Usage

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for package management
- A Moog Sub37 or Subsequent37 synthesizer connected via USB
- Claude Desktop app (for full integration)

### Installing Dependencies

uv is mandatory for this project. Start by installing it:

#### For macOS:

```bash
brew install uv
```

#### For Windows:

Follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/)

### Installing with Claude Desktop

To use with Claude AI, add the MCP server configuration in Claude Desktop:

⚠️ **Important**: You don't need to clone the repository or install the packages manually. The MCP server is published on PyPI and can be installed automatically.

Go to Claude > Settings > Developer > Edit Config > claude_desktop_config.json to include the following:

```json
{
  "mcpServers": {
    "Sub37": {
      "command": "uvx",
      "args": ["moog-sub37-mcp"]
    }
  }
}
```

## Architecture

The MCP server is designed to provide comprehensive control over the Sub37/Subsequent37:

- **Parameter Control**: Direct access to all synthesizer parameters via MIDI CC messages
- **Preset Management**: Load, save, and modify presets
- **Real-time Control**: Immediate response to parameter changes
- **MIDI Implementation**: Complete MIDI specification support
- **Error Handling**: Robust error handling for MIDI communication

## Implementation Details

This library leverages:

- **FastMCP**: For exposing synth controls to LLMs
- **Pydantic Models**: For parameter validation and type safety
- **mido**: For reliable MIDI communication with the synthesizer
- **Dynamic Versioning**: Automatic version management for releases

## Use Cases

- **AI-Assisted Sound Design**: Let Claude help you create new sounds and explore the synth's capabilities
- **Automated Parameter Control**: Program complex parameter changes for evolving sounds
- **Preset Management**: Organize and modify your preset library
- **Live Performance**: Control the synth in real-time with AI assistance
- **Educational Tool**: Learn about synthesis through interactive AI guidance

## Community and Support

- Join our [Discord community](https://discord.gg/ZFuSuegBMS) for help and discussion
- Visit [synthgenie.com](https://www.synthgenie.com/) for the web-based version (API key available for free on Discord)
- Report issues and contribute on GitHub

## License

MIT License - See LICENSE file for details
