import { ConversationChain } from "langchain/chains";
import { ChatOpenAI } from "langchain/chat_models/openai";
import { appendFile } from 'fs/promises';
import {
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  SystemMessagePromptTemplate,
  MessagesPlaceholder,
} from "langchain/prompts";
import { BufferMemory } from "langchain/memory";
import dotenv from "dotenv";

dotenv.config();

const sourceStatement = "Guten Morgen! Vielen Dank. Ich habe drei Jahre Erfahrung in Projektmanagement und Teamführung."
const targetStatement =  "Good morning! Thank you. I have three years of experience in project management and team leadership."

const chatStarter = {
    systemMessage: `You are a German tutor that tries to help you student provide the correct German translation for an English statement.
    For each of your student's responses provide constructive feedbacks and Hints to guide them to the right answer. 
    Applaud them when they finally get th e right translation`,  
    humanMessage: "{input}",
    initialPrompt: `Challenge from Teacher: Hello student, provide the German translation for this English sentence:${sourceStatement}.
    Follow the following instructions step by step to provide constructive feedback to the student. You should avoid English translations in your feedbacks.
    Give the student a maximum of two attempts before revealing the final answer. Refrain from providing the student the right answer until the student's second attempt is made.
    The target answer is ${targetStatement}. List my instructions then proceed.
    Desired format:
      feedback: {constructive feedbacks}
    `
  };

class Trainer {
    chat: ChatOpenAI
    chatPrompt: ChatPromptTemplate | null = null;
    memory: BufferMemory
    chain: ConversationChain | null = null;
    

    constructor(temperature: number = 0.5, chatStarter: any, verbose: boolean = false) {
        this.chat = new ChatOpenAI({
            openAIApiKey: process.env.OPENAI_API_KEY,
            temperature: temperature,
        });

        this.memory = new BufferMemory({
            returnMessages: true,
            memoryKey: "history"
          });
          
        this.initializeChat(chatStarter, this.memory, verbose);  
          
    }

    extractFeedback(dataToStore: string){
      appendFile('response.txt', dataToStore)
        .then(() => {
          console.log('Data has been stored in the file successfully.');
        })
        .catch((err) => {
          console.error('Error writing to file:', err);
        });
    }

    initializeChat({systemMessage = "", humanMessage = "", initialPrompt = ""}: typeof chatStarter,
                     memory: BufferMemory, 
                     verbose: boolean = false) {
        this.chatPrompt = ChatPromptTemplate.fromPromptMessages([
            SystemMessagePromptTemplate.fromTemplate(systemMessage),
            new MessagesPlaceholder("history"),
            HumanMessagePromptTemplate.fromTemplate(humanMessage)
          ]);
          
        this.chain = new ConversationChain({
            memory,
            prompt: this.chatPrompt,
            llm: this.chat,
            verbose: verbose,
        });

        this.chatWithTutor(initialPrompt, this.chain)
    
    }

    async chatWithTutor(input: string, chain: ConversationChain | null) {
    
        if (chain === null) {
          throw new Error("Chain is null");
        }
        else {
          const response = await chain.call({
            input: input
          });
        this.extractFeedback(response.response);
      }
    }
    evaluateAnswer(input:string) {
        this.chatWithTutor(input, this.chain)
    }
    
}

  
const germanTrainer = new Trainer(0.5, chatStarter, false);
germanTrainer.evaluateAnswer("Guten Morgen! Danke. Ich habe drei jahre ProjektManagement Erpharung und Team Leitung")


