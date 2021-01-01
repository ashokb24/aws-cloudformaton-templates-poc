from troposphere import ec2, Ref, Template


class SGUtil:
    def __init__(self, sg_name):
        self.sg_name = sg_name

    def get_security_group_object(self):
        sg = ec2.SecurityGroup(self.sg_name)
        sg.GroupDescription = "Allow access to MyInstance"
        sg.SecurityGroupIngress = [
            ec2.SecurityGroupRule(
                IpProtocol="tcp",
                FromPort="22",
                ToPort="22",
                CidrIp="0.0.0.0/0",
            )]
        return sg


if __name__ == '__main__':
    sgUtil = SGUtil("SampleSGName")
    t = Template()
    t.add_resource(sgUtil.get_security_group_object())
    print(t.to_json())
