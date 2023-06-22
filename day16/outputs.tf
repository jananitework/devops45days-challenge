output "resource_group_name" {
  value = var.resource_group_name
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.my_terraform_vm.public_ip_address
}

output "tls_private_key" {
  value     = tls_private_key.example_ssh.private_key_pem
  sensitive = true
}

output "state_file_path" {
  value = data.terraform_remote_state.state.outputs
}
