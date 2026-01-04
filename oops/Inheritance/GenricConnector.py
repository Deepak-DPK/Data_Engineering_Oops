class BaseConnector:
    def __init__(self,host):
        self._host = host  #protected not private
    
    def connect(self):
        raise NotImplementedError("subclasses must implement connect()")
    
    def get_host(self):
        return self._host
    
class S3Connector(BaseConnector):
    def __init__(self, host, bucket_name):
        super().__init__(host)
        self.bucket_name = bucket_name
    
    def connect(self):
        return f"Connected to s3 bucket {self.bucket_name} at {self._host}"


host = input("Enter the Host name: ")
bucket_name=input("Enter the bucket name : ")

s1=S3Connector(host,bucket_name)

print('*'*15)

print(s1.get_host())
print(s1.connect())