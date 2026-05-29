---
name: ruview
description: "WiFi spatial intelligence — presence detection, vital signs, and spatial mapping from WiFi signals"
tags: [wifi, spatial-intelligence, presence-detection, smart-home, rust]
related_skills: [openhue]
---

# RuView — WiFi Spatial Intelligence

> Turn commodity WiFi into spatial intelligence. No cameras, no wearables, no dedicated sensors.

## Prerequisites

- Linux with WiFi adapter supporting monitor mode
- Rust toolchain
- WiFi router (any modern router works)

## Installation

```bash
git clone https://github.com/ruvnet/RuView.git
cd RuView
cargo build --release
```

## Usage

### Basic presence detection
```bash
./target/release/ruview --interface wlan0 --mode presence
# Output: {"room": "living_room", "occupied": true, "confidence": 0.94}
```

### Movement tracking
```bash
./target/release/ruview --interface wlan0 --mode tracking
# Output: {"path": [{"x": 1.2, "y": 3.4, "time": "..."}, ...]}
```

### Vital sign monitoring
```bash
./target/release/ruview --interface wlan0 --mode vital
# Output: {"heart_rate": 72, "breathing_rate": 16, "movement": "still"}
```

### MCP Server (for AI agent integration)
```bash
./target/release/ruview serve --port 8090
# Add to agent config:
# "mcpServers": {"ruview": {"command": "ruview", "args": ["serve", "--port", "8090"]}}
```

## Modes

| Mode | Use Case | Output |
|------|----------|--------|
| `presence` | Room occupancy detection | Boolean + confidence |
| `tracking` | Movement path following | Coordinate array |
| `vital` | Heart rate, breathing | Numeric values |
| `spatial` | Full 3D room mapping | Point cloud |

## Pitfalls

1. **WiFi adapter**: Must support monitor mode. Check with `iw list` before buying hardware.
2. **Calibration**: First-time setup needs 5-minute calibration walk-through of the space.
3. **Walls**: Thick concrete walls reduce signal penetration. May need multiple access points.
4. **Privacy**: Despite no cameras, spatial data is sensitive. Secure the MCP server endpoint.
5. **Interference**: Microwave ovens and other 2.4GHz devices cause noise. Use 5GHz when possible.

## Verification

```bash
# Test presence detection
./target/release/ruview --interface wlan0 --mode presence --duration 30
# Should output presence readings every second for 30 seconds

# Verify MCP server
curl http://localhost:8090/health
```
