# PID Controller BOM - Rancilio Silvia

## ICs

| Qty | Ref | Component | Value | Package | LCSC | DigiKey |
|-----|-----|-----------|-------|---------|------|---------|
| 1 | U1 | ESP32-S3-WROOM-1-N8 | - | Module | C2913198 | |
| 1 | U2 | MAX31855KASA+T | K-type TC | SOIC-8 | C52028 | |
| 1 | U3 | AMS1117-3.3 | 3.3V LDO | SOT-223 | C6186 | |

## Discrete Semiconductors

| Qty | Ref | Component | Value | Package | LCSC | DigiKey |
|-----|-----|-----------|-------|---------|------|---------|
| 1 | U4 | AQ10A2-ZT4/32VDC | 10A SSR | SIP-4 | C6507016 | https://www.digikey.com/en/products/detail/panasonic-electric-works/AQ10A2-ZT4-32VDC/3992067 |
| 1 | Q1 | BC817-40 | NPN | SOT-23 | C8589 | |

## Resistors (0603)

| Qty | Ref | Component | Value | Package | LCSC | DigiKey |
|-----|-----|-----------|-------|---------|------|---------|
| 1 | R1 | R_base | 1k | 0603 | | |
| 1 | R2 | R_ssr | 100 ohm | 0603 | | |
| 1 | R3 | R_div_top | 10k | 0603 | | |
| 1 | R4 | R_div_bot | 15k | 0603 | | |
| 3 | R5-R7 | R_led | 200 ohm | 0603 | | |

## Capacitors (0603)

| Qty | Ref | Component | Value | Package | LCSC | DigiKey |
|-----|-----|-----------|-------|---------|------|---------|
| 2 | C1-C2 | C_in, C_out | 10uF | 0603 | | |
| 4 | C3-C6 | C_bypass (ESP32) | 100nF | 0603 | | |
| 1 | C7 | C_bypass (MAX31855) | 100nF | 0603 | | |
| 1 | C8 | C_adc | 100nF | 0603 | | |

## LEDs (0603)

| Qty | Ref | Component | Color | Package | LCSC | DigiKey |
|-----|-----|-----------|-------|---------|------|---------|
| 1 | D1 | LED_OK | Green | 0603 | | |
| 1 | D2 | LED_Heat | Orange | 0603 | | |
| 1 | D3 | LED_Err | Red | 0603 | | |

## Connectors

| Qty | Ref | Component | Description | Package | LCSC | DigiKey |
|-----|-----|-----------|-------------|---------|------|---------|
| 1 | J1 | J_power | 5V Power input | Phoenix 2-pos | | |
| 1 | J2 | J_tc | Thermocouple input | Phoenix 2-pos | | |
| 1 | J3 | J_heater | AC heater output | Phoenix 2-pos | | |
| 1 | J4 | J_pressure | Pressure sensor | Phoenix 3-pos | | |

---

## Notes

- **SSR Cooling**: Dissipates ~7-10W at full load (8.3A). Requires heatsink or chassis mounting with thermal pad.
- **Voltage Divider**: Scales 5V pressure sensor output to 3.3V ADC range (10k/15k = 3.0V max).
- **LEDs**: Active-low (cathode to GPIO). 200 ohm for ~5mA at 3.3V.
- **LCSC IDs**: For JLCPCB assembly. SSR (C6507016) may be out of stock - order from DigiKey.

## Assembly Options

1. **JLCPCB SMT**: Use LCSC IDs for automated assembly (excludes SSR, connectors)
2. **DigiKey + Reflow**: Order all from DigiKey, reflow at home
3. **Hybrid**: JLCPCB for SMD, hand-solder SSR and connectors
