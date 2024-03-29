class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expression -- input expression in which the error occured
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expresion = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that"s not allowed.
    
        Attributes:
        previous -- state at beginning of transition
        next -- atemmpted new state
        message -- explanation of why the specific transition is not allowed
        """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

        