class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')

    def __str__(self):
        return self.alphabet.encode('utf-8')

    #===== Methods =====
    def encode(self, str):
        str = str.decode('utf-8')
        print(str.encode('utf-8'))
        result = ""
        fullKey = self.stretchKey(str)

        for character_i in range(0, len(str)):
            if(self.alphabet.find(str[character_i]) != -1):
                result += self.shiftChar(str[character_i], fullKey[character_i])
            else:
                result += str[character_i]
        return result.encode('utf-8')

    def decode(self, str):
        str = str.decode('utf-8')
        print(str.encode('utf-8'))
        result = ""
        fullKey = self.stretchKey(str)

        for character_i in range(0, len(str)):
            if(self.alphabet.find(str[character_i]) != -1):
                result += self.deshiftChar(str[character_i], fullKey[character_i])
            else:
                result += str[character_i]
        return result.encode('utf-8')
        

    def stretchKey(self, str):
        result = ""

        while(len(result) <= len(str)):
            result += self.key

        return result[0:len(str)]

    def shiftChar(self, char, shiftChar):
        shift = self.alphabet.find(shiftChar)
        shiftedValue = self.alphabet.find(char)+shift

        if(shiftedValue >= len(self.alphabet)):
            shiftedValue -= len(self.alphabet)

        return self.alphabet[shiftedValue]

    def deshiftChar(self, char, shiftChar):
        shift = self.alphabet.find(shiftChar)
        shiftedValue = self.alphabet.find(char)-shift

        if(shiftedValue < 0):
            shiftedValue += len(self.alphabet)

        return self.alphabet[shiftedValue]
