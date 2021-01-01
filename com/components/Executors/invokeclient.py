from troposphere import Template, Ref
from com.components.ec2.EC2Creator import EC2Util
from com.components.sg.SGTemplateCreator import SGUtil
from com.components.cloudformation.cloudformation import CloudFormationResource
import json

t = Template()

sgUtil = SGUtil("EC2SGName")
sgTemplate = sgUtil.get_security_group_object()
t.add_resource(sgTemplate)

ec2Util = EC2Util("SampleEC2Instance", "ami-026669ec456129a70", "t2.micro", "ap-south-1")
ec2InstanceTemplate = ec2Util.get_ec2_instance_object()
ec2InstanceTemplate.SecurityGroups = [Ref(sgTemplate)]
t.add_resource(ec2InstanceTemplate)

cftData = json.loads(t.to_json())

cloud_formation_object = CloudFormationResource("ap-south-1")
cloud_formation_object.create_cloud_formation_stack(stack_name="sample-ec2-stack", template_body=cftData)
# cloud_formation_object.destroy_cloud_formation_stack(stack_name="sample-ec2-stack")
