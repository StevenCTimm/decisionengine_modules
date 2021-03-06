import os
import pytest
import mock
import pprint
import utils
from decisionengine_modules.glideinwms.sources import factory_global
from decisionengine_modules.htcondor import htcondor_query


config = {
    'condor_config': 'condor_config',
    'factories': [
        {
            'collector_host': 'cmssrv280.fnal.gov',
            #'classad_attrs': ['Name', 'EntryName', 'GLIDEIN_Gatekeeper', 'GLIDEIN_GridType'],
        },
    ]
}


config_bad = {
    'condor_config': 'condor_config',
    'factories': [
        {
            'collector_host': 'dummy_collector.fnal.gov',
            #'classad_attrs': ['Name', 'EntryName', 'GLIDEIN_Gatekeeper', 'GLIDEIN_GridType'],
        },
    ]
}


class TestFactoryGlobalManifests:

    def test_produces(self):
        fg = factory_global.FactoryGlobalManifests(config)
        produces = ['factoryglobal_manifests']
        assert(fg.produces() == produces)


    def test_acquire(self):
        fg = factory_global.FactoryGlobalManifests(config)
        with mock.patch.object(htcondor_query.CondorStatus, 'fetch') as f:
            f.return_value = utils.input_from_file('factory_global.cs.fixture')
            pprint.pprint(fg.acquire())


    def test_acquire_live(self):
        fg = factory_global.FactoryGlobalManifests(config)
        pprint.pprint(fg.acquire())


    def test_acquire_bad(self):
        fg = factory_global.FactoryGlobalManifests(config_bad)
        fg_df = fg.acquire()
        assert((fg_df['factoryglobal_manifests'] is None) or (len(fg_df['factoryglobal_manifests']) == 0))
