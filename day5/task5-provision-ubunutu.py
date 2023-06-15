import os
from azure.identity import DefaultAzureCredential
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network.models import NetworkSecurityGroup, SecurityRule

# Set your Azure subscription ID and resource group name
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# Create Azure clients
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

# Set the VM and network details
vm_name = 'task5-vm'
vm_username = 'task5-user'
vm_password = 'jananitetask5@1234'
vnet_name = 'task5-vnet'
subnet_name = 'task5-subnet'
nsg_name = 'task5-nsg'
ip_config_name = "task5-ip-config"
ip_name = "task5-ip"
nic_name = 'task5-nic'

# Step 1: Provision a resource group
resource_group_name = "task5-rg"
location = "central india"
rg_result = resource_client.resource_groups.create_or_update(resource_group_name, {"location": location})
print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")


# Step 2: provision a virtual network
vnet_params =  {
        "location": location,
        "address_space": {"address_prefixes": ["10.0.0.0/16"]}
}

poller = network_client.virtual_networks.begin_create_or_update(resource_group_name, vnet_name, vnet_params)
vnet_result = poller.result()
print(f"Provisioned virtual network {vnet_result.name} with address prefixes {vnet_result.address_space.address_prefixes}")

# Step 3: Provision the subnet and wait for completion
subnet_params = {"address_prefix": "10.0.0.0/24"}
poller = network_client.subnets.begin_create_or_update(resource_group_name, vnet_name, subnet_name, subnet_params)
subnet_result = poller.result()
print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")

# Step 4: Provision an IP address and wait for completion
pip_params =  {
        "location": location,
        "sku": {"name": "Standard"},
        "public_ip_allocation_method": "Static",
        "public_ip_address_version": "IPV4",
}
poller = network_client.public_ip_addresses.begin_create_or_update(resource_group_name, ip_name , pip_params)
ip_address_result = poller.result()
print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}")

# Step 5 : Provision a network security group
# Set the security rule details
security_rule_name = 'AllowSSH'
security_rule_priority = 100
security_rule_source_address_prefix = 'Internet'
security_rule_destination_port_range = '22'
security_rule_protocol = 'Tcp'
security_rule_access = 'Allow'

# Create a security rule for SSH access
ssh_rule = SecurityRule(
    name=security_rule_name,
    access=security_rule_access,
    description='Allow SSH',
    destination_port_range=security_rule_destination_port_range,
    destination_address_prefix='*',
    source_port_range='*',
    source_address_prefix=security_rule_source_address_prefix,
    protocol=security_rule_protocol,
    direction='Inbound',
    priority=security_rule_priority
)

nsg_params = NetworkSecurityGroup(location=location)
poller = network_client.network_security_groups.begin_create_or_update(resource_group_name, nsg_name, nsg_params)
nsg_result = poller.result()

network_client.security_rules.begin_create_or_update(resource_group_name, nsg_name, security_rule_name, ssh_rule)

# Create the network interface with NSG
nic_params = {
    'location': location,
    'ip_configurations': [
        {
        'name': ip_config_name,
        'subnet': {'id': subnet_result.id},
        'private_ip_allocation_method': 'Dynamic',
        'public_ip_address': None,
        'network_security_group': {'id': nsg_result.id}
        }
    ]
}
poller = network_client.network_interfaces.begin_create_or_update(resource_group_name, vm_name + '-nic', nic_params)
nic_result = poller.result()
# There is a bug here. The NSG is not getting associated to the NIC
# Step6 . Provision the virtual machine 
vm_params = {
    'location': location,
    'os_profile': {
        'computer_name': vm_name,
        'admin_username': vm_username,
        'admin_password': vm_password
    },
    'hardware_profile': {
        'vm_size': 'Standard_DS1_v2'
    },
    'storage_profile': {
        'image_reference': {
            'publisher': 'Canonical',
            'offer': 'UbuntuServer',
            'sku': '16.04-LTS',
            'version': 'latest'
        }
    },
    'network_profile': {
        'network_interfaces': [{
            'id': nic_result.id
        }]
    }
}

poller = compute_client.virtual_machines.begin_create_or_update(resource_group_name, vm_name, vm_params)
vm_result = poller.result()
print(f"Provisioned virtual machine {vm_result.name}")