# Pattern: WiFi/RF Sensing

> Turn existing wireless infrastructure into sensing systems.

## Problem
Spatial intelligence (presence detection, vital signs, movement tracking) traditionally requires cameras, wearables, or dedicated sensors. Cameras raise privacy concerns, wearables require compliance, and dedicated sensors are expensive to deploy at scale.

## Solution
Use Channel State Information (CSI) from commodity WiFi routers to extract spatial data:
1. **CSI capture** via ESP32 sensors or Intel/Atheros NICs
2. **Signal processing** to extract reflection patterns
3. **Machine learning** to classify presence, movement, vital signs
4. **MCP/REST API** for integration with AI agents and smart home systems

The key insight: WiFi signals already bounce off everything in a room. By analyzing the reflection patterns, you can infer what's happening without any cameras or sensors — just the WiFi router you already have.

## When to Use
- Smart home presence detection without cameras
- Elderly care monitoring (non-invasive vital signs)
- Security systems in privacy-sensitive areas
- Retail analytics without video surveillance
- Research environments needing spatial data

## When NOT to Use
- When high-precision visual identification is needed
- When WiFi coverage is sparse or unreliable
- When environments have extreme multipath interference
- When the cost of ESP32 hardware is prohibitive at scale

## Discovered From
- **RuView** — 67K stars, WiFi spatial intelligence in Rust
  - Supports 802.11n/ac/ax (WiFi 4/5/6)
  - 17-keypoint pose estimation (beta)
  - Home Assistant, Apple Home, Google Home integration
  - Hardware: ESP32-S3 (~$140) or zero-cost (laptop WiFi)

## Variants
- **RSSI-Only**: Coarse presence from signal strength (zero-cost, low accuracy)
- **CSI-Based**: Fine-grained sensing from channel state (ESP32, high accuracy)
- **MIMO Multi-Ap**: Multiple access points for 3D spatial mapping
- **Through-Wall**: Penetrates walls up to ~5m (security/eldercare applications)

## Metrics
- RuView: 67K stars, 8.9K forks, 26 contributors
- Growing 4,690 stars/week (hottest OSS project in May 2026)
- ~$140 hardware cost for full sensing capability
- Supports 3-5 people per access point (scales linearly with multi-AP)
