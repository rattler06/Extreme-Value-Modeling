import numpy as np
import matplotlib.pyplot as plt



def return_level_plot(
    T_emp,
    empirical,
    T_grid,
    mean_level,
    lower,
    upper,
    title="Bayesian GEV Return Level Plot"
):

    plt.figure(figsize=(9, 7))

    plt.scatter(
        T_emp,
        empirical,
        s=50,
        color="steelblue",
        edgecolor="k",
        alpha=0.85,
        label="Observed maxima"
    )

    plt.plot(
        T_grid,
        mean_level,
        "r-",
        lw=3,
        label="Posterior Mean"
    )

    plt.fill_between(
        T_grid,
        lower,
        upper,
        color="red",
        alpha=0.2,
        label="95% Credible Interval"
    )

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Return Period")
    plt.ylabel("Return Level")

    plt.title(title)

    plt.grid(True, which="both", ls="--", alpha=0.7)

    plt.legend()
    plt.tight_layout()
    plt.show()
