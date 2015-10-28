# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.geo.simpleleafletmap.testing import COLLECTIVE_GEO_SIMPLELEAFLETMAP_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.geo.simpleleafletmap is properly installed."""

    layer = COLLECTIVE_GEO_SIMPLELEAFLETMAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.geo.simpleleafletmap is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.geo.simpleleafletmap'))

    def test_uninstall(self):
        """Test if collective.geo.simpleleafletmap is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.geo.simpleleafletmap'])
        self.assertFalse(self.installer.isProductInstalled('collective.geo.simpleleafletmap'))

    def test_browserlayer(self):
        """Test that ICollectiveGeoSimpleleafletmapLayer is registered."""
        from collective.geo.simpleleafletmap.interfaces import ICollectiveGeoSimpleleafletmapLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveGeoSimpleleafletmapLayer, utils.registered_layers())
