# global
import jax
import jax.numpy as jnp

# local
from ivy.functional.backends.jax import JaxArray


def bitwise_invert(x: JaxArray)\
        -> JaxArray:
    return jnp.bitwise_not(x)


def bitwise_and(x1: JaxArray,
                x2: JaxArray)\
        -> JaxArray:
    return jnp.bitwise_and(x1, x2)


def ceil(x: JaxArray)\
        -> JaxArray:
    if 'int' in str(x.dtype):
        return x
    return jnp.ceil(x)


def floor(x: JaxArray)\
        -> JaxArray:
    if 'int' in str(x.dtype):
        return x
    return jnp.floor(x)


def isfinite(x: JaxArray)\
        -> JaxArray:
    return jnp.isfinite(x)

  
def asin(x: JaxArray)\
        -> JaxArray:
    return jnp.arcsin(x)
  

def isinf(x: JaxArray)\
        -> JaxArray:
    return jnp.isinf(x)


def equal(x1: JaxArray, x2: JaxArray)\
        -> JaxArray:
    return x1 == x2


def greater_equal(x1: JaxArray, x2: JaxArray)\
        -> JaxArray:
    return jnp.greater_equal(x1, x2)


def less_equal(x1: JaxArray, x2: JaxArray)\
        -> JaxArray:
    return x1 <= x2


def asinh(x: JaxArray)\
        -> JaxArray:
    return jnp.arcsinh(x)


def sqrt(x: JaxArray)\
        -> JaxArray:
    return jnp.sqrt(x)


def cosh(x: JaxArray)\
        -> JaxArray:
    return jnp.cosh(x)


def log10(x: JaxArray)\
        -> JaxArray:
    return jnp.log10(x)


def log2(x: JaxArray)\
        -> JaxArray:
    return jnp.log2(x)


def log1p(x: JaxArray)\
        -> JaxArray:
    return jnp.log1p(x)


def isnan(x: JaxArray)\
        -> JaxArray:
    return jnp.isnan(x)


def less(x1: JaxArray,x2:JaxArray)\
        -> JaxArray:
    return jnp.less(x1,x2)


def cos(x: JaxArray)\
        -> JaxArray:
    return jnp.cos(x)


def logical_or(x1: JaxArray, x2: JaxArray)\
        -> JaxArray:
    return jnp.logical_or(x1, x2)


def logical_and(x1: JaxArray, x2: JaxArray)\
        -> JaxArray:
    return jnp.logical_and(x1, x2)


def logical_not(x: JaxArray)\
        -> JaxArray:
    return jnp.logical_not(x)


def acos(x: JaxArray)\
        -> JaxArray:
    return jnp.arccos(x)


def acosh(x: JaxArray)\
        -> JaxArray:
    return jnp.arccosh(x)

  
def sin(x: JaxArray)\
        -> JaxArray:
    return jnp.sin(x)


def negative(x: JaxArray) -> JaxArray:
    return jnp.negative(x)


def not_equal(x1: JaxArray, x2: JaxArray)\
        -> JaxArray:
    return jnp.not_equal(x1, x2)


def tanh(x: JaxArray)\
        -> JaxArray:
    return jnp.tanh(x)


def bitwise_or(x1: JaxArray, x2: JaxArray) -> JaxArray:
    return jnp.bitwise_or(x1, x2)


def sinh(x: JaxArray)\
        -> JaxArray:
    return jnp.sinh(x)


def positive(x: JaxArray)\
        -> JaxArray:
    return jnp.positive(x)

    
def square(x: JaxArray) \
        -> JaxArray:
    return jnp.square(x)


def round(x: JaxArray)\
        -> JaxArray:
    if 'int' in str(x.dtype):
        return x
    return jnp.round(x)


def abs(x: JaxArray)\
        -> JaxArray:
    return jnp.absolute(x)


def logaddexp(x1: JaxArray, x2: JaxArray) -> JaxArray:
    return jnp.logaddexp(x1, x2)


tan = jnp.tan
atan = jnp.arctan
atan2 = jnp.arctan2
cosh = jnp.cosh
atanh = jnp.arctanh
log = jnp.log
exp = jnp.exp


# Extra #
# ------#


erf = jax.scipy.special.erf