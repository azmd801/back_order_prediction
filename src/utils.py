import openai
import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
# from src.exception import CustomException
from src.logger import logs_logger,ai_assistant_logger

def AI_assistant(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    This function takes a prompt and a model name as input and returns the response generated by the OpenAI chatbot.

    Args:
    prompt (str): The prompt to be given to the chatbot.
    model (str): The name of the OpenAI model to be used. Default is "gpt-3.5-turbo".

    Returns:
    str: The response generated by the OpenAI chatbot.

    """

    # logging the prompt to a log file
    ai_assistant_logger.info(f"\n Request made to ai assistant:\n\n{prompt}")

    # Create a list of messages to be sent to the chatbot
    messages = [{'role':'system', 'content':'You are data science assistant.'},{"role": "user", "content": prompt}]
    
    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )

    output = response.choices[0].message["content"]

    # logging the response to a log file
    ai_assistant_logger.info(f"\n Request made to ai assistant:\n\n{output }")

    # Return the response generated by the chatbot
    return output 