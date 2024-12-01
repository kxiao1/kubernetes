from dask.distributed import Client

client = Client("localhost:8786")

print(client)