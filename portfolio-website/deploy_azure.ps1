# Azure Deployment Script for Portfolio Website
# Make sure you have Azure CLI installed and logged in

# Variables
$resourceGroup = "arpitpal-portfolio-rg"
$location = "eastus"
$appServicePlan = "arpitpal-portfolio-plan"
$webAppName = "arpitpal-portfolio"

# Create Resource Group
Write-Host "Creating Resource Group..."
az group create --name $resourceGroup --location $location

# Create App Service Plan
Write-Host "Creating App Service Plan..."
az appservice plan create --name $appServicePlan --resource-group $resourceGroup --sku B1 --is-linux

# Create Web App
Write-Host "Creating Web App..."
az webapp create --name $webAppName --resource-group $resourceGroup --plan $appServicePlan --runtime "PYTHON|3.9"

# Configure deployment settings
Write-Host "Configuring deployment settings..."
az webapp config appsettings set --name $webAppName --resource-group $resourceGroup --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true FLASK_APP=frontend/app.py

# Deploy the code
Write-Host "Deploying code..."
az webapp up --name $webAppName --resource-group $resourceGroup --sku B1 --location $location

Write-Host "Deployment completed! Your website is available at: https://$webAppName.azurewebsites.net" 