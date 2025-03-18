#!/bin/bash
# Azure Deployment Script for Portfolio Website
# Make sure you have Azure CLI installed and logged in

# Variables
resourceGroup="arpitpal-portfolio-rg"
location="eastus"
appServicePlan="arpitpal-portfolio-plan"
webAppName="arpitpal-portfolio"

# Create Resource Group
echo "Creating Resource Group..."
az group create --name $resourceGroup --location $location

# Create App Service Plan
echo "Creating App Service Plan..."
az appservice plan create --name $appServicePlan --resource-group $resourceGroup --sku B1 --is-linux

# Create Web App
echo "Creating Web App..."
az webapp create --name $webAppName --resource-group $resourceGroup --plan $appServicePlan --runtime "PYTHON|3.9"

# Configure deployment settings
echo "Configuring deployment settings..."
az webapp config appsettings set --name $webAppName --resource-group $resourceGroup --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true FLASK_APP=frontend/app.py

# Deploy the code
echo "Deploying code..."
az webapp up --name $webAppName --resource-group $resourceGroup --sku B1 --location $location

echo "Deployment completed! Your website is available at: https://$webAppName.azurewebsites.net" 