import sys
sys.path.insert(1, "../../../")
import h2o
import numpy as np
import random
import math
import scipy.special

def expr_math_ops(ip,port):
    # Connect to h2o
    h2o.init(ip,port)

    sin_cos_tan_atan_sinh_cosh_tanh_asinh_data = [[random.uniform(-10,10) for r in range(10)] for c in range(10)]
    asin_acos_atanh_data = [[random.uniform(-1,1) for r in range(10)] for c in range(10)]
    acosh_data = [[random.uniform(1,10) for r in range(10)] for c in range(10)]
    abs_data = [[random.uniform(-100000,0) for r in range(10)] for c in range(10)]

    h2o_data1_1 = h2o.H2OFrame(python_obj=sin_cos_tan_atan_sinh_cosh_tanh_asinh_data)
    h2o_data2_1 = h2o.H2OFrame(python_obj=asin_acos_atanh_data)
    h2o_data3_1 = h2o.H2OFrame(python_obj=acosh_data)
    h2o_data4_1 = h2o.H2OFrame(python_obj=abs_data)

    np_data1 = np.array(sin_cos_tan_atan_sinh_cosh_tanh_asinh_data)
    np_data2 = np.array(asin_acos_atanh_data)
    np_data3 = np.array(acosh_data)
    np_data4 = np.array(abs_data)

    h2o_data1 = h2o_data1_1 + 2
    h2o_data2 = h2o_data2_1 / 1.01
    h2o_data3 = h2o_data3_1 * 1.5
    h2o_data4 = h2o_data4_1 - 1.5

    np_data1 = np_data1 + 2
    np_data2 = np_data2 / 1.01
    np_data3 = np_data3 * 1.5
    np_data4 = np_data4 - 1.5

    h2o.np_comparison_check(h2o.cos(h2o_data1), np.cos(np_data1), 10)
    h2o.np_comparison_check(h2o.sin(h2o_data1), np.sin(np_data1), 10)
    h2o.np_comparison_check(h2o.tan(h2o_data1), np.tan(np_data1), 10)
    h2o.np_comparison_check(h2o.acos(h2o_data2), np.arccos(np_data2), 10)
    h2o.np_comparison_check(h2o.asin(h2o_data2), np.arcsin(np_data2), 10)
    h2o.np_comparison_check(h2o.atan(h2o_data1), np.arctan(np_data1), 10)
    h2o.np_comparison_check(h2o.cosh(h2o_data1), np.cosh(np_data1), 10)
    h2o.np_comparison_check(h2o.sinh(h2o_data1), np.sinh(np_data1), 10)
    h2o.np_comparison_check(h2o.tanh(h2o_data1), np.tanh(np_data1), 10)
    h2o.np_comparison_check(h2o.acosh(h2o_data3), np.arccosh(np_data3), 10)
    h2o.np_comparison_check(h2o.asinh(h2o_data1), np.arcsinh(np_data1), 10)
    h2o.np_comparison_check(h2o.atanh(h2o_data2), np.arctanh(np_data2), 10)
    h2o.np_comparison_check(h2o.cospi(h2o_data2/math.pi), np.cos(np_data2), 10)
    h2o.np_comparison_check(h2o.sinpi(h2o_data2/math.pi), np.sin(np_data2), 10)
    h2o.np_comparison_check(h2o.tanpi(h2o_data2/math.pi), np.tan(np_data2), 10)
    h2o.np_comparison_check(h2o.abs(h2o_data4), np.fabs(np_data4), 10)
    h2o.np_comparison_check(h2o.sign(h2o_data2), np.sign(np_data2), 10)
    h2o.np_comparison_check(h2o.sqrt(h2o_data3), np.sqrt(np_data3), 10)
    h2o.np_comparison_check(h2o.trunc(h2o_data3), np.trunc(np_data3), 10)
    h2o.np_comparison_check(h2o.ceil(h2o_data3), np.ceil(np_data3), 10)
    h2o.np_comparison_check(h2o.floor(h2o_data3), np.floor(np_data3), 10)
    h2o.np_comparison_check(h2o.log(h2o_data3), np.log(np_data3), 10)
    h2o.np_comparison_check(h2o.log10(h2o_data3), np.log10(np_data3), 10)
    h2o.np_comparison_check(h2o.log1p(h2o_data3), np.log1p(np_data3), 10)
    h2o.np_comparison_check(h2o.log2(h2o_data3), np.log2(np_data3), 10)
    h2o.np_comparison_check(h2o.exp(h2o_data3), np.exp(np_data3), 10)
    h2o.np_comparison_check(h2o.expm1(h2o_data3), np.expm1(np_data3), 10)
    h2o_val = h2o.gamma(h2o_data3)[5,5]
    num_val = math.gamma(h2o_data3[5,5])
    assert abs(h2o_val - num_val) < max(abs(h2o_val), abs(num_val)) * 1e-6, \
        "check unsuccessful! h2o computed {0} and math computed {1}. expected equal gamma values between h2o and " \
        "math".format(h2o_val,num_val)
    h2o_val = h2o.lgamma(h2o_data3)[5,5]
    num_val = math.lgamma(h2o_data3[5,5])
    assert abs(h2o_val - num_val) < max(abs(h2o_val), abs(num_val)) * 1e-6, \
        "check unsuccessful! h2o computed {0} and math computed {1}. expected equal lgamma values between h2o and " \
        "math".\
            format(h2o_val,num_val)
    h2o_val = h2o.digamma(h2o_data3)[5,5]
    num_val = scipy.special.polygamma(0,h2o_data3[5,5])
    assert abs(h2o_val - num_val) < max(abs(h2o_val), abs(num_val)) * 1e-6, \
        "check unsuccessful! h2o computed {0} and math computed {1}. expected equal digamma values between h2o and " \
        "math"\
            .format(h2o_val,num_val)
    h2o_val = h2o.trigamma(h2o_data3)[5,5]
    num_val = scipy.special.polygamma(1,h2o_data3[5,5])
    assert abs(h2o_val - num_val) < max(abs(h2o_val), abs(num_val)) * 1e-6, \
        "check unsuccessful! h2o computed {0} and math computed {1}. expected equal trigamma values between h2o and " \
        "math".format(h2o_val,num_val)

if __name__ == "__main__":
    h2o.run_test(sys.argv, expr_math_ops)
