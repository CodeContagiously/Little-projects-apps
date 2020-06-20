""" This program performes subnetting computations """
import IP as ip
class Net:
    bitVal = [128,64,32,16,8,4,2,1] ##bit value for each bit in an IP octed
    def IPSubnet(self, IPAddress_CDR):##sample input parameter: 10.11.10.1/24
        """return the subnet given the IP address and CDR number"""
        CDR = IPAddress_CDR[IPAddress_CDR.index("/"):] #get CDR number
        subNet = []
        while CDR>=8:
            subNet.append("255")
            CDR -= 8
        subNet.append(str(sum(self.bitVal[:4]))) ##add the last subnet Value to subnet
        return ".".join(subNet) ##return Subnet as string

    def NetRange(self, IPAddress_CDR):
        """ returns the IP address range of given Network or SubnetWork """
        subnet = self.IPSubnet(IPAddress_CDR)##get the subnet of IP address

    def subNet(self, IPAddress_CDR, numberOfNet):
        ''' Using VLSM, segment the network as specified
            Return each subnet and it's Range'''

    def subClass(self, IPAddress):
        """Return the class of the IP address"""
        return ip(IPAddress).Class
