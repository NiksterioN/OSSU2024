"""@package docstring
Documentation for this module.

The translated code will be stored
in the computer's memory starting at address 0, and variables will be allocated to
memory locations starting at address 1024


More details.
"""

class Parser:
    
    def __init__(self, filename):
        """
        # Opens the file as a filehandlers
        """
        self.filename = open(filename)
        self.currentCommand = self.advance()
        
    def hasMoreCommands(self):
        """
        Returns True if  there more commands in the
        input, otherwise returns False
        """
        if not self.currentCommand:
            return False
        return True

    
    def advance(self):
        """
        Reads the next command from
        the input and makes it the current
        command. Should be called only
        if hasMoreCommands() is true.
        Initially there is no current command.
        """
        
        while True:
            self.currentCommand = self.filename.readline()
            if not self.currentCommand.startswith(('/', '\n')): 
                break
        self.currentCommand = self.currentCommand.strip()
        return self.currentCommand
    

    def commandType(self):
        """
          @brief Returns the type of the current command : 
            A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number,
            C_COMMAND for dest=comp;jump, 
            L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol    
        """
        
        firstChar = self.currentCommand[0]
        if firstChar == '@':
            return "A_COMMAND"
        elif firstChar == '(':
            return "L_COMMAND"
        else:
            return "C_COMMAND"
    
    def symbol(self):
        """
            @brief returns the symbol or decimal Xxx of the current command 
            Xxx or (Xxx).
            Should only be called only when commandType() is A_COMMAND or L_COMMAND
        """
        # symbolBits = format(int(self.currentCommand[1:]), '#017b')
        # return symbolBits[2:]
        # Symbol
        if self.currentCommand.find('(') > -1:
            return self.currentCommand[1:-1]
        else:
            return self.currentCommand[1:]
    
    def dest(self):
        """
        @brief Returns the dest mnemonic in
        the current C-command (8 possibilities). Should be called only
        when commandType() is C_COMMAND.

        """
        equalIndex = self.currentCommand.find('=')
        return self.currentCommand[:equalIndex]
    
        pass
    
    def comp(self):
        """
        @brief Returns the comp mnemonic in
        the current C-command (28 possibilities). Should be called only
        when commandType() is
        C_COMMAND.
        """
        equalIndex = self.currentCommand.find('=')
        semicolonIndex = self.currentCommand.find(';')
        if semicolonIndex > -1:
            return self.currentCommand[equalIndex+1:semicolonIndex]
        else:
            return self.currentCommand[equalIndex+1:]
        
        pass
    
    def jump(self):
        """
        @brief Returns the jump mnemonic in
        the current C-command (8 possibilities). Should be called only
        when commandType() is
        C_COMMAND.
        """
        semicolonIndex = self.currentCommand.find(';')
        if semicolonIndex > -1: 
            return self.currentCommand[semicolonIndex+1:]
        else:
            return None
        pass

    def reset(self):
        """
        @brief Resets the file pointer to beginning
        and clears the currentCommand string.
        """
        self.filename.seek(0)
        self.currentCommand = self.advance()
        return self.currentCommand
    
    def __del__(self):
        self.filename.close()
        
    
class Code:
    def __init__(self):
        self.destinationKeyWords = {None : 0, "M"  : 1, "D"  : 2, "MD"  : 3,
                                    "A"    : 4, "AM" : 5, "AD" : 6, "AMD" : 7}
        
        self.jumpKeyWords =  { None : 0, "JGT" : 1, "JEQ" : 2, "JGE" : 3,
                               "JLT"  : 4, "JNE" : 5, "JLE" : 6, "JMP" : 7}        
        
        
        self.compKeyWords = {"0"   : "101010", "1"   : "111111", "-1"  : "111010",
                             "D"   : "001100", "A"   : "110000", "!D"  : "001111",
                             "!A"  : "110001", "-D"  : "001101", "-A"  : "110011",
                             "D+1" : "011111", "A+1" : "110111", "D-1" : "001110",
                             "A-1" : "110010", "D+A" : "000010", "D-A" : "010011",
                             "A-D" : "000111", "D&A" : "000000", "D|A" : "010101",}
        

    def dest(self, command):
        """
        @brief Returns the binary code of the dest mnemonic.
        """
        destinationBits = format(self.destinationKeyWords[command], '#05b')
        return destinationBits[2:]
        pass
    
    def comp(self, command):
        """
        @brief Returns the binary code of the comp mnemonic.
        """
        compBits = ""
        if command.find('M') >= 0 :
            command = command.replace('M', 'A') 
            compBits += "1"
        else:
            compBits += "0"
        
        return compBits + self.compKeyWords[command]
        
    def jump(self, command):
        """
        @brief Returns the binary code of the jump mnemonic.
        """
        jumpBits = format(self.jumpKeyWords[command], '#05b')
        return jumpBits[2:]

        
    
class SymbolTable:
    def __init__(self):
        # self.symbolIndex = 0
        # self.addressIndex = 1024
        self.addressTable = {}  
        
    def addEntry(self, symbol, address):
        """
        @brief Adds the pair {symbol : address} to the Symbol Table
        """
        self.addressTable[symbol] = address;
        
    def contains(self, symbol):
        """
        @brief Returns True if the symbol exists in the Symbol Table
        else False if does not exist.
        """
        return symbol in self.addressTable.keys()
    
    def getAddress(self, symbol):
        """
        @brief Returns the address associated with the symbol
        """
        return self.addressTable[symbol]
    def printKeys(self):
        for key in self.addressTable.keys():
            print(key, self.addressTable[key])


# Auxillary Functions - START
def isAorLCommand(commandType):
    """
        @brief Returns True if commandType is "A_COMMAND" or "L_COMMAND"
        otherwise returns False
    """
    if commandType == "A_COMMAND" or commandType == "L_COMMAND":
        return True
    return False

def isAorCCommand(commandType):
    """
        @brief Returns True if commandType is "A_COMMAND" or "C_COMMAND"
        otherwise returns False
    """
    if commandType == "A_COMMAND" or commandType == "C_COMMAND":
        return True
    return False

def symbolToStr(symbol, symbolTable):
    """
    @brief Returns the Symbol in String
    """


    symbolString = ""
    
    if symbol.isnumeric():
        symbolString = symbol
    else:
        symbolString = symbolTable.getAddress(symbol)
    
    symbolString = format(int(symbolString), '#017b')
    return "0" + symbolString[2:]


# Auxillary Functions - END

if __name__ == "__main__":
    filename = str(input("Enter .asm to convert into .hack : "))

    p1 = Parser(filename)
    c1 = Code()
    s1 = SymbolTable()    
    addressIndex = 0

# FIRST PASS
    while (p1.hasMoreCommands()):
        currentCommandType = p1.commandType()
        
        if isAorCCommand(currentCommandType):
            print(addressIndex)
            addressIndex = addressIndex + 1
        if currentCommandType == "L_COMMAND":
            symbolName = p1.symbol()
            s1.addEntry(symbolName, addressIndex)            
        p1.advance()
        
    p1.reset()
    
# SECOND PASS     
    with open(filename[:-4] + ".hack", "w") as savefile:
        while (p1.hasMoreCommands()):
            currentCommandType = p1.commandType()
            if currentCommandType == "A_COMMAND" or  currentCommandType == "L_COMMAND":
                b = symbolToStr(p1.symbol(), s1)
                #D
                savefile.write(b + '\n')
            if currentCommandType == "C_COMMAND":
                a =  "111" + c1.comp(p1.comp()) + c1.dest(p1.dest()) + c1.jump(p1.jump())
                savefile.write(a + '\n')
            
            p1.advance()     

