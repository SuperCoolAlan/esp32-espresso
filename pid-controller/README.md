# ESP32-S3 PID Controller for Espresso Machine

A PID temperature controller board designed for the Rancilio Silvia espresso machine, built with [atopile](https://atopile.io).

## Board Overview

This board provides closed-loop temperature control for an espresso machine boiler using a K-type thermocouple and an external solid-state relay.

### Major Components

| Component | Part Number | Description |
|-----------|-------------|-------------|
| MCU | ESP32-S3-WROOM-1-N8 | WiFi/BLE module, 8MB flash |
| AC-DC Converter | HLK-PM01 | 100-240V AC → 5V DC @ 600mA (3W) |
| Thermocouple IC | MAX31855KASA | K-type thermocouple-to-digital converter |
| Voltage Regulator | AMS1117-3.3 | 3.3V LDO (from 5V) |
| SSR Driver | BC817-40 | NPN transistor for external SSR control |
| Power Diode | SS14 | Schottky diode for USB/AC power OR-ing |

### Connectors / Terminals

| Connector | Pins | Function |
|-----------|------|----------|
| J_AC | 2 | AC mains input (Line, Neutral) |
| J_USB | USB-C | Programming/debugging + backup 5V power |
| J_TC | 2 | K-type thermocouple input (TC+, TC-) |
| J_SSR | 2 | External SSR control output (SSR+, SSR-) |
| J_PRESSURE | 3 | Pressure sensor input (+5V, Signal, GND) |

### Status LEDs

| LED | Color | Function |
|-----|-------|----------|
| LED_OK | Green | System running / OK |
| LED_HEAT | Orange | Heating element active |
| LED_ERR | Red | Error condition |

All LEDs are active-low (accent driven by GPIO sinking current).

## Pin Assignments

### ESP32-S3 GPIO Usage

| GPIO | Function |
|------|----------|
| IO1 | Pressure sensor ADC input |
| IO4 | SSR control output |
| IO5 | Green LED (OK) |
| IO6 | Orange LED (Heating) |
| IO7 | Red LED (Error) |
| IO10 | SPI CS (MAX31855) |
| IO11 | SPI MOSI (unused) |
| IO12 | SPI CLK (MAX31855) |
| IO13 | SPI MISO (MAX31855) |
| IO19 | USB D- |
| IO20 | USB D+ |

## External SSR Wiring

This board outputs a control signal for an external panel-mount SSR (e.g., Fotek SSR-25DA or similar 25A SSR). The external SSR provides better heat dissipation for high-power loads.

```
Board J_SSR          External SSR (25A)         Heater
┌─────────┐          ┌─────────────┐           ┌──────┐
│ Pin 1 ──┼──────────┤ Input +     │           │      │
│ (SSR+)  │          │ (3-32VDC)   │           │      │
│         │          │             ├───────────┤ Load │
│ Pin 2 ──┼──────────┤ Input -     │    AC     │      │
│ (SSR-)  │          │             ├───────────┤      │
└─────────┘          └─────────────┘           └──────┘
```

## Circuit Features

- **AC-DC Power**: On-board HLK-PM01 isolated converter (100-240V AC → 5V DC)
- **USB Type-C**: For programming/debugging, with Schottky diode power OR-ing
- **Dual Power Sources**: USB power works when AC is disconnected (for bench programming)
- **Boot Circuit**: 10k pullup + 1µF RC delay on EN pin for reliable power-on reset
- **Boot Mode**: 10k pullup on GPIO0 for normal SPI flash boot
- **Decoupling**: 100nF + 10µF on 3.3V rail, 10µF + 22µF on LDO
- **Pressure Sensor**: 10k/20k voltage divider (5V → 3.3V) with 100nF filter cap

## Building

Requires [atopile](https://atopile.io) v0.12.4 or later.

```bash
cd pid-controller
ato build
```

Build outputs are placed in `build/default/`.

## BOM / Ordering

All components are available from JLCPCB/LCSC. Run `ato build` to generate the BOM and manufacturing files.

## License

See [LICENSE.txt](LICENSE.txt)
