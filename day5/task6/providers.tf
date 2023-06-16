terraform {
  required_version = ">=0.12"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>2.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.0"
    }
    tls = {
      source = "hashicorp/tls"
      version = "~>4.0"
    }
  }
}

data "azurerm_key_vault" "keyvault" {
  name                = "azurecredentials"
  resource_group_name = var.resource_group_name
}

data "azurerm_key_vault_secret" "app_id" {
  name         = "clientid"
  key_vault_id = data.azurerm_key_vault.keyvault.id
}

data "azurerm_key_vault_secret" "password" {
  name         = "clientsecret"
  key_vault_id = data.azurerm_key_vault.keyvault.id
}

data "azurerm_key_vault_secret" "tenant_id" {
  name         = "tenantid"
  key_vault_id = data.azurerm_key_vault.keyvault.id
}

data "azurerm_key_vault_secret" "subscription_id" {
  name         = "subscriptionid"
  key_vault_id = data.azurerm_key_vault.keyvault.id
}


provider "azurerm" {
  features {}

  subscription_id   = "f9182f0c-787c-49f3-b5e0-dda139de3996"
  tenant_id         = "14347c6c-c7da-4f47-a3eb-89e0ac0d8850"
  client_id         = "0f57c09a-58a5-4be3-a6be-1fcac92535fc"
  client_secret     = "Syq8Q~RsG54Z_G3PPjnSxdysBMA-akKa0xKaXcGa"
}