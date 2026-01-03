from abc import ABC,abstractmethod

class DataSource(ABC):

    @abstractmethod 
    def connect(self):
        pass
    
    @abstractmethod
    def fetch(self):
        pass

class PostgresSource(DataSource):

    def connect(self):
        return "postgress connection"
    
    def fetch(self):
        return "fetched the source from the connection "


class APIDataSource(DataSource):

    def connect(self):
        return "Connect to ExternalAPI"
    
    def fetch(self):
        return "Fetched data from API"


class S3Source(DataSource):

    def connect(self):
        return "Connect to s3 bucket"
    
    def fetch(self):
        return "Fetched data from s3 bucket"
    

def run_pipeline(source : DataSource):
    connection_status = source.connect()
    data = source.fetch()

    return{
        "Connection": connection_status,
        "data": data
    }



p1=PostgresSource()
a1=APIDataSource()
s1=S3Source()



print(run_pipeline(a1))
print(run_pipeline(p1))
print(run_pipeline(s1))




