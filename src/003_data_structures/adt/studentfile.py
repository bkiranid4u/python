class StudentFileReader :
    # Create new Student file reader instance 
    def __init__( self, inputSrc ) :
        self._inputSrc = inputSrc
        self._inputFile = None
    
    # Opens a connection to input file 
    def open( self ) :
        self._inputFile = open( self._inputSrc )
    
    # Closes Connection to input file
    def close( self ) :
        self._inputFile.close()
        self._inputFile = None
    
    # Extracts all student records 
    def fetchAll( self ) :
        sRecords = list()
        student = self.fetchRecord()
        while student != None:
            sRecords.append( student )
            student = self.fecthRecord()
        
        return sRecords

    # Fetch a record
    def fetchRecord( self ) :
        line = self._inputFile.readline()
        if line == "" :
            return None
        # if there is a student record, create storage object to store it 
        student = StudentRecord()
        student.idNum = int( line )
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = int(self._inputFile.readline())
        return student

class StudentRecord :
    def __init__( self ) :
        self .idNum = None
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
