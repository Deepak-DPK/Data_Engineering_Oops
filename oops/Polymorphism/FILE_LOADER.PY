#base class 
class FileLoader:
    def read(self):
        raise NotImplementedError("Subclass must be implemented read()")

#child classes with same method different behaviours

class CSVLoader(FileLoader):
    def read(self):
        return "reading data from csv files"

class JSONLoader(FileLoader):
    def read(self):
        return "reading data from json files"
    
class ParaquetLoader(FileLoader):
    def read(self):
        return "Reading data from paraquet file"

def run_pipeline(loader: FileLoader):
    print(loader.read())

csv = CSVLoader()
json = JSONLoader()
paraquet=ParaquetLoader()

run_pipeline(csv)
run_pipeline(json)
run_pipeline(paraquet)
