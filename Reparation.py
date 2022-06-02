import enum
import datetime

from Vehicule import Vente
from Client import Assurance
from Errors import AccidentAssuranceError

class Reparation(object):
    """
    Class for the reparation.
    """
    def __init__(self,  dateDeRecuperation: object, dateDeRestitution: object, TypeDeReparation: object, vehicule: object, client: object, moyenDePaiement: str, prix: float):
        """
        Constructor of the reparation.
        """
        self.__dateDeDemande = datetime.datetime.now()
        self.__dateDeRecuperation = dateDeRecuperation
        self.__dateDeRestitution = dateDeRestitution
        self.__typeDeReparation = TypeDeReparation
        self.__vehicule = vehicule
        self._client = client
        self.__moyenDePaiement = moyenDePaiement
        self.__prix = prix
    
    @property
    def dateDeDemande(self) -> datetime.datetime:
        """
        Getter of the date of the reparation.
        """
        return self.__dateDeDemande
    

    @property
    def dateDeRecuperation(self) -> datetime.datetime:
        """
        Getter of the date of the reparation.
        """
        return self.__dateDeRecuperation
    
    @dateDeRecuperation.setter
    def dateDeRecuperation(self, dateDeRecuperation: datetime.datetime) -> None:
        """
        Setter of the date of the reparation.
        """
        self.__dateDeRecuperation = dateDeRecuperation
    
    
    @property
    def dateDeRestitution(self) -> datetime.datetime:
        """
        Getter of the date of the reparation.
        """
        return self.__dateDeRestitution

    @dateDeRestitution.setter
    def dateDeRestitution(self, dateDeRestitution: datetime.datetime) -> None:
        """
        Setter of the date of the reparation.
        """
        self.__dateDeRestitution = dateDeRestitution
    
    @property
    def typeDeReparation(self) -> object:
        """
        Getter of the type of the reparation.
        """
        return self.__typeDeReparation
    
    @typeDeReparation.setter
    def typeDeReparation(self, typeDeReparation: object) -> None:
        """
        Setter of the type of the reparation.
        """
        self.__typeDeReparation = typeDeReparation

    
    @property
    def vehicule(self) -> object:
        """
        Getter of the vehicle of the reparation.
        """
        return self.__vehicule
    
    @vehicule.setter
    def vehicule(self, vehicule: object) -> None:
        """
        Setter of the vehicle of the reparation.
        """
        self.__vehicule = vehicule

    @property
    def client(self) -> object:
        """
        Getter of the client.
        """
        return self._client
    
    @client.setter
    def client(self, client: object) -> None:
        """
        Setter of the client.
        """
        self._client = client
    
    @property
    def moyenDePaiement(self) -> str:
        """
        Getter of the payment method of the reparation.
        """
        return self.__moyenDePaiement
    
    @moyenDePaiement.setter
    def moyenDePaiement(self, moyenDePaiement: str) -> None:
        """
        Setter of the payment method of the reparation.
        """
        self.__moyenDePaiement = moyenDePaiement
    
    @property
    def prix(self) -> float:
        """
        Getter of the price of the reparation.
        """
        return self.__prix
    
    @prix.setter
    def prix(self, prix: float) -> None:
        """
        Setter of the price of the reparation.
        """
        self.__prix = prix
    
    def envoyerUneFacture(self) -> None:
        """
        Send a bill.
        """
        if isinstance(self.vehicule, Vente) and self.vehicule.estGarantie(self.dateDeDemande) and self.typeDeReparation == TypeDeReparation.GARANTIE:
            """
            If the vehicle is insured, the price is null and no bill.
            """
            self.prix(0)
            return None
        
        if self.TypeDeReparation == TypeDeReparation.SINISTRE:
            """
            If the reparation is a sinistre, the bill is send to insurance.
            """
           
            if isinstance(self.client, Assurance):
                """
                If the owner is insured, the bill is send to insurance.
                """
                return "Direction assureur : " + self.__str__(self)
            else:
                raise AccidentAssuranceError(self, self.vehicule)
        
        return self.__str__(self)

        
    def __str__(self) -> str:
        """
        String representation of the reparation.
        """
        return "Reparation de " + str(self.vehicule) + " le " + str(self.dateDeDemande) + " pour " + str(self.prix) + " euros"
    
    def __repr__(self) -> str:
        """
        String representation of the reparation.
        """
        return "Reparation de " + str(self.vehicule) + " le " + str(self.dateDeDemande) + " pour " + str(self.prix) + " euros"
    
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return (
            self.dateDeDemande == other.dateDeDemande
            and self.dateDeRecuperation == other.dateDeRecuperation
            and self.dateDeRestitution == other.dateDeRestitution
            and self.TypeDeReparation == other.TypeDeReparation
            and self.vehicule == other.vehicule
            and self.client == other.client
            and self.moyenDePaiement == other.moyenDePaiement
            and self.prix == other.prix
        )
    
    def __lt__(self, other) -> bool:
        """
        Less than operator.
        """
        return self.dateDeDemande < other.dateDeDemande
    
    def __le__(self, other) -> bool:
        """
        Less than or equal operator.
        """
        return self.dateDeDemande <= other.dateDeDemande
    
    def __gt__(self, other) -> bool:
        """
        Greater than operator.
        """
        return self.dateDeDemande > other.dateDeDemande
    
    def __ge__(self, other) -> bool:
        """
        Greater than or equal operator.
        """
        return self.dateDeDemande >= other.dateDeDemande
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)
    
    def __del__(self):
        """
        Destructor of the reparation.
        """
        print("Destruction de la réparation de " + str(self.vehicule) + " le " + str(self.dateDeDemande))
  
    


class TypeDeReparation(enum.Enum):
    """
    Enumeration of the type of reparation.
    """
    GARANTIE = 1
    SINISTRE = 2
    ENTRETIEN = 3
    AUTRE = 4
