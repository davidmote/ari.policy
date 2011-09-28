from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class ariPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import ari.policy
        xmlconfig.file('configure.zcml', ari.policy, context=configurationContext)
        
        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.PloneFormGen')
    
    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ari.policy:default')

ARI_POLICY_FIXTURE = ariPolicy()
ARI_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(ARI_POLICY_FIXTURE,), name="ari:Integration")
