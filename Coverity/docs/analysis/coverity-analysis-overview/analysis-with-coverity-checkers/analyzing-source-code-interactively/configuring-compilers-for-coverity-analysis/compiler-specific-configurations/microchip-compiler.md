---
title: "Microchip compiler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/microchip-compiler.html"
content_id: "BEbmTOa9ObDhbmEGqL1rZw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:44.969884+00:00"
---

# Microchip compiler

The following Microchip MPLAB compilers are supported:

- For 8-bit devices, use compile name `xc8` and compile type
  `microchip:xc8`, or compile name `xc8-cc` and
  compile type `microchip:xc8cc`

  Note: Before version 2.00, the XC8 C
  compiler supports only PIC MCUs, and the documented driver name is
  `xc8`. Starting with version 2.00, the XC8 C compiler
  supports both PIC and AVR MCUs, and the documented driver name is
  `xc8-cc`.
- For 16-bit devices, use compile name `xc16-gcc` and compile type
  `microchip:xc16`
- For 32-bit devices, use compile name `xc32-gcc` and compile type
  `microchipcc:xc32`

Use a template configuration
for the Microchip Compilers:

```
cov-configure --template --compiler xc8 --comptype microchip:xc8
cov-configure --template --compiler xc8-cc --comptype microchip:xc8cc
cov-configure --template --compiler xc16-gcc --comptype microchip:xc16
cov-configure --template --compiler xc32-gcc --comptype microchipcc:xc32
```
