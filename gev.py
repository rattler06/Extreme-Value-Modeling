import numpy as np
        self.proposal_sd_sigma = proposal_sd_sigma
        self.proposal_sd_xi = proposal_sd_xi

        self.random_state = random_state
        self.standardize = standardize

    def _log_likelihood(self, mu, sigma, xi, data):

        if sigma <= 0:
            return -np.inf

        try:
            return np.sum(
                gev.logpdf(data, c=-xi, loc=mu, scale=sigma)
            )
        except:
            return -np.inf

    def _log_prior(self, mu, sigma, xi):

        if sigma <= 0:
            return -np.inf

        lp_mu = -0.5 * (
            (mu - self.prior_mu_mean) / self.prior_mu_sd
        )**2

        lp_sigma = (
            -0.5 * (sigma / self.prior_sigma_sd)**2
            - np.log(self.prior_sigma_sd)
        )

        lp_xi = -0.5 * (
            (xi - self.prior_xi_mean) / self.prior_xi_sd
        )**2

        return lp_mu + lp_sigma + lp_xi

    def _log_posterior(self, mu, sigma, xi, data):

        lp = self._log_prior(mu, sigma, xi)

        if not np.isfinite(lp):
            return -np.inf

        return lp + self._log_likelihood(mu, sigma, xi, data)

    def fit(self, data):

        np.random.seed(self.random_state)

        data = clean_data(data)

        self.data_ = data

        c_mle, loc_mle, scale_mle = gev.fit(data)

        xi_current = -c_mle
        mu_current = loc_mle
        sigma_current = scale_mle

        chain = np.zeros((self.n_iter, 3))

        log_post_current = self._log_posterior(
            mu_current,
            sigma_current,
            xi_current,
            data
        )

        accept = 0

        for i in range(self.n_iter):

            mu_prop = (
                mu_current
                + np.random.normal(0, self.proposal_sd_mu)
            )

            sigma_prop = (
                sigma_current
                + np.random.normal(0, self.proposal_sd_sigma)
            )

            xi_prop = (
                xi_current
                + np.random.normal(0, self.proposal_sd_xi)
            )
        )
