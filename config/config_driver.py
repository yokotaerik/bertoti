################################################################################
# Import Libraries

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

################################################################################
class ConfigDriver:
    
    def __init__(self):
        # options = Options()
        # options.add_argument("--headless")  # Adiciona o modo headless
        self.service = Service(executable_path=".\config\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)

    ################################################################################        
    def get_driver(self):
        return self.driver