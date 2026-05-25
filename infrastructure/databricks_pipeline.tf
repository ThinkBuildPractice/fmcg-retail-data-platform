provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "retail_rg" {
  name     = "retail-data-platform-rg"
  location = "Japan East"
}

resource "azurerm_storage_account" "datalake" {
  name                     = "retaildatalake001"
  resource_group_name      = azurerm_resource_group.retail_rg.name
  location                 = azurerm_resource_group.retail_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
