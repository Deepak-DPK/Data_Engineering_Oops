#base class
class FileLoader:
    def read(self):
        raise NotImplementedError
    
    def validate(self):
        raise NotImplementedError
    
# child class
class CSVLoader(FileLoader):
    def read(self):
        return "Reading csv data"
    def validate(self):
        return "CSV schema Validated"

class JSONLoader(FileLoader):
    def read(self):
        return "Reading json data"
    def validate(self):
        return "JSON structure is validated"
    
class ParaquetLoader(FileLoader):
    def read(self):
        return "Reading paraquet data"
    def validate(self):
        return "paraquet metadata is validated"


def run_pipeline(loader : FileLoader):
    print(loader.read())
    print(loader.validate())

csv=CSVLoader()
Json=JSONLoader()
paraquet=ParaquetLoader()

run_pipeline(csv)
run_pipeline(Json)
run_pipeline(paraquet)
