#!/usr/bin/env python3
"""
Simple component placement script for KiCad PCB files.
Sets component positions based on logical groupings.

Board: 210mm x 60mm
Layout strategy:
- Left side: Power input, regulator
- Center: ESP32-S3 module
- Right side: SSR, heater output
- Top edge: Thermocouple, pressure sensor
- Bottom edge: Status LEDs
"""

import re
from pathlib import Path

# Board dimensions (mm)
BOARD_W = 210
BOARD_H = 60

# Component positions (x, y, rotation) - origin at bottom-left
# Grouped by function
POSITIONS = {
    # Power section (left side)
    "regulator|LDO_3V3.ic|AMS1117_3V3": (25, 30, 0),
    "c_in|Capacitor.ic|_Capacitor": (15, 35, 0),
    "c_out|Capacitor.ic|_Capacitor": (35, 35, 0),

    # ESP32-S3 (center)
    "mcu|ESP32S3Module.ic|ESP32_S3_WROOM_1": (105, 30, 0),
    "mcu|ESP32S3Module.cap1|Capacitor.ic|_Capacitor": (85, 20, 0),
    "mcu|ESP32S3Module.cap2|Capacitor.ic|_Capacitor": (85, 25, 0),
    "mcu|ESP32S3Module.cap3|Capacitor.ic|_Capacitor": (85, 30, 0),

    # Thermocouple (top, near ESP32)
    "thermocouple|MAX31855Module.ic|MAX31855KASA": (140, 45, 0),
    "thermocouple|MAX31855Module.cap|Capacitor.ic|_Capacitor": (150, 45, 0),

    # SSR section (right side)
    "ssr|SSR_Driver.ssr|AQ10A2_SSR": (180, 30, 0),
    "ssr|SSR_Driver.q|BC817": (170, 25, 0),
    "ssr|SSR_Driver.r_base|_Resistor": (165, 20, 0),
    "ssr|SSR_Driver.r_ssr|_Resistor": (175, 40, 0),

    # Pressure sensor (top left)
    "r_div_top|Resistor.ic|_Resistor": (50, 50, 0),
    "r_div_bot|Resistor.ic|_Resistor": (50, 45, 0),
    "c_adc|Capacitor.ic|_Capacitor": (55, 47, 90),

    # LEDs (bottom edge)
    "led_ok|LED.resistor|_Resistor": (60, 10, 0),
    "led_ok|LED.led|_LED": (65, 10, 0),
    "led_heat|LED.resistor|_Resistor": (75, 10, 0),
    "led_heat|LED.led|_LED": (80, 10, 0),
    "led_err|LED.resistor|_Resistor": (90, 10, 0),
    "led_err|LED.led|_LED": (95, 10, 0),
}


def update_footprint_position(content: str, ref_pattern: str, x: float, y: float, rotation: float) -> str:
    """Update a footprint's position in the PCB content."""

    # Find footprint blocks and update position
    # KiCad PCB format: (footprint "..." (at X Y R) ...)

    # Pattern to match footprint with the reference
    fp_pattern = rf'(\(footprint\s+"[^"]+"\s+.*?\(property\s+"Reference"\s+"({ref_pattern})"\s+.*?\))'

    def replace_at(match):
        block = match.group(0)
        # Update the (at X Y) or (at X Y R) in the footprint
        at_pattern = r'\(at\s+[\d.-]+\s+[\d.-]+(?:\s+[\d.-]+)?\)'
        new_at = f"(at {x} {y} {rotation})"
        return re.sub(at_pattern, new_at, block, count=1)

    return re.sub(fp_pattern, replace_at, content, flags=re.DOTALL)


def main():
    pcb_path = Path(__file__).parent / "layouts/default/default.kicad_pcb"

    if not pcb_path.exists():
        print(f"PCB file not found: {pcb_path}")
        return

    content = pcb_path.read_text()

    # Extract all footprint references for debugging
    refs = re.findall(r'\(property\s+"Reference"\s+"([^"]+)"', content)
    print(f"Found {len(refs)} footprints:")
    for ref in sorted(set(refs)):
        print(f"  {ref}")

    # Apply positions
    # Note: atopile generates references like "mcu|ESP32S3Module.ic|ESP32_S3_WROOM_1"
    # We need to match these patterns

    updated = content
    for ref_pattern, (x, y, rot) in POSITIONS.items():
        # Escape special regex chars in the pattern
        escaped = re.escape(ref_pattern)
        updated = update_footprint_position(updated, escaped, x, y, rot)

    # Write back
    pcb_path.write_text(updated)
    print(f"\nUpdated positions in {pcb_path}")


if __name__ == "__main__":
    main()
