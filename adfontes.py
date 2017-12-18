from random import uniform
job_1 = {1: [2, 4, 1], 2: [1, 5, 2], 3:[1, 5, 1], 4:[2, 6, 2]}  #job = {op_number : [machine, time, operation sequence]}
gen_len = len(job_1)
genes = [uniform(0, 1) for _ in range(gen_len*2)]
time = 0
buffer = []
prioritetes = genes[:len(genes)//2]

def generate(n):
    chrms = list()
    for i in range(2*n):
        chrms.append(uniform(0, 1))
    return chrms


def get_priority(lst):
    return lst[:len(lst)//2]


def get_delay(lst, max_dur, iter):
    lst_1 = lst[len(lst)//2::]
    lst_2 = list()
    return lst[iter]*1.5*max_dur


def initialize_shadow(mach_number, alltime_procces):
    lst = [[[0]*alltime_procces for _ in range(mach_number)]]
    return lst


def update(jobs):
    chrms = generate(len(job_1))
    prioritetes = get_priority(chrms)
    buffer = list()
    delays = list()
    prior_job = int()
    jobs_index = list(jobs.keys())
    print(jobs_index)
    priority_lst = list()
    for i in range(len(jobs_index)):
        delays.append(get_delay(chrms, jobs.get(i+1)[1], i))
    for items in jobs:
        if jobs.get(items)[2] == 1:
            buffer.append(items)
    return buffer

update(job_1)




def genetic(job, prioriteetes, machines, delays):
    chrms = generate(len(job_1))
    tg = [0]
    prior_lst = list()
    operation_sequences = []
    for items in job.values():
        operation_sequences.append(items[2])
    max_sequence = max(operation_sequences)
    jobs_index = list(job.keys())
    for i in range(len(jobs_index)):
        delays.append(get_delay(chrms, job.get(i+1)[1], i))
    buffer = update(job)
    while job != {}:
        for items in buffer:
            prior_lst.append(prioritetes[items - 1])
        num_job = prioritetes.index(max(prioritetes))
        prior_lst.clear()
        if num_job <= tg[0] + delays[num_job - 1]:
            try:
                machines[job.get(num_job)[0]] = job.get(num_job)[1]
                job.pop(num_job)
                buffer.remove(num_job)
                buffer.append(num_job + max_sequence)
            except KeyError:
                continue





a = {1:[1, 2, 3], 2:[2, 2, 2], 3:[3, 2, 3], 4:[5, 2, 3]}
#print(max(a.values(), key=lambda x:x[0]))