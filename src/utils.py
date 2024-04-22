import subprocess
import argparse
import psutil
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description="Get metrics from a command execution and store them in a file.")
    parser.add_argument("directory", type=str, help="Directory where the results will be stored.")
    parser.add_argument("command", nargs='+', help="Command to be executed.")
    return parser.parse_args()

def syscalls(command, result_file):
    with subprocess.Popen(
        ["strace", "-o", result_file] + command, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
    ) as proc:
        stdout, stderr = proc.communicate()
        return stdout, stderr

def memory_usage(command, interval=1e-2):
    memory_records = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_process = psutil.Process(process.pid)
    try:
        while process.poll() is None:
            memory_records.append(ps_process.memory_info()._asdict())
            time.sleep(interval)  # Wait until the next record
    except psutil.NoSuchProcess:
        print("The process finished before the end of the monitoring.")
    stdout, stderr = process.communicate()
    return memory_records, stdout, stderr

def cpu_usage(command, interval=1e-2):
    cpu_records = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_process = psutil.Process(process.pid)
    try:
        while process.poll() is None:
            cpu_records.append(ps_process.cpu_times()._asdict())
            time.sleep(interval)
    except psutil.NoSuchProcess:
        print("The process finished before the end of the monitoring.")
    stdout, stderr = process.communicate()
    return cpu_records, stdout, stderr


def execution_time(command, iterations=1):
    execution_times = []
    for _ in range(iterations):
        start_time = time.time()
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return execution_times, stdout, stderr