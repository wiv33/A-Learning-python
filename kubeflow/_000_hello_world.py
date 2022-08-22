import kfp
from kfp import dsl
import pprint

BASE_IMAGE = 'library/bash:4.4.23'
KUBEFLOW_HOST = "http://192.168.64.12:31380/pipeline"


def echo_op():
    pprint.pprint(locals())
    pass


echo_op()

