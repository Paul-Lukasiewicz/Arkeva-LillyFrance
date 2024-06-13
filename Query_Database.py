from Create_Database import get_database  # Fonction pour obtenir la connexion à la base de données
from langchain.prompts import ChatPromptTemplate  # Classe pour créer des templates de prompts
from langchain_openai import ChatOpenAI  # Classe pour interagir avec le modèle OpenAI GPT
from Ressources import prompt_template, OPENAI_API_KEY  # Template de prompt et clé API OpenAI



def main(query: str) -> None:
    """
    Fonction principale pour traiter une requête utilisateur.
    Arguments:
    query : str : La requête utilisateur.
    Retourne :
    str : La réponse du modèle de langage après traitement.
    """


    # Interroger la base de données avec la requête et obtenir le premier résultat
    response_from_database = query_database(query, 1)[0]
    # Créer un prompt pour le modèle de langage en utilisant la requête et la réponse de la base de données
    prompt = create_prompt(query, response_from_database)
    # Envoyer le prompt au modèle de langage et obtenir la réponse
    response_from_llm = request_to_llm(prompt)
    # Retourner la réponse obtenue du modèle de langage
    return response_from_llm



def query_database(query: str, number_of_results: int) -> [str]:
    """
    Interroge la base de données avec une requête donnée et retourne les résultats.
    Arguments:
    query : str : La requête à envoyer à la base de données.
    number_of_results : int : Le nombre de résultats à retourner.
    Retourne :
    [str] : Une liste de résultats de la base de données.
    """


    # Obtenir la collection de la base de données
    collection = get_database()
    # Interroger la collection avec le texte de la requête et obtenir les résultats
    results = collection.query(query_texts=[query], n_results=number_of_results)
    # Retourner les documents des résultats obtenus
    return results['documents'][0]



def request_to_llm(prompt: str) -> str:
    """
    Envoie un prompt au modèle de langage et retourne la réponse.
    Arguments:
    prompt : str : Le prompt à envoyer au modèle de langage.
    Retourne :
    str : La réponse du modèle de langage.
    """


    # Initialiser le modèle de langage OpenAI GPT avec la clé API
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
    # Envoyer le prompt au modèle et obtenir le contenu de la réponse
    response_text = model.invoke(prompt).content
    # Retourner le texte de la réponse
    return response_text



def create_prompt(query: str, context_texts: str) -> str:
    """
    Crée un prompt formaté en utilisant le template de prompt et les textes de contexte.
    Arguments:
    query : str : La requête utilisateur.
    context_texts : str : Les textes de contexte obtenus de la base de données.
    Retourne :
    str : Le prompt formaté prêt à être envoyé au modèle de langage.
    """


    # Créer un template de prompt à partir du template défini
    prompt = ChatPromptTemplate.from_template(prompt_template)
    # Formater le template avec les textes de contexte et la question
    prompt = prompt_template.format(context=context_texts, question=query)
    # Retourner le prompt formaté
    return prompt

if __name__ == '__main__':
	main("Hello")
