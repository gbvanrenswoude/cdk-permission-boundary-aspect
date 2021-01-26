from aws_cdk import (
    aws_s3 as s3, core, aws_lambda, aws_ec2 as ec2, aws_iam, aws_s3_notifications, aws_events, aws_events_targets,
    aws_sns, aws_lambda_event_sources)
from custom-aspects import PermissionBoundaryAspect



class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        self.node.apply_aspect(
            PermissionBoundaryAspect(
                f'arn:aws:iam::{core.Aws.ACCOUNT_ID}:policy/a-boundary'
            )
        )
