# Moog Sub37 MCP

A Model Context Protocol (MCP) server that allows Claude and other MCP-compatible LLMs to interact with and control Moog Sub37 Monophonic Synthesizer via MIDI.

#### A web-based version of this MCP server can be found at [senthgenie.com](https://www.synthgenie.com/). (You can ask for API key for free on discord)

#### If you want help or would like to contribute to development, please join our [Discord community](https://discord.gg/ZFuSuegBMS).

# Prompt examples

```
"Use Sub37 MCP to design an evolving dark pad."
"Use Sub37 MCP to design a Dark thick bass line."
```

## Features

- [x] Complete MIDI control interface for the Moog Sub37 Monophonic Synthesizer

## Demo

Watch Claude control the Moog Sub37 Monophonic Synthesizer in real-time:

[![Claude controlling Moog Sub37](https://img.youtube.com/vi/EXf6lOTjla8/0.jpg)](https://www.youtube.com/watch?v=EXf6lOTjla8)

## Installation and Usage

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) for package management
- An Moog Sub37 Monophonic Synthesizer connected via USB
- Claude Desktop app (for full integration)

### Installing Dependencies

uv is mandatory for this project so start by installing it:

#### For macOS:

```bash
brew install uv
```

#### For Windows:

Follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/)

### 3. Installing with Claude Desktop

To use with Claude AI, add the MCP server configuration in Claude Desktop:

⚠️ **Important**: You don't need to clone the repository or install the packages, all you need is to add the MCP server configuration to your claude_desktop_config.json file the MPC server is already published on pypi.

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

- **Base Controllers**: Common functionality abstracted into base classes
- **Specialized Controllers**: Dedicated controllers for each synth engine and module
- **MCP Tools**: Direct interface between LLMs and the synth's parameters
- **MIDI Interface**: Reliable communication with Sub37 hardware

## Implementation Details

This library uses:

- **FastMCP**: For exposing synth controls to LLMs
- **Pydantic models**: For data validation, serialization, and type safety
- **mido**: For MIDI communication

## Use Cases

- Allow Claude and other LLMs to create and modify sounds on the Sub37
- Programmatically control Sub37 parameters for automated sound design
- Bridge between AI-generated music and hardware synthesis
