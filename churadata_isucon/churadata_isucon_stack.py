from os import path
from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct


class ChuradataIsuconStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self,
            id="vpc",
            vpc_name="ChuraDATA ISUCON",
            cidr="192.168.0.0/16",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC),
            ],
        )

        security_group = ec2.SecurityGroup(
            self,
            id="sg",
            vpc=vpc,
            allow_all_outbound=True,
        )
        security_group.add_ingress_rule(
            peer=security_group,
            connection=ec2.Port.all_traffic(),
        )
        security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4(self.node.try_get_context("allowed_cidr")),
            connection=ec2.Port.tcp(22),
        )

        instance_spec = [
            ("bench", "192.168.0.10", "c4.xlarge"),
            # ("app-1", "192.168.0.11", "c5.large"),
            # ("app-2", "192.168.0.12", "c5.large"),
            # ("app-3", "192.168.0.13", "c5.large"),
        ]

        with open(path.dirname(__file__) + "/user_data.yml", "r") as f:
            user_data_template = f.read()

        for (i_name, i_addr, i_type) in instance_spec:
            user_data = ec2.UserData.for_linux(shebang="#cloud-config")
            user_data.add_commands(
                user_data_template.format(
                    i_name=i_name,
                    ssl_cert_url=self.node.try_get_context("ssl_cert_url"),
                )
            )
            ec2.Instance(
                self,
                id=f"ec2-{i_name}",
                instance_name=f"ChuraDATA ISUCON / {i_name}",
                instance_type=ec2.InstanceType(i_type),
                machine_image=ec2.MachineImage.generic_linux({"ap-northeast-1": "ami-0796be4f4814fc3d5"}),
                vpc=vpc,
                security_group=security_group,
                block_devices=[
                    ec2.BlockDevice(
                        device_name="/dev/xvda",
                        volume=ec2.BlockDeviceVolume.ebs(20, volume_type=ec2.EbsDeviceVolumeType.GP3),
                    )
                ],
                key_name=self.node.try_get_context("key_name"),
                private_ip_address=i_addr,
                user_data=user_data,
            )

        # TODO: EIP 指定
