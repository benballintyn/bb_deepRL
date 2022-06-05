import numpy as np

def conv2d_input_output_converter(Nh, Nw, Fh, Fw, p, s):
    Oh = (Nh - Fh + 2*p)/s + 1
    Ow = (Nw - Fw + 2*p)/s + 1
    return (Oh, Ow)
