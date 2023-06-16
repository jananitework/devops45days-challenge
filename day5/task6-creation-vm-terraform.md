
# Install Terraform on windows 

#### 1. Create service principle 
A Service Principal is an application within Azure Active Directory whose authentication tokens can be used as the client_id, client_secret, and tenant_id fields needed by Terraform (subscription_id can be independently recovered from your Azure account details).

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "id": "f9182f0c-787c-49f3-b5e0-dda139de3996",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "user": {
      "name": "meera0569@gmail.com",
      "type": "user"
    }
  }
]
```

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az ad sp create-for-rbac --name sp1 --role Contributor --scopes /subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996
Creating 'Contributor' role assignment under scope '/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996'
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "0f57c09a-58a5-4be3-a6be-1fcac92535fc",
  "displayName": "sp1",
  "password": "Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa",
  "tenant": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850"
}
```
- appId is the client_id defined above.
- password is the client_secret defined above.
- tenant is the tenant_id defined above.

![image](https://github.com/jananitework/devops45days-challenge/assets/136428700/ffdc4cba-5957-4934-af47-b0ff5cfe78ea)

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5> az login --service-principal -u 0f57c09a-58a5-4be3-a6be-1fcac92535fc -p Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa --tenant 14347c6c-c7da-4f47-a3eb-89e0ac0d8850
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "id": "f9182f0c-787c-49f3-b5e0-dda139de3996",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "14347c6c-c7da-4f47-a3eb-89e0ac0d8850",
    "user": {
      "name": "0f57c09a-58a5-4be3-a6be-1fcac92535fc",
      "type": "servicePrincipal"
    }
  }
]

```
#### 2. Download terraform binaries and add to system path

# Use terraform to create a VM

#### 1. Terraform init

<details>
<summary>Terraform init output</summary>

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\task6> terraform init -upgrade

Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/azurerm versions matching "~> 2.0"...
- Finding hashicorp/random versions matching "~> 3.0"...
- Finding hashicorp/tls versions matching "~> 4.0"...
- Installing hashicorp/azurerm v2.99.0...
- Installed hashicorp/azurerm v2.99.0 (signed by HashiCorp)
- Installing hashicorp/random v3.5.1...
- Installed hashicorp/random v3.5.1 (signed by HashiCorp)
- Installing hashicorp/tls v4.0.4...
- Installed hashicorp/tls v4.0.4 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

```
</details>

#### 2. Terraform plan

<details>
<summary>Terraform plan output</summary>

```
PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\task6> terraform plan -var-file="dev-vm.tfvars"
data.azurerm_client_config.current: Reading...
data.azurerm_key_vault.keyvault: Reading...
data.azurerm_client_config.current: Read complete after 0s [id=2023-06-16 14:11:31.5339381 +0000 UTC]
data.azurerm_key_vault.keyvault: Read complete after 0s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.KeyVault/vaults/azurecredentials]
data.azurerm_key_vault_secret.app_id: Reading...
data.azurerm_key_vault_secret.subscription_id: Reading...
data.azurerm_key_vault_secret.tenant_id: Reading...
data.azurerm_key_vault_secret.password: Reading...
data.azurerm_key_vault_secret.app_id: Read complete after 10s [id=https://azurecredentials.vault.azure.net/secrets/clientid/405b538e7ef54b4f9d04e0c6eaa740c7]
data.azurerm_key_vault_secret.password: Still reading... [10s elapsed]
data.azurerm_key_vault_secret.subscription_id: Still reading... [10s elapsed]
data.azurerm_key_vault_secret.tenant_id: Still reading... [10s elapsed]
data.azurerm_key_vault_secret.tenant_id: Read complete after 10s [id=https://azurecredentials.vault.azure.net/secrets/tenantid/d844d71f699a4f1388e61f1531912957]
data.azurerm_key_vault_secret.password: Read complete after 10s [id=https://azurecredentials.vault.azure.net/secrets/clientsecret/e0643c106eb248dfbf2a87cad50821b8]
data.azurerm_key_vault_secret.subscription_id: Read complete after 10s [id=https://azurecredentials.vault.azure.net/secrets/subscriptionid/f0aa9b562a134d39b1e66db4be978843]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # azurerm_linux_virtual_machine.my_terraform_vm will be created
  + resource "azurerm_linux_virtual_machine" "my_terraform_vm" {
      + admin_username                  = "task6-user"
      + allow_extension_operations      = true
      + computer_name                   = (known after apply)
      + disable_password_authentication = true
      + extensions_time_budget          = "PT1H30M"
      + id                              = (known after apply)
      + location                        = "centralindia"
      + max_bid_price                   = -1
      + name                            = "task6-vm"
      + network_interface_ids           = (known after apply)
      + patch_mode                      = "ImageDefault"
      + platform_fault_domain           = -1
      + priority                        = "Regular"
      + private_ip_address              = (known after apply)
      + private_ip_addresses            = (known after apply)
      + provision_vm_agent              = true
      + public_ip_address               = (known after apply)
      + public_ip_addresses             = (known after apply)
      + resource_group_name             = "rg6"
      + size                            = "Standard_DS1_v2"
      + virtual_machine_id              = (known after apply)
      + zone                            = (known after apply)

      + admin_ssh_key {
          + public_key = (known after apply)
          + username   = "task6-user"
        }

      + os_disk {
          + caching                   = "ReadWrite"
          + disk_size_gb              = (known after apply)
          + name                      = "task6-osdisk"
          + storage_account_type      = "Standard_LRS"
          + write_accelerator_enabled = false
        }

      + source_image_reference {
          + offer     = "0001-com-ubuntu-server-jammy"
          + publisher = "Canonical"
          + sku       = "22_04-lts-gen2"
          + version   = "latest"
        }
    }

  # azurerm_network_interface.my_terraform_nic will be created
  + resource "azurerm_network_interface" "my_terraform_nic" {
      + applied_dns_servers           = (known after apply)
      + dns_servers                   = (known after apply)
      + enable_accelerated_networking = false
      + enable_ip_forwarding          = false
      + id                            = (known after apply)
      + internal_dns_name_label       = (known after apply)
      + internal_domain_name_suffix   = (known after apply)
      + location                      = "centralindia"
      + mac_address                   = (known after apply)
      + name                          = "task6-nic"
      + private_ip_address            = (known after apply)
      + private_ip_addresses          = (known after apply)
      + resource_group_name           = "rg6"
      + virtual_machine_id            = (known after apply)

      + ip_configuration {
          + gateway_load_balancer_frontend_ip_configuration_id = (known after apply)
          + name                                               = "task6-ipconfig"
          + primary                                            = (known after apply)
          + private_ip_address                                 = (known after apply)
          + private_ip_address_allocation                      = "Dynamic"
          + private_ip_address_version                         = "IPv4"
          + public_ip_address_id                               = (known after apply)
          + subnet_id                                          = (known after apply)
        }
    }

  # azurerm_network_interface_security_group_association.example will be created
  + resource "azurerm_network_interface_security_group_association" "example" {
      + id                        = (known after apply)
      + network_interface_id      = (known after apply)
      + network_security_group_id = (known after apply)
    }

  # azurerm_network_security_group.my_terraform_nsg will be created
  + resource "azurerm_network_security_group" "my_terraform_nsg" {
      + id                  = (known after apply)
      + location            = "centralindia"
      + name                = "task6-nsg"
      + resource_group_name = "rg6"
      + security_rule       = [
          + {
              + access                                     = "Allow"
              + description                                = ""
              + destination_address_prefix                 = "*"
              + destination_address_prefixes               = []
              + destination_application_security_group_ids = []
              + destination_port_range                     = "22"
              + destination_port_ranges                    = []
              + direction                                  = "Inbound"
              + name                                       = "SSH"
              + priority                                   = 1001
              + protocol                                   = "Tcp"
              + source_address_prefix                      = "*"
              + source_address_prefixes                    = []
              + source_application_security_group_ids      = []
              + source_port_range                          = "*"
              + source_port_ranges                         = []
            },
        ]
    }

  # azurerm_public_ip.my_terraform_public_ip will be created
  + resource "azurerm_public_ip" "my_terraform_public_ip" {
      + allocation_method       = "Dynamic"
      + availability_zone       = (known after apply)
      + fqdn                    = (known after apply)
      + id                      = (known after apply)
      + idle_timeout_in_minutes = 4
      + ip_address              = (known after apply)
      + ip_version              = "IPv4"
      + location                = "centralindia"
      + name                    = "task6-pip"
      + resource_group_name     = "rg6"
      + sku                     = "Basic"
      + sku_tier                = "Regional"
      + zones                   = (known after apply)
    }

  # azurerm_subnet.my_terraform_subnet will be created
  + resource "azurerm_subnet" "my_terraform_subnet" {
      + address_prefix                                 = (known after apply)
      + address_prefixes                               = [
          + "10.0.1.0/24",
        ]
      + enforce_private_link_endpoint_network_policies = false
      + enforce_private_link_service_network_policies  = false
      + id                                             = (known after apply)
      + name                                           = "task6-subnet"
      + resource_group_name                            = "rg6"
      + virtual_network_name                           = "task6-vnet"
    }

  # azurerm_virtual_network.my_terraform_network will be created
  + resource "azurerm_virtual_network" "my_terraform_network" {
      + address_space         = [
          + "10.0.0.0/16",
        ]
      + dns_servers           = (known after apply)
      + guid                  = (known after apply)
      + id                    = (known after apply)
      + location              = "centralindia"
      + name                  = "task6-vnet"
      + resource_group_name   = "rg6"
      + subnet                = (known after apply)
      + vm_protection_enabled = false
    }

  # tls_private_key.example_ssh will be created
  + resource "tls_private_key" "example_ssh" {
      + algorithm                     = "RSA"
      + ecdsa_curve                   = "P224"
      + id                            = (known after apply)
      + private_key_openssh           = (sensitive value)
      + private_key_pem               = (sensitive value)
      + private_key_pem_pkcs8         = (sensitive value)
      + public_key_fingerprint_md5    = (known after apply)
      + public_key_fingerprint_sha256 = (known after apply)
      + public_key_openssh            = (known after apply)
      + public_key_pem                = (known after apply)
      + rsa_bits                      = 4096
    }

Plan: 8 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + public_ip_address   = (known after apply)
  + resource_group_name = "rg6"
  + tls_private_key     = (sensitive value)

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.

```
</details>

#### 3. Terraform apply

<details>
<summary>Terraform apply output</summary>

```

PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\task6> terraform apply -var-file="dev-vm.tfvars"
data.azurerm_client_config.current: Reading...
data.azurerm_key_vault.keyvault: Reading...
data.azurerm_client_config.current: Read complete after 0s [id=2023-06-16 14:15:33.0125088 +0000 UTC]
data.azurerm_key_vault.keyvault: Read complete after 0s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.KeyVault/vaults/azurecredentials]
data.azurerm_key_vault_secret.tenant_id: Reading...
data.azurerm_key_vault_secret.app_id: Reading...
data.azurerm_key_vault_secret.subscription_id: Reading...
data.azurerm_key_vault_secret.password: Reading...
data.azurerm_key_vault_secret.app_id: Read complete after 1s [id=https://azurecredentials.vault.azure.net/secrets/clientid/405b538e7ef54b4f9d04e0c6eaa740c7]
data.azurerm_key_vault_secret.tenant_id: Read complete after 1s [id=https://azurecredentials.vault.azure.net/secrets/tenantid/d844d71f699a4f1388e61f1531912957]
data.azurerm_key_vault_secret.subscription_id: Read complete after 1s [id=https://azurecredentials.vault.azure.net/secrets/subscriptionid/f0aa9b562a134d39b1e66db4be978843]
data.azurerm_key_vault_secret.password: Read complete after 1s [id=https://azurecredentials.vault.azure.net/secrets/clientsecret/e0643c106eb248dfbf2a87cad50821b8]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # azurerm_linux_virtual_machine.my_terraform_vm will be created
  + resource "azurerm_linux_virtual_machine" "my_terraform_vm" {
      + admin_username                  = "task6-user"
      + allow_extension_operations      = true
      + computer_name                   = (known after apply)
      + disable_password_authentication = true
      + extensions_time_budget          = "PT1H30M"
      + id                              = (known after apply)
      + location                        = "centralindia"
      + max_bid_price                   = -1
      + name                            = "task6-vm"
      + network_interface_ids           = (known after apply)
      + patch_mode                      = "ImageDefault"
      + platform_fault_domain           = -1
      + priority                        = "Regular"
      + private_ip_address              = (known after apply)
      + private_ip_addresses            = (known after apply)
      + provision_vm_agent              = true
      + public_ip_address               = (known after apply)
      + public_ip_addresses             = (known after apply)
      + resource_group_name             = "rg6"
      + size                            = "Standard_DS1_v2"
      + virtual_machine_id              = (known after apply)
      + zone                            = (known after apply)

      + admin_ssh_key {
          + public_key = (known after apply)
          + username   = "task6-user"
        }

      + os_disk {
          + caching                   = "ReadWrite"
          + disk_size_gb              = (known after apply)
          + name                      = "task6-osdisk"
          + storage_account_type      = "Standard_LRS"
          + write_accelerator_enabled = false
        }

      + source_image_reference {
          + offer     = "0001-com-ubuntu-server-jammy"
          + publisher = "Canonical"
          + sku       = "22_04-lts-gen2"
          + version   = "latest"
        }
    }

  # azurerm_network_interface.my_terraform_nic will be created
  + resource "azurerm_network_interface" "my_terraform_nic" {
      + applied_dns_servers           = (known after apply)
      + dns_servers                   = (known after apply)
      + enable_accelerated_networking = false
      + enable_ip_forwarding          = false
      + id                            = (known after apply)
      + internal_dns_name_label       = (known after apply)
      + internal_domain_name_suffix   = (known after apply)
      + location                      = "centralindia"
      + mac_address                   = (known after apply)
      + name                          = "task6-nic"
      + private_ip_address            = (known after apply)
      + private_ip_addresses          = (known after apply)
      + resource_group_name           = "rg6"
      + virtual_machine_id            = (known after apply)

      + ip_configuration {
          + gateway_load_balancer_frontend_ip_configuration_id = (known after apply)
          + name                                               = "task6-ipconfig"
          + primary                                            = (known after apply)
          + private_ip_address                                 = (known after apply)
          + private_ip_address_allocation                      = "Dynamic"
          + private_ip_address_version                         = "IPv4"
          + public_ip_address_id                               = (known after apply)
          + subnet_id                                          = (known after apply)
        }
    }

  # azurerm_network_interface_security_group_association.example will be created
  + resource "azurerm_network_interface_security_group_association" "example" {
      + id                        = (known after apply)
      + network_interface_id      = (known after apply)
      + network_security_group_id = (known after apply)
    }

  # azurerm_network_security_group.my_terraform_nsg will be created
  + resource "azurerm_network_security_group" "my_terraform_nsg" {
      + id                  = (known after apply)
      + location            = "centralindia"
      + name                = "task6-nsg"
      + resource_group_name = "rg6"
      + security_rule       = [
          + {
              + access                                     = "Allow"
              + description                                = ""
              + destination_address_prefix                 = "*"
              + destination_address_prefixes               = []
              + destination_application_security_group_ids = []
              + destination_port_range                     = "22"
              + destination_port_ranges                    = []
              + direction                                  = "Inbound"
              + name                                       = "SSH"
              + priority                                   = 1001
              + protocol                                   = "Tcp"
              + source_address_prefix                      = "*"
              + source_address_prefixes                    = []
              + source_application_security_group_ids      = []
              + source_port_range                          = "*"
              + source_port_ranges                         = []
            },
        ]
    }

  # azurerm_public_ip.my_terraform_public_ip will be created
  + resource "azurerm_public_ip" "my_terraform_public_ip" {
      + allocation_method       = "Dynamic"
      + availability_zone       = (known after apply)
      + fqdn                    = (known after apply)
      + id                      = (known after apply)
      + idle_timeout_in_minutes = 4
      + ip_address              = (known after apply)
      + ip_version              = "IPv4"
      + location                = "centralindia"
      + name                    = "task6-pip"
      + resource_group_name     = "rg6"
      + sku                     = "Basic"
      + sku_tier                = "Regional"
      + zones                   = (known after apply)
    }

  # azurerm_subnet.my_terraform_subnet will be created
  + resource "azurerm_subnet" "my_terraform_subnet" {
      + address_prefix                                 = (known after apply)
      + address_prefixes                               = [
          + "10.0.1.0/24",
        ]
      + enforce_private_link_endpoint_network_policies = false
      + enforce_private_link_service_network_policies  = false
      + id                                             = (known after apply)
      + name                                           = "task6-subnet"
      + resource_group_name                            = "rg6"
      + virtual_network_name                           = "task6-vnet"
    }

  # azurerm_virtual_network.my_terraform_network will be created
  + resource "azurerm_virtual_network" "my_terraform_network" {
      + address_space         = [
          + "10.0.0.0/16",
        ]
      + dns_servers           = (known after apply)
      + guid                  = (known after apply)
      + id                    = (known after apply)
      + location              = "centralindia"
      + name                  = "task6-vnet"
      + resource_group_name   = "rg6"
      + subnet                = (known after apply)
      + vm_protection_enabled = false
    }

  # tls_private_key.example_ssh will be created
  + resource "tls_private_key" "example_ssh" {
      + algorithm                     = "RSA"
      + ecdsa_curve                   = "P224"
      + id                            = (known after apply)
      + private_key_openssh           = (sensitive value)
      + private_key_pem               = (sensitive value)
      + private_key_pem_pkcs8         = (sensitive value)
      + public_key_fingerprint_md5    = (known after apply)
      + public_key_fingerprint_sha256 = (known after apply)
      + public_key_openssh            = (known after apply)
      + public_key_pem                = (known after apply)
      + rsa_bits                      = 4096
    }

Plan: 8 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + public_ip_address   = (known after apply)
  + resource_group_name = "rg6"
  + tls_private_key     = (sensitive value)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

tls_private_key.example_ssh: Creating...
azurerm_virtual_network.my_terraform_network: Creating...
azurerm_public_ip.my_terraform_public_ip: Creating...
azurerm_network_security_group.my_terraform_nsg: Creating...
tls_private_key.example_ssh: Still creating... [10s elapsed]
azurerm_public_ip.my_terraform_public_ip: Creation complete after 2s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/publicIPAddresses/task6-pip]
azurerm_network_security_group.my_terraform_nsg: Creation complete after 2s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/networkSecurityGroups/task6-nsg]
azurerm_virtual_network.my_terraform_network: Creation complete after 5s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/virtualNetworks/task6-vnet]
azurerm_subnet.my_terraform_subnet: Creating...
azurerm_subnet.my_terraform_subnet: Creation complete after 5s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/virtualNetworks/task6-vnet/subnets/task6-subnet]
azurerm_network_interface.my_terraform_nic: Creating...
tls_private_key.example_ssh: Still creating... [20s elapsed]
azurerm_network_interface.my_terraform_nic: Creation complete after 2s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/networkInterfaces/task6-nic]
azurerm_network_interface_security_group_association.example: Creating...
tls_private_key.example_ssh: Creation complete after 23s [id=4a05ef8e2efa82aedfb95ba0e8ce384137e2b88a]
azurerm_linux_virtual_machine.my_terraform_vm: Creating...
azurerm_network_interface_security_group_association.example: Creation complete after 5s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/networkInterfaces/task6-nic|/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Network/networkSecurityGroups/task6-nsg]
azurerm_linux_virtual_machine.my_terraform_vm: Still creating... [10s elapsed]
azurerm_linux_virtual_machine.my_terraform_vm: Still creating... [20s elapsed]
azurerm_linux_virtual_machine.my_terraform_vm: Still creating... [30s elapsed]
azurerm_linux_virtual_machine.my_terraform_vm: Still creating... [40s elapsed]
azurerm_linux_virtual_machine.my_terraform_vm: Creation complete after 49s [id=/subscriptions/f9182f0c-787c-49f3-b5e0-dda139de3996/resourceGroups/rg6/providers/Microsoft.Compute/virtualMachines/task6-vm]

Apply complete! Resources: 8 added, 0 changed, 0 destroyed.

Outputs:

public_ip_address = "20.235.89.22"
resource_group_name = "rg6"
tls_private_key = <sensitive>

```
</details>

#### 4. Get the private key

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\task6> terraform output -raw tls_private_key > key2 ```

``` PS C:\Users\91887\Desktop\AZ-104\devops45days-challenge\day5\task6> ssh -i .\key2 task6-user@20.235.89.22 ```

Reference: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret
https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-windows-powershell?tabs=bash#create-a-service-principal
