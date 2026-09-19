import enum
from cocotbext.pcie.core.caps import PciExtCap

# CXL Spec 8.1.1 pg. 523
CXL_VENDOR_ID = 0x1E98

# 
CXL_MEMORY_DEVICE_CLASS_CODE = 0x050210

class CxlDvsecId(enum.IntEnum):
    """
    DVSEC ID assignments, CXL Spec Table 8-2
    """
    DEVICE = 0
    NON_CXL_FUNCTION_MAP = 2
    PORT_EXTENSIONS = 3
    GPF_PORT = 4
    GPF_DEVICE = 5
    FLEXBUS_PORT = 7
    REGISTER_LOCATOR = 8
    MLD = 9
    
class CxlRegisterBlockId(enum.IntEnum):
    """
    CXL Spec Table 8-22
    """
    EMPTY = 0x00
    COMPONENT = 0x01
    BAR_VIRTUALIZATION_ACL = 0x02
    CXL_DEVICE = 0x03
    CPMU = 0x04
    
class CxlDvsec(PciExtCap):
    pass
    
class CxlDeviceDvsec(CxlDvsec):
    pass
    
