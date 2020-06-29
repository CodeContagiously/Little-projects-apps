"""this class performs binary to decimal operations and decimal to binary operations"""

class BinaryDecimal:

    def toBinary(self, decNum):
        """return binary equivalent of decimal number"""
        binum = [] ##list object of binary numbers
        while decNum >0: ##algorythm is divide by two to get remainder; is the binary values of decNum
            binum.append(str(decNum%2)) ##append the remainder of the division to list of biNum
            decNum = decNum//2 ##redefine the decimal number to the new divident value after division
        binum.append("0") ##append the last zero of the remainder division
        return "".join(binum)

    def toDecimal(self, BiNum):
        """return decimal equivalent of Binary number"""
        decnum = 0
        for pos in range(len(BiNum)): ##algorythm go through string BiNum get position. raise two by it and multiply with val at that position
            decnum = decnum + int(BiNum[pos]) * (2**pos)

        return decnum ## return the decimal number


bi = BinaryDecimal()
print(bi.toBinary(10))
print(bi.toDecimal("0011"))