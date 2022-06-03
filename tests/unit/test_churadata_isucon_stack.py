import aws_cdk as core
import aws_cdk.assertions as assertions

from churadata_isucon.churadata_isucon_stack import ChuradataIsuconStack

# example tests. To run these tests, uncomment this file along with the example
# resource in churadata_isucon/churadata_isucon_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ChuradataIsuconStack(app, "churadata-isucon")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
