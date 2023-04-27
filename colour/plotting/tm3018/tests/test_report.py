# !/usr/bin/env python
"""Define the unit tests for the :mod:`colour.plotting.tm3018.report` module."""

import os
import unittest
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.pyplot import Axes, Figure
import numpy as np

from colour.colorimetry import SDS_ILLUMINANTS
from colour.io.image import read_image
from colour.plotting.tm3018.report import (
    plot_single_sd_colour_rendition_report_full,
    plot_single_sd_colour_rendition_report_intermediate,
    plot_single_sd_colour_rendition_report_simple,
    plot_single_sd_colour_rendition_report,
)
from colour.utilities.array import as_array

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "TestPlotSingleSdColourRenditionReportFull",
    "TestPlotSingleSdColourRenditionReportIntermediate",
    "TestPlotSingleSdColourRenditionReportSimple",
    "TestPlotSingleSdColourRenditionReport",
]


class TestPlotSingleSdColourRenditionReportFull(unittest.TestCase):
    """
    Define :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report_full` definition unit tests methods.
    """

    def test_plot_single_sd_colour_rendition_report_full(self):
        """
        Test :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report_full` definition.
        """

        figure, axes = plot_single_sd_colour_rendition_report_full(
            SDS_ILLUMINANTS["FL2"]
        )

        self.assertIsInstance(figure, Figure)
        self.assertIsInstance(axes, Axes)


class TestPlotSingleSdColourRenditionReportIntermediate(unittest.TestCase):
    """
    Define :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report_intermediate` definition unit tests
    methods.
    """

    def test_plot_single_sd_colour_rendition_report_intermediate(self):
        """
        Test :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report_intermediate` definition.
        """

        figure, axes = plot_single_sd_colour_rendition_report_intermediate(
            SDS_ILLUMINANTS["FL2"]
        )

        self.assertIsInstance(figure, Figure)
        self.assertIsInstance(axes, Axes)


class TestPlotSingleSdColourRenditionReportSimple(unittest.TestCase):
    """
    Define :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report_simple` definition unit tests methods.
    """

    def test_plot_color_vector_graphic(self):
        """
        Test :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report_simple` definition.
        """

        figure, axes = plot_single_sd_colour_rendition_report_simple(
            SDS_ILLUMINANTS["FL2"]
        )

        self.assertIsInstance(figure, Figure)
        self.assertIsInstance(axes, Axes)


class TestPlotSingleSdColourRenditionReport(unittest.TestCase):
    """
    Define :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report` definition unit tests methods.
    """

    def test_plot_single_sd_colour_rendition_report(self):
        """
        Test :func:`colour.plotting.tm3018.report.\
plot_single_sd_colour_rendition_report` definition.
        """

        figure, axes = plot_single_sd_colour_rendition_report(
            SDS_ILLUMINANTS["FL2"]
        )
        self.assertIsInstance(figure, Figure)
        self.assertIsInstance(axes, Axes)

        canvas = FigureCanvasAgg(figure)
        canvas.draw()

        test_img = as_array(canvas.buffer_rgba()) / 255

        ROOT_RESOURCES: str = os.path.join(
            os.path.dirname(__file__), "resources"
        )

        ref_image_path = os.path.join(
            ROOT_RESOURCES, "TM30_Report_Example.png"
        )
        ref_image = read_image(ref_image_path)

        np.testing.assert_allclose(
            ref_image,
            test_img,
            err_msg="TM30 Report Image Changed",
            atol=1 / 255,
            rtol=0,
        )


if __name__ == "__main__":
    unittest.main()
