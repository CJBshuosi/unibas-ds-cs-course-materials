import numpy as np
import matplotlib.pyplot as plt


def exp_cdf(x, l):
    """
    Value of the exponential cumulative distribution function for the provided values of x and lambda.
    """
    raise NotImplementedError("Implement the exp_cdf function")


def exp_quantile(p, l):
    """
    Value of the exponential quantile function for the provided values of x and lambda.
    """
    raise NotImplementedError("Implement the exp_quantile function")


def inverse_cdf_sampling(n, l, rng=None):
    """
    Implements the inverse CDF sampling by drawing n uniform numbers and then applying the inverse CDF.
    """
    if rng is None:
        rng = np.random.default_rng()

    raise NotImplementedError("Implement the inverse_cdf_sampling function")


def plot_inverse_cdf(n, l):
    x, u = inverse_cdf_sampling(n, l)
    x_theory = np.linspace(0, max(x), 1000)
    y = exp_cdf(x_theory, l)

    plt.figure(figsize=(10, 6))
    plt.plot(x_theory, y, "r-", label="True CDF", zorder=1)
    plt.scatter(x, u, s=12, alpha=0.5, label="Inverse CDF samples", zorder=2)

    plt.legend()


if __name__=="__main__":
    plot_inverse_cdf(n=100, l=1.)
    plt.show()


