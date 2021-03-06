import pandas as pd

import decisionengine_modules.AWS.sources.AWSInstancePerformance as AWSInstancePerformance

config={'data_file':'instance_performance_sample.csv'}

expected_pandas_df = pd.read_csv(config.get("data_file")).drop_duplicates(subset=[ 'AvailabilityZone', 'InstanceType'], keep='last').reset_index(drop = True)
produces = ['Performance_Data']

class TestAWSInstancePerformance:

    def test_produces(self):
        aws_job_limits = AWSInstancePerformance.AWSInstancePerformance(config)
        assert aws_job_limits.produces() == produces

    def test_acquire(self):
        aws_i_p = AWSInstancePerformance.AWSInstancePerformance(config)
        res = aws_i_p.acquire()
        assert produces == res.keys()
        assert expected_pandas_df.equals(res.get(produces[0]))

