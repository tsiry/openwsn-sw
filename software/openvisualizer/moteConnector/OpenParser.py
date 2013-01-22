
import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
log = logging.getLogger('OpenParser')
log.setLevel(logging.ERROR)
log.addHandler(NullHandler())

from ParserException import ParserException
import Parser
import ParserStatus
import ParserInfoErrorCritical
import ParserData

class OpenParser(Parser.Parser):
    
    HEADER_LENGTH  = 1
    
    TYPE_STATUS          = ord('S')
    TYPE_INFO            = ord('I')
    TYPE_ERROR           = ord('E')
    TYPE_CRITICAL        = ord('C')
    TYPE_DATA            = ord('D')
    TYPE_ALL             = [TYPE_STATUS,
                            TYPE_ERROR,
                            TYPE_DATA,]
    
    def __init__(self):
        
        # log
        log.debug("create instance")
        
        # initialize parent class
        Parser.Parser.__init__(self,self.HEADER_LENGTH)
        
        # subparser objects
        self.parserStatus              = ParserStatus.ParserStatus()
        self.parserInfoErrorCritical   = ParserInfoErrorCritical.ParserInfoErrorCritical()
        self.parserData                = ParserData.ParserData()
        
        # register subparsers
        self._addSubParser(index=0,  val=self.TYPE_STATUS,     parser=self.parserStatus.parseInput)
        self._addSubParser(index=0,  val=self.TYPE_INFO,       parser=self.parserInfoErrorCritical.parseInput)
        self._addSubParser(index=0,  val=self.TYPE_ERROR,      parser=self.parserInfoErrorCritical.parseInput)
        self._addSubParser(index=0,  val=self.TYPE_CRITICAL,   parser=self.parserInfoErrorCritical.parseInput)
        self._addSubParser(index=0,  val=self.TYPE_DATA,       parser=self.parserData.parseInput)
    
    #======================== public ==========================================
    
    #======================== private =========================================