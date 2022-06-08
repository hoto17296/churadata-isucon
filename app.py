#!/usr/bin/env python3

from aws_cdk import App, Environment
from churadata_isucon.churadata_isucon_stack import ChuradataIsuconStack
from context import context

app = App(context=context)

ChuradataIsuconStack(
    app,
    "ChuradataIsuconStack",
    env=Environment(region="ap-northeast-1"),
)

app.synth()
