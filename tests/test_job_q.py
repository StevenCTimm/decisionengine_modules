import os
import pytest
import mock
import pprint
import utils
from decisionengine_modules.htcondor import htcondor_query
from decisionengine_modules.htcondor.sources import job_q


config_cq = {
    'condor_config': 'condor_config',
    'collector_host': 'fermicloud122.fnal.gov',
    'schedds': ['fermicloud122.fnal.gov'],
    'classad_attrs': ['ClusterId', 'ProcId', 'JobStatus']
}


class TestJobQ:

    def test_produces(self):
        produces = ['job_manifests']
        jq = job_q.JobQ(config_cq)
        assert(jq.produces() == produces)


    def test_condorq(self):
        jq = job_q.JobQ(config_cq)
        with mock.patch.object(htcondor_query.CondorQ, 'fetch') as f:
            f.return_value = utils.input_from_file('cq.fixture')
            pprint.pprint(jq.acquire())


    def test_condorq_live(self):
        jq = job_q.JobQ(config_cq)
        pprint.pprint(jq.acquire())
