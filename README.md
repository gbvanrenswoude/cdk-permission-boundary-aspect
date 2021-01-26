# cdk-permission-boundary-aspect

Some IAM roles automatically created by AWS CDK are notoriously hard to reach when your corp requires you to add a permissions boundary to them. This custom aspect  thought up by josef.stach provides that functionality for you. In this repo it is implemented at the Stack level instead of at the App level. This allows for adding a permissionsboundary to every IAM:Role created in the stack in where it is used, even if AWS CDK generates these roles for you.
