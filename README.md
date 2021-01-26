# cdk-permission-boundary-aspect

Some IAM roles automatically created by AWS CDK are notoriously hard to reach when your corp requires you to add a permissions boundary to them. If you want to add a permission boundary to them globally, CDK does not natively support that (at the time of writing).
This custom aspect (thought up by josef.stach in github issue https://github.com/aws/aws-cdk/issues/3242) provides that functionality for you. 

In this repo it is implemented at the Stack level instead of at the App level. This allows for adding a permissionsboundary to every IAM:Role created in the stack in where it is used, even if AWS CDK generates these roles for you.
