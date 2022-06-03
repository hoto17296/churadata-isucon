#!/usr/bin/env python3
import os

import aws_cdk as cdk

from churadata_isucon.churadata_isucon_stack import ChuradataIsuconStack


app = cdk.App()
ChuradataIsuconStack(
    app,
    "ChuradataIsuconStack",
    env=cdk.Environment(region="ap-northeast-1"),
)

app.synth()
