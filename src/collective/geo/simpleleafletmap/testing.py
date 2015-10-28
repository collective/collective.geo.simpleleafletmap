# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.geo.simpleleafletmap


class CollectiveGeoSimpleleafletmapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.geo.simpleleafletmap,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geo.simpleleafletmap:default')


COLLECTIVE_GEO_SIMPLELEAFLETMAP_FIXTURE = CollectiveGeoSimpleleafletmapLayer()


COLLECTIVE_GEO_SIMPLELEAFLETMAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEO_SIMPLELEAFLETMAP_FIXTURE,),
    name='CollectiveGeoSimpleleafletmapLayer:IntegrationTesting'
)


COLLECTIVE_GEO_SIMPLELEAFLETMAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GEO_SIMPLELEAFLETMAP_FIXTURE,),
    name='CollectiveGeoSimpleleafletmapLayer:FunctionalTesting'
)


COLLECTIVE_GEO_SIMPLELEAFLETMAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_GEO_SIMPLELEAFLETMAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveGeoSimpleleafletmapLayer:AcceptanceTesting'
)
