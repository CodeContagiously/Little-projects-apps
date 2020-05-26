"""This class handles computations with octet groups in IPv4 address"""

class IP:
    def __inti__(self, IPaddress):
        self.ip = IPaddress

    def firstOct(self):
        '''returns the decimal value of first octet in IPaddress'''
        endIndx = self.ip.index(".")#gives first index of substring "."
        return self.ip[:endIndx]
