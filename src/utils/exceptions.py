class InvalidPostalCodeException(Exception):
    """
    Exception raised for invalid postal codes.
    """
    pass

class InvalidPopulationDataException(Exception):
    """
    Exception raised when population data provided is invalid.
    """
    pass
class InvalidDemandScoreException(Exception):
    """
    Represents an exception raised when an invalid demand score is encountered correctly.
    """
    pass

class LoginException(Exception):
    """
    Exception raised for errors during the login process.
    """
    pass

class SearchException(Exception):
    """
    Represents a custom exception that occurs during search operations.
    This can include invalid search requests or other search-related issues.
    """
    def __str__(self):
        return "A search-related exception occurred."
    
