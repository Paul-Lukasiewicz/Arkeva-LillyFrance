from Create_Database import get_database

def add_to_database() -> None:
	"""Fonction test qui permet de mettre un contenu dans la base de donnée pour débugger"""

	collection = get_database()
	collection.add(documents=["Ceci est un exemple de contenu"], metadatas=[{'file': "Nom du document"}], ids=['test-001'])

	print(collection)


if __name__ == '__main__':
	add_to_database()
