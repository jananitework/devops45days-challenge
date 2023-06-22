variable "resource_group_location" {
  type        = string
  description = "Location of the resource group."
}

variable "resource_group_name" {
  type        = string
  description = "Resource group name under which Azure resources will be grouped"
}

variable "vnet_cidr" {
  description = "VNET CIDR"
  type        = string
}

variable "subnet_cidr" {
  description = "Subnet CIDR"
  type        = string
}

variable "vm_name" {
  type        = string
  description = "The name of the Linux Virtual Machine"
}

variable "username" {
  type        = string
  description = "The username of the local administrator used for the Virtual Machine"
}

variable "storage_account_name" {
  type        = string
  description = "storage account to store the tf state files"
}

variable "container_name" {
  type        = string
  description = "Storage account container name"
}