"""This class handles computations with octet groups in IPv4 address"""

class IP:
    def __inti__(self, IPaddress):
        BitVal = [128,64,32,16,8,4,2,1] ##value of bits in each octed of ip
        self.ip = IPaddress
        IPaddress = IPaddress.split(".")
        self.firstOct = IPaddress[0] ##first octed of IP address
        self.secOct = IPaddress[1] ##sec octed
        self.thirdOct = IPaddress[2] ##third Octed
        self.fourthOct = IPaddress[3] ## fourth Octed
    def Class(self):
        if self.firstOct() <= 127:
            return "Class A"
        if self.firstOct() <= 191:
            return "Class B"
        if self.firstOct() <= 223:
            return "Class C"
        if self.firstOct() <= 224:
            return "Class D"
    def IP_BitVal(self):
        """Return Binary equivalent of IP address"""
        ip = self.ip.split(".")##create a list object of IP
        ##convert each val to binary
        ##Use Binary module I made

    def DecimalBit(self):
        """returns the Decimal value of Binary IP """