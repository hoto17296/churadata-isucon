from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct


class ChuradataIsuconStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            "ChuraDATA-ISUCON",
            cidr="192.168.0.0/16",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC),
            ],
        )
