#!/usr/bin/env python3

from aws_cdk import core
from stack import MyStack

env_EU = core.Environment(account="zzz", region="eu-central-1")
app = core.App()

MyStack(app, "randomname",env = env_EU)

app.synth()
