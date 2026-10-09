from email_validator import validate_email, EmailNotValidError

class Client:  #Represent items in the client section
    def __init__(self,
                 client_id: int,
                 name: str,
                 email_address: str):

        """Initialize the client object 
          
           Args:
        Client_id (int): Unique identifier for the client.
        Name (str): Name of the client.
        Email_address (str): Email address of the client.
        """

        if client_id <= 0:
            raise ValueError("Client ID must be a positive number.")

        client_name = name.strip()
        if not client_name:
            raise ValueError("Client name cannot be empty.")

        try:
            validated_email = validate_email(email_address)

        except EmailNotValidError:
            raise ValueError("Invalid email address.")

        self._client_id = client_id
        self._name = client_name
        self.email_address = validated_email.email  # Store the normalized email address

    @property
    def client_id(self) -> int:
        """Get the client ID."""
        return self._client_id

    @property
    def name(self) -> str:
        """Get the client name."""
        return self._name
    

    @property
    def email_address(self) -> str:
        """Get the client email address."""
        return self._email_address

    @email_address.setter
    def email_address(self, value: str) -> None:
        """Set the email address, validating and normalizing it.
           Raises:
           EmailNotValidError: If the email address is not valid. 
        """

        ### check_deliverability=False is required by the assignment instructions. ###
        valid = validate_email(value, check_deliverability=False)
        self._email_address = valid.normalized

    