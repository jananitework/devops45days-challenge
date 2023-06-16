import os
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
credential = AzureCliCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

for vms in compute_client.virtual_machines.list_all():
  print(vms.id)
