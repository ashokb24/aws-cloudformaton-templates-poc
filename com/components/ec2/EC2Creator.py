from troposphere import ec2, Ref, Template

class EC2Util:
    """
    Author: Ashok Bhadrappa
    Class to create a EC2 instance for a given set of parameters
    """

    def __init__(self, instance_name, ami_id, instance_type, region_name):
        self.instance_name = instance_name
        self.ami_id = ami_id
        self.instance_type = instance_type
        self.region_name = region_name

    def get_ec2_instance_object(self):
        instance = ec2.Instance(self.instance_name)
        instance.ImageId = self.ami_id
        instance.InstanceType = self.instance_type
        return instance


if __name__ == '__main__':
    ec2Util = EC2Util("SampleEC2Instance", "ami-026669ec456129a70", "t2.micro", "ap-south-1")
    t = Template()
    t.add_resource(ec2Util.get_ec2_instance_object())
    print(t.to_json())
