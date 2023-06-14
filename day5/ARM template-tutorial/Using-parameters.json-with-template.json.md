- Parameter files are JSON files with a structure that's similar to your template. In the file, you provide the parameter values you want to pass in during deployment.
- Within the parameter file, you provide values for the parameters in your template. The name of each parameter in your parameter file needs to match the name of a parameter in your template. The name is case-insensitive but to easily see the matching values we recommend that you match the casing from the template.
- You don't have to provide a value for every parameter. If an unspecified parameter has a default value, that value is used during deployment. If a parameter doesn't have a default value and isn't specified in the parameter file, you're prompted to provide a value during deployment.
- You can't specify a parameter name in your parameter file that doesn't match a parameter name in the template. You get an error when you provide unknown parameters

Reference : https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/template-tutorial-use-parameter-file?tabs=azure-cli
