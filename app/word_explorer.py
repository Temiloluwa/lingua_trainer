import re
import json
from typing import List, Dict
from queryverse.llm import OpenAI
from queryverse.prompter import SystemPrompter, UserPrompter

def get_llm(api_key: str, temperature: float=1) -> OpenAI:
    """Create llm object"""
    gpt = OpenAI(api_key, temperature=temperature)

    return gpt


def json_parser(response: str) -> List[dict]:
    """ parse json response """
    pattern = r'\{[^{}]*\}'
    matches = re.findall(pattern, response)
    data = [json.loads(match) for match in matches]

    return data


def word_explanator(german_word: str, llm: OpenAI) -> List[Dict[str, str]]:
    """
    Get an explanation and synonyms of a German word.

    Args:
    - german_word (str): The German word to explain and find synonyms for.
    - llm (OpenAI): An instance of OpenAI language model.

    Returns:
    str: a str that can be parsed to a list of dictionaries containing explanation and synonyms.
    
    Each dictionary has the following keys:
    - 'explanation' (str): A simple explanation in English.
    - 'synonyms' (str): Comma-separated synonyms.

    Example:
    >>> german_word = "Haus"
    >>> explanations_and_synonyms = word_explanator(german_word)
    >>> print(explanations_and_synonyms)
    [{'explanation': 'A house is a place where people live.', 'synonyms': 'Haushalt'}]
    """

    system_prompt = SystemPrompter("You are a fluent German speaker that is great at following instructions.")
    user_prompt = UserPrompter("""
        Given a German word, supply the following:
        1. An explanation of the word in English, in very simple terms (like to a child).
        2. Synonyms of the word if they exist.

        Output Format (comma-separated JSON format):
        
        explanation: <Simple explanation like to a child>
        synonyms: <comma-separated synonyms>

        German Word: {word}
    """)

    response = llm.prompt(messages=[system_prompt(), user_prompt(word=german_word)])
    explanations_and_synonyms = json_parser(response[0]['assistant'])
   
    return explanations_and_synonyms



def sentence_generator(german_word: str, number_of_sentences: int, llm: OpenAI) -> List[Dict[str, str]]:
    """
    Generate sentences in German based on a given word.

    Args:
    - german_word (str): The German word to base the generated sentences on.
    - number_of_sentences (int): The number of sentences to generate.
    - llm (OpenAI, optional): An instance of the OpenAI language model (default: None).

    Returns:
    List[Dict[str, str]]: A list of dictionaries containing contextual scenarios, German sentences,
    and their English translations.

    Each dictionary has the following keys:
    - 'context' (str): A series of sentences in English describing a scenario for which the generated sentence is applicable.
    - 'german sentence' (str): The sentence generated in German.
    - 'english translation' (str): The direct translation of the generated sentence to English.

    Example:
    >>> german_word = "Haus"
    >>> number_of_sentences = 2
    >>> generated_sentences = json_parser(sentence_generator(german_word, number_of_sentences))
    >>> for sentence in generated_sentences:
    >>>     print(sentence['context'])
    >>>     print("German: ", sentence['german sentence'])
    >>>     print("English: ", sentence['english translation'])
    """

    system_prompt = SystemPrompter("You are a fluent German speaker that is great at following instructions.")
    user_prompt = UserPrompter("""
        Given a German word, generate {num_sent} sentences with the word.
        First provide a contextual scenario in English, then generate the sentence in German.
        The sentences must vary in meaning, conjugated tense, tone (passive or active tone), and quantity (singular or plural) of the word.
        Avoid using the praeteritum; instead, use partizip II.

        Output Format (comma-separated JSON format):
        
        context: <A series of sentences in English describing a scenario for which the generated sentence is applicable>
        german sentence: <A sentence that was generated based on the supplied German word>
        english translation: <Direct translation of the generated sentence to English>

        German Word: {word}
    """)

    response = llm.prompt(messages=[system_prompt(), 
                                    user_prompt(word=german_word, num_sent=number_of_sentences)])

    generated_sentences = json_parser(response[0]['assistant'])
    return generated_sentences