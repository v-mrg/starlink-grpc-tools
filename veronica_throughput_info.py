#!/bin/bash
import starlink_grpc, time, csv

while True:
    with open('/home/debroglie2/march7throughput.csv','a') as fd:
        status = starlink_grpc.status_data()
        # print(status[0])
        newrow = [time.time_ns(), status[0]["uplink_throughput_bps"], status[0]["downlink_throughput_bps"]]
        writer = csv.writer(fd)
        writer.writerow(newrow)
        time.sleep(0.1)
