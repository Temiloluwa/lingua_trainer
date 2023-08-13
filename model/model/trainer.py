from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.prompts.prompt import  PromptTemplate
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import FileChatMessageHistory
from dotenv import load_dotenv
from langchain.llms import OpenAI
import langchain

load_dotenv()

class Trainer:
    def __init__(self, 
                 table_name="hyc-lingua-trainer-tb"):
        self.table_name = table_name
        self.session_id = self.get_session_id()
        self.memory, \
        self.message_history = self.get_memory(self.session_id, 
                                               self.table_name)


    def get_session_id(self):
        return "1"


    def get_memory(self, 
                   session_id: str,
                   table_name: str):
        session_id = self.get_session_id()
        file_path = f"model/memory/history-session-{session_id}.json"
        message_history = FileChatMessageHistory(file_path="history.json")
        memory = ConversationBufferMemory(
                        memory_key="history", 
                        chat_memory=message_history, 
                        return_messages=True)
        return memory, message_history
        
    
    @classmethod
    def prepare_chat_prompt(cls,
                            task_prompt=None,
                            chat_history=[]):
        """ Generates Prompt Template """
        chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template("""
            You are a German tutor that tries to help you student grasp the German Language
            For each of your student's responses you provide constructive feedbacks to improve their mastery of German
            """),
         MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template(task_prompt)
        
        ])
                                
        return chat_prompt

        
    @classmethod
    def prompt_model(cls,
                     trainer,
                     chat_input=None,
                     task_prompt=None,
                     temperature=0.5,
                     memory=None,
                     verbose=True,
                    ):
        """Prompt Model """

        chat_prompt = Trainer.prepare_chat_prompt(task_prompt)
        llm = ChatOpenAI(temperature=temperature)

        if memory is None and not getattr(trainer, "memory"):
            memory = ConversationBufferMemory(return_messages=True)
        elif hasattr(trainer, "memory"):
            memory = trainer.memory
            
        conversation = ConversationChain(memory=memory, 
                                        prompt=chat_prompt, 
                                        llm=llm, 
                                        verbose=verbose)
        response = conversation.predict(input=chat_input)
        return response
            

def process_answer(answer: str, 
                   temperature: float=0.7):
    ling_trainer = Trainer()
    trainer_response = ling_trainer.prompt_model(ling_trainer, 
                                                answer, 
                                                task_prompt, 
                                                temperature)
    return trainer_response

task_data = {
    "call-target": "Guten Morgen! Herzlich willkommen zum Vorstellungsgespräch. Können Sie mir etwas über Ihre frühere Arbeitserfahrung erzählen?",
    "call": "Good morning! Welcome to the interview. Can you tell me about your previous work experience?",
    "response-target": "Guten Morgen! Vielen Dank. Ich habe drei Jahre Erfahrung in Projektmanagement und Teamführung.",
    "response": "Good morning! Thank you. I have three years of experience in project management and team leadership."
}

response = task_data["response"]
response_target = task_data["response-target"]

task_prompt = f"""
    Your student has provided a German translation for the English Statement: {response}.
    The expected response you want from the student is this: {response_target}.
    Provide hints only when the student's answer is wrong. 
    When possible, you would  be provide previous interactions between you and the student.
    Rate the student's response on a scale of poor, average, good, and excellent.
    Count the number of attempts the student has made and state it in your response.
    Guide the student to the right answer by obeyings these instructions:
        1. Hints should be provided in English
        2. Do not supply an english to german or german to english translation
        3. Hints should be explicitly state the problem to be corrected. 
        4. If the Student repeated a mistake refer to the repitition and correct them
        5. If the Student performed worse than the previous attempt, state this and correct them
        
    Example hints are:  
        - Correct the spelling of the "vermute"
        - The german word for happy is not correct
        - Revise the response by following German capitalization rules for nouns
        - The german word you provided for stop is almost correct. Could you think of a more appropriate german word for stop

    Evaluate the student's response by following this format:
    Desired Output:
        attempts: <Sum(Number of Student's attempts), think step by step>
        evaluation: <Rating>
        feedback: <Give a fair assessments of the student's effort>
        hints: <Your helpful hints>
    
    Student's Attempt: {{input}}
    
"""