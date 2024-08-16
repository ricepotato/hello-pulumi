import pulumi
import pulumi_aws as aws

vpc_name = "pulumi-vpc"
cidr_block = "10.5.0.0/16"

# 10.5.16.0/20
# 10.5.32.0/20
# 10.5.48.0/20
# 10.5.64.0/20

pub_subnet1_az = "ap-northeast-2a"
pub_subnet1_name = "pulumi-public-subnet1"
pub_subnet1_cidr_block = "10.5.16.0/20"

pub_subnet2_az = "ap-northeast-2b"
pub_subnet2_name = "pulumi-public-subnet2"
pub_subnet2_cidr_block = "10.5.32.0/20"

igw_name = "pulumi-igw"


# Create a VPC
vpc = aws.ec2.Vpc(vpc_name, cidr_block=cidr_block, tags={"Name": vpc_name})

public_subnet1 = aws.ec2.Subnet(
    pub_subnet1_name,
    vpc_id=vpc.id,
    availability_zone=pub_subnet1_az,
    cidr_block=pub_subnet1_cidr_block,
)

public_subnet2 = aws.ec2.Subnet(
    pub_subnet2_name,
    vpc_id=vpc.id,
    availability_zone=pub_subnet2_az,
    cidr_block=pub_subnet2_cidr_block,
)

igw = aws.ec2.InternetGateway(igw_name, vpc_id=vpc.id, tags={"Name": igw_name})

pulumi.export("vpc_id", vpc.id)
pulumi.export("public_subnet_id", public_subnet1.id)
pulumi.export("private_subnet_id", public_subnet2.id)
