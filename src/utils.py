from cpuinfo import get_cpu_info
import subprocess
import argparse
import psutil
import numpy as np
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description="Get metrics from a command execution and store them in a file.")
    parser.add_argument("benchmark", type=str, help="Name of the benchmark.")
    parser.add_argument("--sys", action="store_true", help="Run the command with strace.")
    parser.add_argument("--val", action="store_true", help="Run the command with valgrind.")
    parser.add_argument("command", nargs='+', help="Command to be executed.")
    return parser.parse_args()

def syscalls(command, result_file):
    res = subprocess.run(["strace", "-o", result_file, *command], text=True, capture_output=True)
    return res.stdout, res.stderr

# Why is logaritmic scale used? because metrics like memory and cpu usage fast in the beginning and then slow down
def memory_and_cpu_usage(command, max_time, base=2):
    memory_records = []
    cpu_records = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_process = psutil.Process(process.pid)

    intervals = np.logspace(0, np.log2(max_time), num=100, base=base)
    start_time = time.time()
    try:
        for interval in intervals:
            elapsed_time = time.time() - start_time
            if elapsed_time >= max_time:
                break
            if process.poll() is not None:
                break
            memory_records.append(ps_process.memory_info()._asdict())
            cpu_records.append(ps_process.cpu_times()._asdict())
            time.sleep(interval - elapsed_time)  # Wait until the next record
    except psutil.NoSuchProcess:
        print("The process finished before the end of the monitoring.")
    stdout, stderr = process.communicate()
    return cpu_records, memory_records, stdout, stderr

def execution_time(command, iterations=1):
    execution_times = []
    time_format = "%e, %P, %M"
    for _ in range(iterations):
        result = subprocess.run(["/usr/bin/time", "-f", time_format, *command], text=True, capture_output=True)
        execution_times.append(result.stderr)
    return execution_times

def pc_info():
    info = get_cpu_info()
    return {
        'brand_raw': info['brand_raw'],
        'vendor_id_raw': info['vendor_id_raw'],
        'arch': info['arch'],
        'count': info['count'],
        'l2_cache_size': info['l2_cache_size'],
        'l3_cache_size': info['l3_cache_size'],
        'hz_actual_friendly': info['hz_actual_friendly'],
        'hz_advertised_friendly': info['hz_advertised_friendly'],
        'l2_cache_line_size': info['l2_cache_line_size'],
        'l2_cache_associativity': info['l2_cache_associativity'],
    }

def run_callgrind(command, result_file):
    # Ejecutar el commanda con Valgrind y Callgrind
    result = subprocess.run(
        ['valgrind', '--tool=callgrind', '--simulate-cache=yes', f'--callgrind-out-file={result_file}', *command],
        capture_output=True, text=True
    )
    
    # Verificar si la ejecución fue exitosa
    if result.returncode != 0:
        print(f"Error al ejecutar {command}: {result.stderr}")
        return None
    
def run_massif(command, result_file):
    # Ejecutar el commanda con Valgrind y Callgrind
    result = subprocess.run(
        ['valgrind', '--tool=massif', f'--massif-out-file={result_file}', *command],
        capture_output=True, text=True
    )
    
    # Verificar si la ejecución fue exitosa
    if result.returncode != 0:
        print(f"Error al ejecutar {command}: {result.stderr}")
        return None

# TODO: Save massif and callgrind results in a dataframe