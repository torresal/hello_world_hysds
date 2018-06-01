#!/usr/bin/env python
import os, sys, re, json, requests
from hysds_commons.job_utils import submit_mozart_job
from hysds.orchestrator import submit_job
from hysds.log_utils import logger as logging

def main(num_jobs):
    #Setup input arguments here

    # rule arguement
    rule = {
        "rule_name": "APT",
	"queue": "dumby-job_worker-small",
	"priority": 0,
	"kwargs": '{}'
    }

    # job specification arguement
    job_spec = "job-hello_world:master"
	
    # construct payload
    for i in range(1,num_jobs + 1):
        #payload = {
        #  "job_type": "job:job-hello_world:master",
	#  "job_queue": "job_worker-small", 
	#  "payload": {
        #    "_command": "/home/ops/verdi/ops/hello_world/run_hello_world.sh",
	#    "id": i,	
        #    "min_sleep": 30,
        #    "max_sleep": 60
        #  }
        #}
        # print "Submitting: ",i,"\r"
        # if i % 3 == 0: payload['priority'] = 3
        # if i % 7 == 0: payload['priority'] = 5
        # if i % 12 == 0: payload['priority'] = 7
        # if i % 33 == 0: payload['priority'] = 9
        # submit_job.apply_async((payload,), queue='jobs_processed')
        
        # Set Parameters 
	params = [
                {
                  "name": "id",
                  "from": "value",
                  "value": i,
                }
            ]

        # Submit Mozart job 
	submit_mozart_job({}, rule,
        	hysdsio={"id": i,
                 	"params": params,
                 	"job-specification": job_spec})

if __name__ == "__main__":
    main(int(sys.argv[1])) # first CLI arguement = number of jobs to submit
