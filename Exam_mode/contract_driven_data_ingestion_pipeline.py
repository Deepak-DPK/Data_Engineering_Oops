from abc import ABC,abstractmethod

class DataSource(ABC):
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def read(self):
        pass


class BaseSource(DataSource):
    def __init__(self,source_name):
        self._source_name = source_name

    def connect(self):
        return f"Connected to {self._source_name}"
    
    
class PostgresSource(BaseSource):

    def validate(self):
        return "PostgresSource is validating"
    def read(self):
        return "PostgresSource is reading"
    
    
class APIDataSource(BaseSource):

    def validate(self):
        return "APIDataSource is validating"
    def read(self):
        return "APIDataSource is reading"
    

class S3Source(BaseSource):

    def validate(self):
        return "S3Source is validating"
    def read(self):
        return "S3Source is reading"
    

def run_pipeline(source:DataSource):

    Connection_status = source.connect()
    Validate_status = source.validate()
    Read_status = source.read()
    

    return {
        "Source":source._source_name,
        "Connection":Connection_status,
        "Validation":Validate_status,
        "data":Read_status
    }


p1=PostgresSource("postgres")
a1=APIDataSource("API")
s1=S3Source("S3")

print(run_pipeline(p1))
print(run_pipeline(a1))
print(run_pipeline(s1))



