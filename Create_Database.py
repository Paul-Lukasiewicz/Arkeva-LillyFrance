import chromadb
from Get_Embedding_Function import CustomOpenAIEmbeddings


def get_database():
	"""
	Cette fonction à pour but de créer une base de donnée vectorielle si elle n'existe pas.
	La première fois qu'elle est appellée, si le dossier Data_Path, n'existe pas, il est crée et la collection Lilly_France est crée
	Si tout ça existe déjà, on s'y connecte simplement

	CustomOpenAIEmbedding est la fonction d'embedding qu'on utilise sur les documents et les querys.

	collection est une instance de la base de donnée qu'on appelle pour intéragir avec les données de la table.
	"""
	Data_Path = "POC_Lilly_Database"
	persistent_client = chromadb.PersistentClient(path=Data_Path)
	collection = persistent_client.get_or_create_collection(name="Lilly_France", embedding_function=CustomOpenAIEmbeddings())

	return collection

if __name__ == '__main__':
	get_database()