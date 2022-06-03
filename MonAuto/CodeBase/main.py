import Vehicule
import Client 
import Reparation
import datetime

def main():
    """
    Main function.
    """

    immatriculation = "1-ABC-123"
    marque = "Peugeot"
    modele = "206"
    couleur = "bleu"
    nbPlaces = 5
    vehicule = Vehicule.Vehicule(immatriculation, marque, modele, couleur, nbPlaces)
    
    # Create a client.
    numeroDeClient = 1
    telephone = "0612345678"
    email = "tes"
    nom = "Dupont"
    adresse = "1 rue de la paix"
    codePostal = 75000
    ville = "Paris"
    prenom = "Jean"
    dateDeNaissance = datetime.date(2000, 1, 1)
    client = Client.Particulier(numeroDeClient, telephone, email, vehicule, nom, adresse, codePostal, ville, prenom, dateDeNaissance)
    
    # Create a reparation.
    date = datetime.date(2020, 1, 1)
    dateDeRecuperation = datetime.date(2020, 1, 2)
    dateDeRestitution = datetime.date(2020, 1, 3)
    
    TypeDeReparation = Reparation.TypeDeReparation.GARANTIE
    moyenDePaiement = "Espèce"
    prix = 100
    reparation = Reparation.Reparation(dateDeRecuperation, dateDeRestitution, TypeDeReparation, vehicule, client, moyenDePaiement, prix)

    # Print the reparation.
    print(reparation)

    # Print the client.
    print(client)

    # Print the vehicule.
    print(vehicule)

    # Print the date.
    print(date)

if __name__ == "__main__":
    main()