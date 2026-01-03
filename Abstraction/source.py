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

p1=PostgresSource()

print(p1.connect())
print(p1.fetch())