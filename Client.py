import abc

class Client(abc.ABC):

    """
    Abstract class for the client.
    """
    @abc.abstractmethod
    def __init__(self, numeroDeClient: int, telephone: str, email: str, vehicule: object, nom: str, adresse: str, codePostal: int, ville: str):
        """
        Constructor of the client.
        """
        self.__numeroDeClient = numeroDeClient
        self.__telephone = telephone
        self.__email = email
        self.__vehicule = []
        self.__vehicule.append(vehicule)
        self.__nom = nom
        self.__adresse = adresse
        self.__codePostal = codePostal
        self.__ville = ville

    
    @property
    def numeroDeClient(self) -> int:
        """
        Getter of the client's number.
        """
        return self.__numeroDeClient
    

    
    @numeroDeClient.setter
    def numeroDeClient(self, numeroDeClient) -> None:
        """
        Setter of the client's number.
        """
        self.__numeroDeClient = numeroDeClient

    @property
    def telephone(self) -> str:
        """
        Getter of the client's telephone.
        """
        return self.__telephone

    
    @telephone.setter
    def telephone(self, telephone) -> None:
        """
        Setter of the client's telephone.
        """
        self.__telephone = telephone
    
    @property
    def email(self) -> str:
        """
        Getter of the client's email.
        """
        return self.__email
    
    
    @email.setter
    def email(self, email) -> None:
        """
        Setter of the client's email.
        """
        self.__email = email        

    @property
    def vehicule(self) -> object:
        """
        Getter of the client's vehicle.
        """
        return self.__vehicule
    
    
    @vehicule.setter
    def vehicule(self, vehicule) -> None:
        """
        Setter of the client's vehicle.
        """
        self.__vehicule.append(vehicule)

    @vehicule.deleter
    def vehicule(self) -> None:
        """
        Deleter of the client's vehicle.
        """
        for vehicule in self.__vehicule:
            del vehicule
        

    @property
    def nom(self) -> str:
        """
        Getter of the client's name.
        """
        return self.__nom

    
    @nom.setter
    def nom(self, nom) -> None:
        """
        Setter of the client's name.
        """
        self.__nom = nom
    
    @property
    def adresse(self) -> str:
        """
        Getter of the client's address.
        """
        return self.__adresse
    
    
    @adresse.setter
    def adresse(self, adresse) -> None:
        """
        Setter of the client's address.
        """
        self.__adresse = adresse
    
    @property
    def codePostal(self) -> int:
        """
        Getter of the client's postal code.
        """
        return self.__codePostal
    
    
    @codePostal.setter
    def codePostal(self, codePostal) -> None:
        """
        Setter of the client's postal code.
        """
        self.__codePostal = codePostal
    
    @property
    def ville(self) -> str:
        """
        Getter of the client's city.
        """
        return self.__ville
    
    
    @ville.setter
    def ville(self, ville) -> None:
        """
        Setter of the client's city.
        """
        self.__ville = ville

    @abc.abstractmethod
    def __str__(self, *args, **kwargs) -> str:
        """
        String representation of the client.
        """
        pass
    
    @abc.abstractmethod
    def __repr__(self, *args, **kwargs) -> str:
        """
        String representation of the client.
        """
        pass

    @abc.abstractmethod
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        pass

    @abc.abstractmethod
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        pass

    @abc.abstractmethod
    def __del__(self) -> None:
        """
        Destructor of the client.
        """
        pass


class Particulier(Client):

    """
    Class for the particulier client.
    """

    def __init__(self, numeroDeClient: int, telephone: str, email: str, vehicule: object, nom: str, adresse: str, codePostal: int, ville: str, prenom: str, dateDeNaissance: int):
        """
        Constructor of the particulier client.
        """
        super().__init__(numeroDeClient, telephone, email, vehicule, nom, adresse, codePostal, ville)
        self.__prenom = prenom
        self.__dateDeNaissance = dateDeNaissance

    @property
    def prenom(self) -> str:
        """
        Getter of the client's first name.
        """
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom) -> None:
        """
        Setter of the client's first name.
        """
        self.__prenom = prenom


    @property
    def dateDeNaissance(self) -> int:
        """
        Getter of the client's birth date.
        """
        return self.__dateDeNaissance
    
    @dateDeNaissance.setter
    def dateDeNaissance(self, dateDeNaissance) -> None:
        """
        Setter of the client's birth date.
        """
        self.__dateDeNaissance = dateDeNaissance
    
    def __str__(self) -> str:
        """
        String representation of the particulier client.
        """
        return "Particulier : " + self.nom + " " + self.prenom + " (" + str(self.numeroDeClient) + ")"
    
    def __repr__(self) -> str:
        """
        String representation of the particulier client.
        """
        return "Particulier : " + self.nom + " " + self.prenom + " (" + str(self.numeroDeClient) + ")"
    
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return (
            self.__numeroDeClient == other.numeroDeClient
            and self.__telephone == other.telephone
            and self.__email == other.email
            and self.__vehicule == other.vehicule
            and self.__nom == other.nom
            and self.__prenom == other.prenom
            and self.__adresse == other.adresse
            and self.__codePostal == other.codePostal
            and self.__ville == other.ville
            and self.__dateDeNaissance == other.dateDeNaissance
        )
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)
    
    def __del__(self) -> None:
        """
        Destructor of the particulier client.
        """
        del self.vehicule    

class Assurance(Client):

    """
    Class for the assurance client.
    """

    def __init__(self, numeroDeClient: int, telephone: str, email: str, vehicule: object, nom: str, adresse: str, codePostal: int, ville: str, siret: str):
        """
        Constructor of the assurance client.
        """
        super().__init__(numeroDeClient, telephone, email, vehicule, nom, adresse, codePostal, ville)
        self.__siret = siret

    @property
    def siret(self) -> str:
        """
        Getter of the client's siret.
        """
        return self.__siret
    
    @siret.setter
    def siret(self, siret) -> None:
        """
        Setter of the client's siret.
        """
        self.__siret = siret
    
    def __str__(self) -> str:
        """
        String representation of the assurance client.
        """
        return "Assurance : " + self.__nom + " (" + self.__numeroDeClient + ")"
    
    def __repr__(self) -> str:
        """
        String representation of the assurance client.
        """
        return "Assurance : " + self.__nom + " (" + self.__numeroDeClient + ")"
    
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return (
            self.__numeroDeClient == other.numeroDeClient
            and self.__telephone == other.telephone
            and self.__email == other.email
            and self.__vehicule == other.vehicule
            and self.__nom == other.nom
            and self.__adresse == other.adresse
            and self.__codePostal == other.codePostal
            and self.__ville == other.ville
            and self.__siret == other.siret
        )
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)
    
    def __del__(self) -> None:
        """
        Destructor of the assurance client.
        """
        return None
        