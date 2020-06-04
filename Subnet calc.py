""" This program performes subnetting computations """
import IP as ip
class Net:
    def __init__(self):
        pass
    def IPSubnet(self, IPAddress_CDR):
        '''return the subnet given IP address and CDR number'''

    def NetRange(self, IPAddress_CDR):
        ''' returns the IP address range '''

    def subNet(self, IPAddress_CDR, numberOfNet):
        ''' Using VLSM, segment the network as specified
            Return each subnet and it's Range'''

    def subClass(self, IPAddress):
        if ip(IPAddress).firstOct() <= 127:
            return "Class A"
        if ip(IPAddress).firstOct() <= 191:
            return "Class B"
        if ip(IPAddress).firstOct() <= 223:
            return "Class C"
        if ip(IPAddress).firstOct() <= 224:
            return "Class D"
        
