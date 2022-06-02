class Errors(Exception):
    """
    Base class for exceptions in this module.
    """
    def __init__(self, message: str):
        """
        Constructor of the exception.
        """
        super().__init__(message)
        self.__message = message
    
    def __str__(self) -> str:
        """
        String representation of the exception.
        """
        return self.__message
    
    def __repr__(self) -> str:
        """
        String representation of the exception.
        """
        return self.__message

    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return self.__message == other.message
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)

class AccidentAssuranceError(Errors):
    """
    Exception for the accident without insurance.
    """
    def __init__(self, reparation: object, vehicule: object):
        """
        Constructor of the exception.
        """
        message = "Accident sans assurance : " + str(reparation) + " " + str(vehicule)
        super().__init__(message)
        self.__message = message
        self.__reparation = reparation
        self.__vehicule = vehicule

    def __str__(self) -> str:
        """
        String representation of the exception.
        """
        return self.__message
    
    def __repr__(self) -> str:
        """
        String representation of the exception.
        """
        return self.__message

class WrongImmatruclationError(Errors):
    """
    Exception for the wrong immatruclation.
    """
    def __init__(self, immatruclation: str):
        """
        Constructor of the exception.
        """
        message = "Immatruclation incorrecte : " + immatruclation
        super().__init__(message)
        self.__message = message
        self.__immatruclation = immatruclation

    def __str__(self) -> str:
        """
        String representation of the exception.
        """
        return self.__message
    
    def __repr__(self) -> str:
        """
        String representation of the exception.
        """
        return self.__message
        

