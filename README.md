# ESP32 Espresso Machine Controller

An open-source PID temperature controller for espresso machines, featuring WiFi connectivity and precise temperature control.

## Project Structure

```
esp32-espresso/
├── pid-controller/     # PCB design (atopile)
│   ├── main.ato        # Main circuit definition
│   ├── components/     # Custom component definitions
│   └── build/          # Generated manufacturing files
└── pyproject.toml      # Python dependencies
```

## Hardware

The controller board is designed in [atopile](https://atopile.io) and manufactured via JLCPCB.

### Features

- **ESP32-S3** microcontroller with WiFi/BLE
- **On-board AC-DC converter** (100-240V AC → 5V DC) - direct mains power
- **USB Type-C** for programming/debugging (also provides backup power)
- **MAX31855** K-type thermocouple interface for precise temperature measurement
- **External SSR control** for heater switching (supports 25A panel-mount SSRs)
- **Pressure sensor input** with 5V→3.3V level shifting
- **Status LEDs** for system state indication

See [pid-controller/README.md](pid-controller/README.md) for detailed board documentation.

## Building the PCB

```bash
# Install dependencies
uv sync

# Build the PCB
cd pid-controller
ato build
```

Manufacturing files will be generated in `pid-controller/build/default/`.

## License

See individual component licenses in their respective directories.
