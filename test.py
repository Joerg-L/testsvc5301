import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KVUri = os.environ['KEYVAULT_URI']
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
retrieved_secret = client.get_secret('example-secret')";
