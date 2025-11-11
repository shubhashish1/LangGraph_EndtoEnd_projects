# This file is used to read the config from the uiconfigfile.ini

# Now to read and extract details from the uiconfigfile.ini we need a config parser

from configparser import ConfigParser

class Config:
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file) # Reading the config file elements using ConfigParser

    # Now let's read one by one element. First let's go with llm option reading
    def get_llm_option(self):
        # In the uiconfigfile.ini DEFAULT is the root directory to access all the elements
        # Here we are using .split(",") to split this field by comma in case we have more than one entry such as 
        # groq, openai etc.
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        # Here page title can be only one, hence no split by comma
        return self.config["DEFAULT"].get("PAGE_TITLE")