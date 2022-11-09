## Adding new endpoint's path
When adding new endpoint please add it's path to `upi-prod-config-for-pipelines.json` file
and after successful code review and merge- update `/upi/prod/config-for-pipelines` parameter in AWS SSM Parameter Store (parameter value = the whole content of the `upi-prod-config-for-pipelines.json` file)
The process of updating AWS SSM parameter value is going to be automated soon.
## UPI Deployment
There is no working Gitlab auto deployment process yet,
so after merging changes UPI has to be deployed manually to stage prod.
When you use `serverless deploy` command in `serverless.yml` file there should be `url` parameter set to `false`.
When you use `npx serverless deploy` it should be set to `true` .
This is going to be automated soon; in case of any questions please ask Daniel.