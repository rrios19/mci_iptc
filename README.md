# Integrated Power Testing System for CubeSats (IPTC)

![IPTC Logo](GUI/IPTC_logo.png)

## Overview

The Integrated Power Testing System for CubeSats (IPTC) is a comprehensive control and interface module designed for CubeSat power testing. This repository contains the source code and configuration files for the IPTC system. The system is developed by the SetecLab at the Tecnologico de Costa Rica.

## Features

- **SPI Communication:** The system uses SPI communication to interface with modules, providing efficient and reliable communication for power testing operations.

- **Flexible Configuration:** Configure the system using the MCI Configuration Tool (`mci-config.py`), allowing users to adapt the system to specific test scenarios.

- **Modular Design:** The system is designed with a modular structure, allowing for easy integration of additional functionalities and modules.

- **Logging and Debugging:** Utilizes logging mechanisms for detailed debugging and logging of system activities.

## Repository Structure

- **`ifaces/`:** Contains interface modules, such as SPI master (`spi_master.py`), for communication with external devices.

- **`conf/`:** Configuration tools and files, including `mci-config.py` for system configuration.

- **`macro/`:** Stores macro files generated during the testing process.

- **`tests/`:** Test cases and scripts for validating system functionalities.

Regarding the conf/local_conf.json file 

    The JSON file represents a nested dictionary with two main keys: "usr" and "mci".
    "usr" contains user-related configuration settings, such as logging paths, verbosity level, network information, file paths, etc.
    "mci" contains MCI-related configuration settings, including test file information, logging paths, verbosity level, instrument identifiers, command acknowledgment, reset values, shift values, file type configurations, manufacturer details, model, serial, and version.



Regarding the scpi_set.json file

    *IDN?: This SCPI command corresponds to the Python function run_IDN.
    *CLS: This SCPI command corresponds to the Python function run_CLS.
    *RST: This SCPI command corresponds to the Python function run_RST.
    INST: This SCPI command corresponds to the Python class INST.
    CAT?, CAT: These SCPI commands correspond to the Python method CAT_cmd within the INST class.
    SEL: This SCPI command corresponds to the Python method SEL_cmd within the INST class.
    NSEL: This SCPI command corresponds to the Python method NSEL_cmd within the INST class.
    INIT: This SCPI command corresponds to the Python method INIT_cmd within the INST class.
    CONF: This SCPI command corresponds to the Python class CONF.
    TIME, TINT, SAMP, MODE, CURR, VOLT, POW, ANGL, COUN: These SCPI commands correspond to the respective Python methods within the CONF class.
    MEAS: This SCPI command corresponds to the Python class MEAS.
    VOLT?, CURR?, POW?, RES?: These SCPI commands correspond to the respective Python methods within the MEAS class.
    SYST: This SCPI command corresponds to the Python class SYST.
    ERR?: This SCPI command corresponds to the Python method ERR_cmd within the SYST class.
    MEM: This SCPI command corresponds to the Python class MEM.
    DEL: This SCPI command corresponds to the Python method DEL_cmd within the MEM class.