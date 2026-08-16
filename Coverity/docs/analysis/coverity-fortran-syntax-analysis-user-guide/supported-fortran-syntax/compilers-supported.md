---
title: "Compilers supported"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compilers-supported.html"
content_id: "enaTguLC0sYUnRk3ukmfMw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:56.370005+00:00"
---

# Compilers supported

Configuration files for the following Fortran 77 compilers are supplied. In the first
column the filename of the configuration file is listed (without the filename
extension). The second column presents the mnemonic used in the table of Fortran
extensions.

Table 1. Configuration files for Fortran 77 compilers

| Configuration file | Mnemonic | Compiler name |
| --- | --- | --- |
| absoftf77.cnf | AB | Absoft FORTRAN 77 V4.3 |
| cyber.cnf | CBR | Control Data Cyber NOS/VE Fortran Version 1, level 1.6, PRS level 700 |
| cd4000.cnf | CD4 | Control Data 4000 Fortran |
| convex.cnf | CVX | Convex Fortran, Version 6.0 |
| crayf77.cnf | CF77 | Cray Fortran 77, V4 |
| decvms.cnf | DAV | DEC Equipment FORTRAN for Open VMS Alpha |
| decux.cnf | DEC | Digital Equipment FORTRAN for Ultrix and DIGITAL UNIX |
| digres.cnf | DR | Digital Research Fortran-77 |
| domain.cnf | DM | Apollo/Domain Fortran, SR 10 |
| vax.cnf | VAX | Digital Equipment VAX Fortran, Version 5.0 and VAX Fortran-HPO, Version 1.0 |
| f2c.cnf | F2C | F2c Fortran 77 |
| g77.cnf | F77 | GNU Fortran 77 |
| hp77.cnf | HP7 | HP Fortran 77 for series 800 |
| hpvms.cnf | HPVMS | HP Fortran for OpwnVMS 8.0 |
| ibmvs2.cnf | VS2 | IBM VS Fortran, Version 2, Release 2.5 |
| ibmxlf.cnf | XLF | IBM AIX XL FORTRAN V14.1 |
| laheyf77.cnf | LH | Lahey F77L, V5.00 and F77L-EM32 V5.00 |
| msf5.cnf | MS5 | Microsoft Fortran, V5.1, Microsoft Fortran PowerStation, V 1.0 |
| ndp.cnf | NDP | NDP Fortran, Release 2.0 |
| pdp11.cnf | PDP | DEC Equipment PDP-11 Fortran-77, Version 5.0 |
| prime.cnf | PR | Prime Fortran-77, T1.0-21.0 |
| prospero.cnf | PF | Prospero Fortran, V2.12 |
| rm.cnf | RM | Ryan-McFarland RM/Fortran V1.00, IBM Professional Fortran, V1.23 |
| rm2.cnf | RM2 | Ryan-McFarland RM/Fortran, V2.40 |
| rs6000.cnf | XLF | IBM AIX XL FORTRAN V6.1 |
| sgif77.cnf | SGI | Silicon Graphics MIPSpro Fortran 77, Version 3.4.1 |
| sunf77.cnf | SUN | Sun Fortran 77 |
| ftn77.cnf | FTN | Salford FTN77, V3.62 |
| unisys.cnf | UNI | Unisys 1100 Fortran-77, L10 |
| watcom.cnf | WAT | WATCOM Fortran 77 V11.0 |

Not all of the compilers are listed in the table. The DEC FORTRAN for AXP/VMS (DAV)
extensions are equivalent to those of DEC; only the default file name extensions differ.
For the Digital Research compiler, a configuration file with the supported types is
supplied and the `%INCLUDE` directive is supported. When you want
Coverity Fortran Syntax Analysis to accept the Digital Research compiler extensions you
have to adapt the configuration file.

Configuration files for the following Fortran 90, Fortran 95, Fortran-2003, Fortran 2008
and Fortran 2015 compilers are supplied:

Table 2. Configuration files for the Fortran 90, Fortran 95, Fortran-2003, Fortran 2008
and Fortran 2015 compilers

| Configuration file | Mnemonic | Compiler name |
| --- | --- | --- |
| absoftf90.cnf | AB90 | Absoft FORTRAN 90 V6.0 |
| absoftf95.cnf | AB95 | Absoft FORTRAN 95 V6 |
| crayf90.cnf | CF90 | Cray Fortran 90, V2 |
| crayf03.cnf | Cray | Cray Fortran, V7 |
| crayf08.cnf | Cray Fortran 2008, V8.1 | |
| cvf.cnf | CVF | Compaq Visual Fortran V6.6 |
| decf90.cnf | Dec-90 | DEC Fortran 90 |
| decf95.cnf | Dec-95 | DEC Fortran 95 |
| fujitsu.cnf | FUJ | Fujitsu Fortran 90 |
| gfortran.cnf | gfort | GNU Fortran 95 |
| g95.cnf | g95 | Open source Fortran 95 based on GNU |
| hpf95.cnf | HP95 | Fortran for HP-UX |
| hp9000.cnf | HP9 | HP-UX FORTRAN/9000 for series 300/400/700 and 800 |
| hpux.cnf | HP95 | HP Fortran 95 for HP-UX |
| intel7.cnf |  | Intel Visual Fortran V7.0 |
| intel9.cnf |  | Intel Visual Fortran V9.0 |
| intel0.cnf |  | Intel Visual Fortran V10.0 |
| intel11.cnf |  | Intel Visual Fortran V11.0 |
| intel12.cnf |  | Intel Visual Fortran V12.0 |
| intel13.cnf |  | Intel Visual Fortran V13.0 |
| intel14.cnf |  | Intel Visual Fortran V14.0 |
| intel15.cnf | INT | Intel Visual Fortran V15.0 |
| intel16.cnf | INT | Intel Visual Fortran V16.0 |
| intel17.cnf | INT | Intel Visual Fortran V17.0 |
| ibmxlf.cnf | XLF | IBM AIX XL Fortran |
| laheyf90.cnf | LF90 | Lahey Fortran 90 |
| laheyf95.cnf | LF95 | Lahey Fortran 95 |
| msfps.cnf | MSF | Microsoft Fortran PowerStation V4.0 |
| nagf90.cnf | NAG90 | NagWare f90 Compiler |
| nagfor.cnf | NAG | NagWare f95 Compiler |
| nasf95.cnf | NAS | NASoftware Fortran Plus Compiler |
| oracle12.5.cnf | OF95 | Oracle Developer Studio Fortran 95 V12.5 |
| pathscale.cnf | PATH | PathScale EKOPath Compiler |
| pgif90.cnf | PGI90 | The Portland Group Fortran 90 Compiler |
| pgif95.cnf | PGI95 | The Portland Group Fortran 95 Compiler |
| pgif03.cnf | PGI03 | The Portland Group Fortran 2003 Compiler |
| ftn90.cnf | FTN90 | Salford FTN90 |
| ftn95.cnf | FTN95 | Silverfrost FTN95 |
| sgif90.cnf | SG90 | Silicon Graphics MIPSpro Fortran 90, Version 7.3 |
| sgif95.cnf | SG95 | Silicon Graphics MIPSpro Fortran 95 |
| sunf90.cnf | SF90 | Sun Fortran 90 |
| sunf95.cnf | SF95 | Sun Fortran 95 |

The Fortran 90/95 extensions marked in the column F2003 of the table are included in the
Fortran 2003 standard. The Fortran 90/95 extensions marked in the column F2008 of the
table are included in the Fortran 2008 standard. The Fortran 90/95 extensions marked in
the column F2015 of the table are included in the Fortran 2015 standard.
