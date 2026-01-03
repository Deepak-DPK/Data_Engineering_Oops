from abc import ABC, abstractmethod

class FileLoader(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def validate(self):
        pass 

class CSVLoader(FileLoader):
    def read(self):
        return "Reading csv data"
    
    def validate(self):
        return "csv schema validated"
    
c1=CSVLoader()
print(c1.read())
print(c1.validate())