import matplotlib.pyplot as plt



def traceplot(chain, parameter_names=None):

    n_params = chain.shape[1]

    if parameter_names is None:
        parameter_names = [f"param_{i}" for i in range(n_params)]

    fig, axes = plt.subplots(n_params, 1, figsize=(10, 2.5*n_params))

    if n_params == 1:
        axes = [axes]

    for i in range(n_params):
        axes[i].plot(chain[:, i], lw=0.5)
        axes[i].set_title(parameter_names[i])

    plt.tight_layout()
    plt.show()
