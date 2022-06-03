import datetime
import Client

from Errors import WrongImmatruclationError

class Immatriculation(object):
    """
    Class for the immatriculation of the vehicle.
    """

    def __init__(self, immatriculation: str):
        """
        Constructor of the immatriculation.
        """
        self.__immatriculation = immatriculation
    
    @property
    def immatriculation(self) -> str:
        """
        Getter of the immatriculation.
        """
        return self.__immatriculation
    
    @immatriculation.setter
    def immatriculation(self, immatriculation: str) -> None:
        """
        Setter of the immatriculation.
        """
        if self.checkImmatriculation(immatriculation):
            self.__immatriculation = immatriculation
        else:
            raise WrongImmatruclationError(immatriculation)
    
    def checkImmatriculation(self, immatriculation: str) -> bool:
        """
        Check if the immatriculation is valid.
        """
        if len(immatriculation) != 7:
            return False
        if (
                immatriculation[0].isalpha() 
            and immatriculation[1].isdigit() 
            and immatriculation[2].isalpha() 
            and immatriculation[3].isdigit() 
            and immatriculation[4].isalpha() 
            and immatriculation[5].isdigit() 
            and immatriculation[6].isalpha()
        ):
            return True
        else:
            return False
    
    def __str__(self) -> str:
        """
        String representation of the immatriculation.
        """
        return self.__immatriculation
    
    def __repr__(self) -> str:
        """
        String representation of the immatriculation.
        """
        return self.__immatriculation
    
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return self.__immatriculation == other.immatriculation
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)
    
    


class Vehicule(object):
    """
    Class for the vehicle.
    """

    def __init__(self, immatriculation: str, marque: str, modele: str, couleur: str, nbPlaces: int):
        """
        Constructor of the vehicle.
        """
        self.__immatriculation = Immatriculation(immatriculation)
        self.__marque = marque
        self.__modele = modele
        self.__couleur = couleur
        self.__nbPlaces = nbPlaces
       

    
    @property
    def immatriculation(self) -> object:
        """
        Getter of the immatriculation.
        """
        return self.__immatriculation
    
    @property
    def marque(self) -> str:
        """
        Getter of the vehicle's brand.
        """
        return self.__marque
    
    @marque.setter
    def marque(self, marque: str) -> None:
        """
        Setter of the vehicle's brand.
        """
        self.__marque = marque
    
    @property
    def modele() -> str:
        """
        Getter of the vehicle's model.
        """
        return self.__modele
    
    @modele.setter
    def modele(self, modele: str) -> None:
        """
        Setter of the vehicle's model.
        """
        self.__modele = modele
    
    @property
    def couleur(self) -> str:
        """
        Getter of the vehicle's color.
        """
        return self.__couleur
    
    @couleur.setter
    def couleur(self, couleur: str) -> None:
        """
        Setter of the vehicle's color.
        """
        self.__couleur = couleur
    
    @property
    def nbPlaces(self) -> int:
        """
        Getter of the vehicle's number of places.
        """
        return self.__nbPlaces
    
    @nbPlaces.setter
    def nbPlaces(self, nbPlaces: int) -> None:
        """
        Setter of the vehicle's number of places.
        """
        self.__nbPlaces = nbPlaces
    

    def __str__(self) -> str:
        """
        String representation of the vehicle.
        """
        return str(self.__immatriculation) + " " + self.__marque + " " + self.__modele + " " + self.__couleur + " " + str(self.__nbPlaces) 
    
    def __repr__(self) -> str:
        """
        String representation of the vehicle.
        """
        return str(self.__immatriculation) + " " + self.__marque + " " + self.__modele + " " + self.__couleur + " " + str(self.__nbPlaces)
    
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return self.__immatriculation == other.immatriculation
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)
    

class Vente(Vehicule):
    
    """
    Class for the sale of a vehicle.
    """

    def __init__(self, immatriculation: str, marque: str, modele: str, couleur: str, nbPlaces: int):
        """
        Constructor of the sale.
        """
        super().__init__(immatriculation, marque, modele, couleur, nbPlaces, proprietaire)
        self.__dateDeLivraison = datetime.date.today()
    
    @property
    def dateDeLivraison(self) -> datetime.date:
        """
        Getter of the delivery date.
        """
        return self.__dateDeLivraison
    
    def estGarantie(self, date) -> bool:
        """
        Check if the vehicle is garanteed.
        """
        if self.__dateDeLivraison + datetime.timedelta(days=365) > date:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        """
        String representation of the sale.
        """
        return super().__str__() + " " + str(self.__dateDeLivraison) + " " + str(self.estGarantie())

    
    def __repr__(self) -> str:
        """
        String representation of the sale.
        """
        return super().__repr__() + " " + str(self.__dateDeLivraison) + " " + str(self.estGarantie())
    
    def __eq__(self, other) -> bool:
        """
        Equality operator.
        """
        return self.__immatriculation == other.immatriculation
    
    def __ne__(self, other) -> bool:
        """
        Inequality operator.
        """
        return not self.__eq__(other)
    
