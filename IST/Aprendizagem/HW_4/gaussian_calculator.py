from numpy import *
import math
# covariance matrix
sigma = matrix([[0.996, -1.076],
           [-1.076, 1.389]
          ])
# mean vector
mu = array([0.785,0.843])

# input
x = array([3,-1])

def norm_pdf_multivariate(x, mu, sigma):
    size = len(x)
    if size == len(mu) and (size, size) == sigma.shape:
        det = linalg.det(sigma)
        if det == 0:
            raise NameError("The covariance matrix can't be singular")

        norm_const = 1.0/ ( math.pow((2*pi),float(size)/2) * math.pow(det,1.0/2) )
        x_mu = matrix(x - mu)
        inv = sigma.I        
        result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
        return norm_const * result
    else:
        raise NameError("The dimensions of the input don't match")

print(norm_pdf_multivariate(x, mu, sigma))