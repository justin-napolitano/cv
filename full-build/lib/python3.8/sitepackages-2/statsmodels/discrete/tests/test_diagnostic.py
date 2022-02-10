# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:38:13 2017

Author: Josef Perktold
"""

import numpy as np
from numpy.testing import assert_allclose
import pytest

from statsmodels.discrete.discrete_model import Poisson
import statsmodels.discrete._diagnostics_count as dia


class TestCountDiagnostic(object):

    @classmethod
    def setup_class(cls):

        expected_params = [1, 1, 0.5]
        np.random.seed(987123)
        nobs = 500
        exog = np.ones((nobs, 2))
        exog[:nobs//2, 1] = 0
        # offset is used to create misspecification of the model
        # for predicted probabilities conditional moment test
        #offset = 0.5 * np.random.randn(nobs)
        #range_mix = 0.5
        #offset = -range_mix / 2 + range_mix * np.random.rand(nobs)
        offset = 0
        mu_true = np.exp(exog.dot(expected_params[:-1]) + offset)

        endog_poi = np.random.poisson(mu_true / 5)
        # endog3 = distr.zigenpoisson.rvs(mu_true, 0,
        #                                2, 0.01, size=mu_true.shape)

        model_poi = Poisson(endog_poi, exog)
        res_poi = model_poi.fit(method='bfgs', maxiter=5000)
        cls.exog = exog
        cls.endog = endog_poi
        cls.res = res_poi
        cls.nobs = nobs

    def test_count(self):
        # partially smoke
        tzi1 = dia.test_poisson_zeroinflation(self.res)

        tzi2 = dia.test_poisson_zeroinflation_brock(self.res)
        # compare two implementation in special case
        assert_allclose(tzi1[:2], (tzi2[0]**2, tzi2[1]), rtol=1e-5)

        tzi3 = dia.test_poisson_zeroinflation(self.res, self.exog)

        # regression test
        tzi3_1 = (0.79863597832443878, 0.67077736750318928, 2, 2)
        assert_allclose(tzi3, tzi3_1, rtol=5e-4)

    @pytest.mark.matplotlib
    def test_probs(self, close_figures):
        nobs = self.nobs
        probs = self.res.predict_prob()
        freq = np.bincount(self.endog) / nobs

        tzi = dia.test_chisquare_prob(self.res, probs[:, :2])
        # regression numbers
        tzi1 = (0.387770845, 0.5334734738)
        assert_allclose(tzi[:2], tzi1, rtol=5e-5)

        # smoke test for plot
        dia.plot_probs(freq, probs.mean(0))
