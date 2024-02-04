# mci_iptc

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