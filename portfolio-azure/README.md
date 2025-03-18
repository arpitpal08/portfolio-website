# Portfolio Website

A simple portfolio website built with Flask.

## Deployment Instructions

### Deploy to Azure

1. Install Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
2. Login to Azure:
   ```
   az login
   ```
3. Create a resource group:
   ```
   az group create --name arpitpal-portfolio-rg --location eastus
   ```
4. Create an App Service plan:
   ```
   az appservice plan create --name arpitpal-portfolio-plan --resource-group arpitpal-portfolio-rg --sku B1 --is-linux
   ```
5. Create a web app:
   ```
   az webapp create --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg --plan arpitpal-portfolio-plan --runtime "PYTHON|3.9"
   ```
6. Deploy the code:
   ```
   az webapp up --name arpitpal-portfolio --resource-group arpitpal-portfolio-rg
   ```

### Deploy to AWS

1. Install AWS CLI: https://aws.amazon.com/cli/
2. Configure AWS credentials:
   ```
   aws configure
   ```
3. Create an Elastic Beanstalk application:
   ```
   aws elasticbeanstalk create-application --application-name arpitpal-portfolio
   ```
4. Create an environment:
   ```
   aws elasticbeanstalk create-environment --application-name arpitpal-portfolio --environment-name arpitpal-portfolio-env --solution-stack-name "64bit Amazon Linux 2 v3.3.10 running Python 3.8" --option-settings file://aws-config.json
   ```
5. Deploy the application:
   ```
   aws elasticbeanstalk create-application-version --application-name arpitpal-portfolio --version-label v1 --source-bundle S3Bucket=elasticbeanstalk-samples-us-east-1,S3Key=portfolio.zip
   aws elasticbeanstalk update-environment --application-name arpitpal-portfolio --environment-name arpitpal-portfolio-env --version-label v1
   ``` 