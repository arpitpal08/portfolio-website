# Portfolio Website Deployment Guide

This guide provides step-by-step instructions for deploying the portfolio website to Azure App Service or AWS Elastic Beanstalk.

## Prerequisites

- Git installed on your computer
- Azure CLI or AWS CLI installed (depending on your chosen platform)
- A Microsoft Azure account or AWS account

## Deploying to Microsoft Azure

### 1. Setup Azure CLI

1. Install Azure CLI from: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
2. Open a terminal/command prompt and login to Azure:
   ```
   az login
   ```

### 2. Create Azure Resources

1. Create a resource group:
   ```
   az group create --name arpitpal-portfolio-rg --location eastus
   ```

2. Create an App Service plan:
   ```
   az appservice plan create --name arpitpal-portfolio-plan --resource-group arpitpal-portfolio-rg --sku B1 --is-linux
   ```

3. Create a web app:
   ```
   az webapp create --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg --plan arpitpal-portfolio-plan --runtime "PYTHON|3.9"
   ```

### 3. Configure for Deployment

1. Set up application settings (environment variables):
   ```
   az webapp config appsettings set --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true FLASK_APP=frontend/app.py
   ```

### 4. Deploy Your Code

1. Push your code to GitHub:
   ```
   git add .
   git commit -m "Prepare for Azure deployment"
   git push origin main
   ```

2. Set up deployment from local Git:
   ```
   az webapp deployment source config-local-git --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg
   ```

3. Get the deployment URL:
   ```
   az webapp deployment list-publishing-profiles --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg --query "[?publishMethod=='MSDeploy'].publishUrl" -o tsv
   ```

4. Add the Azure remote to your Git repository:
   ```
   git remote add azure <URL_FROM_PREVIOUS_STEP>
   ```

5. Push to Azure:
   ```
   git push azure main
   ```

6. Alternatively, use Azure CLI to deploy directly:
   ```
   cd portfolio-website
   az webapp up --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg
   ```

### 5. Configure Custom Domain (Optional)

1. Purchase a domain from a domain registrar
2. Add DNS records pointing to your Azure App Service
3. Configure SSL binding in Azure App Service

## Deploying to AWS Elastic Beanstalk

### 1. Install and Configure AWS CLI

1. Install AWS CLI: https://aws.amazon.com/cli/
2. Configure with your AWS credentials:
   ```
   aws configure
   ```

### 2. Install Elastic Beanstalk CLI

1. Install EB CLI:
   ```
   pip install awsebcli
   ```

### 3. Initialize Elastic Beanstalk Application

1. Navigate to your project directory:
   ```
   cd portfolio-website
   ```

2. Initialize EB application:
   ```
   eb init -p python-3.8 arpitpal-portfolio
   ```

3. Create an environment:
   ```
   eb create arpitpal-portfolio-env
   ```

### 4. Deploy Your Application

1. Deploy to Elastic Beanstalk:
   ```
   eb deploy
   ```

2. Open your website:
   ```
   eb open
   ```

## Troubleshooting

### Azure Deployment Issues

- If deployment fails, check the logs:
  ```
  az webapp log tail --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg
  ```

- Ensure your `web.config` file is correctly configured
- Verify that all packages in requirements.txt are compatible with Python 3.9

### AWS Deployment Issues

- Check logs:
  ```
  eb logs
  ```

- Ensure your application works locally before deploying
- Verify environment variables are correctly set in AWS environment

## Maintenance

Once deployed, you can update your website by:

1. Making changes to your code locally
2. Committing changes to Git
3. Pushing to Azure/AWS:
   - For Azure: `git push azure main` or `az webapp up --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg`
   - For AWS: `eb deploy` 