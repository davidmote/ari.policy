import unittest2 as unittest
from ari.policy.testing import ARI_POLICY_INTEGRATION_TESTING
from plone.app.testing import applyProfile

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = ARI_POLICY_INTEGRATION_TESTING

    def test_theme_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('avrc.ari.theme'))        

    def test_indexing_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('collective.indexing'))        

    def test_datepicker_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('jyu.z3cform.datepicker'))     

    def test_formgen_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('Products.PloneFormGen'))   