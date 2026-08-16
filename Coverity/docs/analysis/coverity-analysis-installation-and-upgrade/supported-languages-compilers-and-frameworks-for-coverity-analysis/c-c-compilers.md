---
title: "C/C++ compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-compilers.html"
content_id: "qt2lMUSObdnB1FsoxZKFaQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:01.961552+00:00"
---

# C/C++ compilers

Coverity provides, and supports the Compiler Integration Toolkit (CIT) (CIT). This
toolkit is used to integrate compilers with Coverity Analysis for C/C++. Coverity
acknowledges that not all compilers can be integrated using CIT. Coverity provides
compiler integrations out of the box for many popular compilers (listed below).

Coverity provides commercially reasonable efforts to support documented compiler features
driven by market need. Coverity does not generally support undocumented or unintended
language features. To properly analyze files that use undocumented, unintended, or
non-standard features, customers might need to customize their configuration or change
their code.

Non-CIT issues with compilers that have not been integrated by Coverity will be handled
on a case by case basis but are generally considered "unsupported". Since Coverity will
not be able to validate these issues, we will require very detailed and precise problem
reports to begin the investigation.

Unless otherwise specified, Coverity does not support new or changed language features
specified in any of the following:

- Unpublished C and C++ language standards.
- C and C++ technical reports (TRs) or technical specifications (TSs). Examples of such
  specifications include ISO/IEC TR 18037 (Programming languages—C—Extensions to
  support embedded processors), ISO/IEC TS 19217:2015 (Information
  technology—Programming languages—C++ Extensions for concepts), and ISO/IEC TS
  21544:2018 (Programming languages—Extensions to C++ for modules).

Coverity provides support for the C++20 standard (ISO/IEC 14882:2020) except where
otherwise specified. In particular, modules-related constructs (export declarations,
import declarations, module declarations, etc.) are not supported.

Coverity provides the following compiler integrations:

Table 1. Coverity Analysis for C/C++ compiler integrations

| Compiler | Version | Host OS | Target | Notes |
| --- | --- | --- | --- | --- |
| Analog Devices Compilers | 8.12.0.0 | Windows | Blackfin | ISO/IEC TR 18037 fixed point extensions are supported for C (not C++) code on Blackfin and SHARC. |
| 8.0.0.8-8.12.0.0 | SHARC |
| 7.3.0.5 | TigerSHARC |
| ARM C and C++ | 5.0-6.13.1 | Windows/Linux | ARM |  |
| 6.14.1 | Linux |
| ARM Embedded FuSa | 6.16.2-6.22.2 | Linux | ARM |  |
| CEVA compilers | 17.0 | Linux | CEVA-X |  |
| b753 | Windows | CEVA-TL4CC |
| b480 | CEVA-XC12 |
| 10.3-16.1 | CEVA-XC321, CEVA-XC323, CEVA-XC4210, CEVA-XC4500 |
| SDT 18.0.6-18.1 | CEVA-BX1, CEVA-BX2 |
| SDT V18.0.2 | CEVA-X1, CEVA-X2 |
| b453 | Windows/Linux | CEVA-XM4 |
| SDT V20.1.0 | CEVA-XC16 |
| Clang | Android NDK Clang 9.0.9-18.0.1 (NDK revisions r22b-r27a) | Windows, Linux, macOS | ARM, x86, x86_64 | Clang compilers have various use limitations with Coverity products, which are listed in the *Coverity Analysis User and Administrator Guide*.  Coverity Analysis supports the MISRA C:2004 and MISRA C:2012 compliance standards for Clang compilers.  MISRA C 2004 Rule 1:1, MISRA C 2012 Rule 1.1, MISRA C 2023 Rule 1.1 and MISRA C++ 2023 Rule 4.1.1 ensures that the analyzed program is compliant with the C / C++ standard. The Clang compiler uses different parse warnings and error messages than `cov-emit` uses. You might encounter minor discrepancies between the enforcement of MISRA rule by the Clang compiler and `cov-emit`.  LLVM Clang on 32 bit Linux is not supported.  macOS on Intel: To ensure a complete capture, version 12-26 of Xcode (with command line tools) must be installed. Also, ensure that `xcodebuild -version` runs without error; Coverity uses this command to check the Xcode version.  macOS on Apple silicon: Build capture requires both Rosetta 2 and Xcode (*with command line tools*) 12-26 in order to function. Please ensure `xcodebuild -version` runs without error.  macOS on Apple silicon: Support on macOS on Apple silicon is limited to LLVM Clang versions 14.0-22.1.0.  Deprecation Notice: Support for Xcode 12.x-14.x is deprecated as of 2025.12. |
| LLVM Clang 10.0-22.1.0 | Windows, Linux, macOS, FreeBSD | ARM, ARM64 (Linux only), MIPS, x86, x86_64 |
| Rynda Clang |
| clang-cl | 10.0-22.1.0 | Windows | x86_64 |  |
| Cosmic C Cross Compilers | cx6808 4.5.10-4.6.3 | Windows | Freescale 68HC08 and HCS08 |  |
| cx6812 4.6i | Freescale 68HC12 and HCS12 |
| cxs12x 4.7.7-4.8.9 | Freescale HCS12X |
| cx332 4.1l | Freescale MC68332 |
| cxs12z 4.3.4 | Freescale S12Z |
| cxstm8 4.3.7 | STM8 and STLUX family |
| cxxgate 4.2.4 | Freescale XGATE co-processor |
| cx6805 4.2d | Motorola 68HC05 |
| cx6811 4.1t | Motorola 68HC11 |
| cx6816 4.1r | Motorola 68HC16 |
| CrossWorks | 3.1.1 | Windows | MSP430 |  |
| 4.0.1 | ARM | ISO/IEC TR 18037 fixed point extensions are supported for C (not C++) code on ARM. |
| Embarcadero (formerly Borland) C++ | 7.60 | Windows | x86, x86_64 | Support for Embarcadero C++ 7.60 is limited to `bcc32` (Classic Borland C++ compiler), `bcc32x` (Clang-enhanced C++ compiler for 32-bit Windows), and `bcc64` (Clang-enhanced C++ compiler for 64-bit Windows). The `bcc32c` binary is not supported. |
| Freescale CodeWarrior | 10.9 | Windows | StarCore | CodeWarrior compilers are supported only for command-line builds. Coverity Analysis does not support the CodeWarrior IDE. |
| 11.2 | dsp56800e |
| GNU GCC and G++ | GNU gcc and g++ versions 4.8.0-15.2 | FreeBSD, Linux, Linux ARM64, macOS on Intel, Solaris, Windows | ARM, Itanium, MIPS, PowerPC, SPARC, x86, x86_64 | ISO/IEC TR 18037 fixed point extensions are supported for C (not C++) code.  GNU GCC compilers distributed with Apple Xcode are not supported.  Versions of any of these compilers that are modified to accept non-standard syntax are not supported.  Linux ARM64: Support on Linux ARM64 is limited to GCC versions 9.1-15.2. |
| Green Hills Optimizing C and C++/EC++ | 4.2.3 | Solaris | MPC83xx, PowerQUICC II PRO |  |
| 2015.1.4-2021.1.4 | Windows | ARM |
| 2015.1-2018.5.5 | V850 |
| 2019.5.5 | RH850 |
| 2012.1 | 68K/ColdFire |
| 2020.1.4 | PowerPC |
| 2018.1.5-2021.1.5 | TriCore |
| 2015.1.4-2018.1.4 | Linux | ARM |
| HighTec compiler | 4.9.3.0 | Windows | Tricore |  |
| 4.9.4.1 | Windows/Linux |
| IAR Embedded Workbench C/C++ | 6.30-9.70 | Windows | ARM |  |
| 8.50-9.10 | Linux |
| 4.30-6.10 | Windows | Atmel AVR |
| 4.1 | Atmel AVR32 |
| 1.13C-2.30 | Dallas/Maxim MAXQ |
| 4.10A-5.30 | MSP430 |
| 4.81 | Renesas 78K |
| 1.3 | Renesas RH850 |
| 2.10B-2.30 | Renesas H8 |
| 2.21 | Renesas RL78 |
| 2.3 | Renesas SuperH |
| 3.21D-3.50 | Renesas M16C |
| 3.21A-3.30 | Renesas M32C |
| 3.5 | Renesas R8C |
| 1.4 | Renesas R32C |
| 4.1 | Renesas V850 |
| 4.12-5.20.1 | Renesas RX |
| 3.2 | Samsung SAM8 |
| 2.2 | STM8 |
| IBM XLC | 13 | AIX | Power, PPC |  |
| Intel C++ | 17.0.0 | Linux | x86 |  |
| 17.0.0-19.1.0 | Windows |
| Intel oneAPI DPC++/C++ | 2022.1.0 | Windows/Linux | x86_64 | OpenMP features are not supported. |
| 2024.2.1 | Linux |
| 2025.0.4 | Windows/Linux |
| Keil Compilers | RVCT 5.06 for uVision | Windows | ARM |  |
| 8.12-9.52 | C51 |
| 6.11-7.53 | C166 |
| 4.53a-5.55 | C251 |
| Microchip Compilers | XC8 1.42-2.36 | Windows | 8-bit PIC MCUs, 8-bit AVR MCUs |  |
| XC8 2.20-2.36 | Linux |
| XC16 1.50-2.00 | Windows/Linux | 16-bit PIC MCUs |
| XC32 2.20-4.00 | 32-bit PIC MCUs |
| XC-DSC 3.21 | Windows/Linux | 16-bit DSC PIC MCUs |
| Microsoft Visual C++ | 2019-2026 | Windows | x86, x86_64, ARM | Managed C++ and Common Language Runtime (CLR) are not supported. Compilations with switches beginning with "/CLR" will be skipped.  Visual C++ 2019 and higher are the only supported compilers for `FxCop` and `cov-import-msvsca`.  The compiler version can be determined by running the compiler (`cl`) on the command line, which returns detailed information. For example:   ``` > cl Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30146 for x86 Copyright (C) Microsoft Corporation.  All rights reserved.  usage: cl [ option... ] filename... [ /link linkoption... ] ``` |
| Panasonic compiler | 5.4R3 | Windows | MN103S, MN103L |  |
| QNX C/C++ | 6.5.0-7.1.0 | Windows/Linux | ARM |  |
| Intel XScale |
| MIPS |
| 8.0.0 | PPC |
| SH-4 |
| x86 |
| Qualcomm Compilers | 8.0.10 | Windows | Hexagon |  |
| 8.0.10-8.4.09 | Linux |
| 2.06 | Windows | Kalimba |
| 10.0.0 | Linux | Snapdragon ARM |
| Renesas C/C++ Compilers | 1.02r01 | Windows | R32C |  |
| 1.03 | RH850 |
| 1.03-1.09 | RL78 |
| 3.01 | RX |
| 2.72 | 78k0r |
| 3.47 | CA850 (NEC V850) |
| 5.41 | M32C |
| M16C |
| 6.02 | H8 |
| H8S |
| 9.01-9.04 | SuperH |
| 1.31 | V850 |
| SONY PS5 SDK | 4.000-12.000 | Windows | PS5 | Sony PS5 is supported only on Windows 64-bit systems. |
| Sun (Oracle) CC and cc | Studio12.6: CC and cc 5.15 | Solaris | SPARC, x86 |  |
| Synopsys MetaWare C and C++ Compilers (mcc/hcac binaries) | I-2013.12 | Windows/Linux | ARC 600 | ISO/IEC TR 18037 fixed point extensions are supported for C (not C++) code. |
| ARC 700 |
| ARC EM family |
| ARCompact |
| ARCtangent-A4 |
| Synopsys MetaWare C and C++ Compilers (ccac binary) | N-2017.09-X-2025.09 | Windows/Linux | ARC EM family | ISO/IEC TR 18037 fixed point extensions are supported for C and C++ code.  AT&T inline assembly syntax is supported for C and C++ code. |
| ARC HS family |
| TASKING | 5.2r1 | Windows | ARM Cortex |  |
| 6.0r1-6.3r1 | TriCore | ISO/IEC TR 18037 fixed point extensions are supported for C (not C++) code on TriCore. |
| 10.0r8 | C68K/Coldfire target 5235 and 68360 |  |
| Texas Instruments Code Composer | 17.3.0-20.2.7 | Windows | ARM (armcl) | TI compilers require an environment variable to be set in order for `cov-configure` to properly probe compiler behavior. The environment variable should point to the include directories, and is specific to the compiler (for example, `C6X_C_DIR` for the C6000 compiler). |
| 16.9.11 | MSP430 |
| 5.1.0-7.6.0 | TMS320C6x |
| 4.1.0-4.2.0 | TMS320C54x |
| 3.2.2-4.3.6 | TMS320C55x |
| 4.1.0-25.11.0 | TMS320C2000 |
| 4.1.2-4.6.3 | TMS470 |
| 15.12.3 | Linux | ARM (armcl) |
| 1.3.0-2.1.3 | ARM (tiarmclang) |
| 1.2.0 | C7000 |
| 5.1.0-8.3.12 | TMS320C6x |
| 4.1.0-6.2.8 | TMS320C2000 |
| Wind River (formerly Diab) C/C++ | 5.0.x-5.9.1 | Windows/Linux | ARM (XSCALE) |  |
| ColdFire |
| M32R |
| MC68k |
| M*CORE |
| MIPS |
| PPC |
| SH |
| SPARC |
| TriCore |
| x86 |
| 7.0.5 | Windows | ARM (XSCALE) |
| 4.3g | Windows | PowerPC |
| Xcode (with Clang compiler) | Apple Clang 12.0 (Xcode 12.0-12.5) | macOS | ARM, x86, x86_64 | macOS on Intel: To ensure a complete capture, version 12-26 of Xcode (with command line tools) must be installed. Also, ensure that `xcodebuild -version` runs without error; Coverity uses this command to check the Xcode version.  macOS on Apple silicon: Build capture requires both Rosetta 2 and Xcode (*with command line tools*) 12-26 in order to function. Please ensure `xcodebuild -version` runs without error.  Deprecation Notice: Support for Xcode 12.x-14.x is deprecated as of 2025.12. |
| Apple Clang 13.1.6 (Xcode 13.3) |
| Apple Clang 14.0.3 (Xcode 14.0-14.3) |
| Apple Clang 15.0.0 (Xcode 15.0-15.3) |
| Apple Clang 16.0.0 (Xcode 16.0) |
| Apple Clang 17.0.0 (Xcode 16.3) |
| Apple Clang 19.0.0 (Xcode 26.0) |
| Xtensa compilers | xt-xcc and xt-xtc++ RI-2019.2 | Windows/Linux | x86, xtensa |  |
| xt-clang RI-2021.7-2022.10 | xtensa |
| xt-clang RI-2023.11 | Linux | xtensa |
| xtensa RJ-2024.4 |
| xtensa RJ-2025.5 |
| Paradigm | 5.0 | Windows | x86 |  |

Note: The Platform Builder IDE is supported if the compiler that it is using is supported.
Platform Builder is not a compiler.
