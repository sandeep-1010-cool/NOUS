import pulumi
import pulumi_aws as aws

config = pulumi.Config()
instance_type = config.require("instanceType")

# Create an EC2 instance using the configuration value
ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[{"name": "name", "values": ["amzn2-ami-hvm-*"]}]
)

instance = aws.ec2.Instance(
    "config-instance",
    instance_type=instance_type,
    ami=ami.id,
    tags={"Name": "ConfigInstance"}
)

pulumi.export("instance_id", instance.id)
