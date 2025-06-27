az storage account create \
  --name billingarchivestorage \
  --resource-group myRG \
  --location eastus \
  --sku Standard_LRS

az storage container create \
  --name coldrecords \
  --account-name billingarchivestorage \
  --public-access off
