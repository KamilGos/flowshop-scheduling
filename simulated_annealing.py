import numpy as np
import random
import math
import time


def makespan(order, tasks, machines_val):
    times = []
    for i in range(0, machines_val):
        times.append(0)
    for j in order:
        times[0] += tasks[j][0]
        for k in range(1, machines_val):
            if times[k] < times[k-1]:
                times[k] = times[k-1]
            times[k] += tasks[j][k]
    return max(times)


def insert(sequence, tasks_val):
    a = random.randrange(0, tasks_val)
    b = random.randrange(0, tasks_val)
    new_seq = sequence[:]
    new_seq.remove(a)
    new_seq.insert(b, a)
    return new_seq


def swap(list, tasks_val):
    a = random.randrange(0, tasks_val)
    b = random.randrange(0, tasks_val)
    tmp_list = list.copy()
    tmp = tmp_list[a]
    tmp_list[a] = tmp_list[b]
    tmp_list[b] = tmp
    return tmp_list


def probability(Cold, Cnew, Temp):
    if Cnew < Cold:
        prob = 1
    else:
        prob = math.exp((Cold-Cnew)/Temp)
    return prob

def annealing1(T, u):
    return T*u


############################################### CLASSICAL APPROACH ####################################################
def sim_ann1(tasks_val, tasks, machines_val, T_start, T_end):
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)  
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    while (T >= Tgr):
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability(cmax_old, cmax, T)
        s = random.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = annealing1(T, u)
        else:
            T = annealing1(T, u)
    return pi, cmax_old


############################################# DIFFERENT ANNEALING FUNCTION ###########################################
def annealing2(T, k, kmax):
    return T*(k/kmax)

def sim_ann2(tasks_val, tasks, machines_val, T_start, T_end, iter_val):
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    iter = 0
    max_iter = iter_val

    for i in range(0, max_iter):
        iter = iter + 1
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability(cmax_old, cmax, T)
        s = random.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = annealing2(T, iter, max_iter)
        else:
            T = annealing2(T, iter, max_iter)
        if T == 0:
            break
    return pi, cmax_old



########################################## WITHOUT PROBABILITY EQUALS TO 1 ############################################
def probability3(Cold, Cnew, Temp):
    prob = math.exp((Cold-Cnew)/Temp)
    return prob

def sim_ann3(tasks_val, tasks, machines_val, T_start, T_end):
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    while (T >= Tgr):
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability3(cmax_old, cmax, T)
        s = random.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = annealing1(T, u)
        else:
            T = annealing1(T, u)
    return pi, cmax_old


############################################## WITHOUT Cnew = Cold ####################################################
#bez takiego samego Cnew jak Cold (bez rowne)
def probability4(Cold, Cnew, Temp):
    if Cnew < Cold:
        prob = 1
    if Cnew > Cold:
        prob = math.exp((Cold - Cnew) / Temp)
    return prob


def sim_ann4(tasks_val, tasks, machines_val, T_start, T_end):
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    while (T >= Tgr):
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        if cmax_old != cmax:
            p = probability4(cmax_old, cmax, T)
            s = random.random()
            if p >= s:
                pi = piprim
                cmax_old = cmax
                T = annealing1(T, u)
            else:
                T = annealing1(T, u)
    return pi, cmax_old


###################################################################### NEH ############################################
def sum_and_order(tasks_val, machines_val, tasks):
    tab = []
    tab1 = []
    for i in range(0, tasks_val):
        tab.append(0)
        tab1.append(0)
    for j in range(0, tasks_val):
        for k in range(0, machines_val):
            tab[j] += tasks[j][k]
    tmp_tab = tab.copy()
    place = 0
    iter = 0
    while(iter != tasks_val):
        max_time = 1
        for i in range(0, tasks_val):
            if(max_time < tab[i]):
                max_time = tab[i]
                place = i
        tab[place] = 1
        tab1[iter] = place
        iter = iter + 1
    return tab1


def insertNEH(sequence, position, value):
    new_seq = sequence[:]
    new_seq.insert(position, value)
    return new_seq


def neh(tasks, machines_val, tasks_val):
    order = sum_and_order(tasks_val, machines_val, tasks)
    current_seq = [order[0]]
    for i in range(1, tasks_val):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp = insertNEH(current_seq, j, order[i])
            cmax_tmp = makespan(tmp, tasks, machines_val)
            if min_cmax > cmax_tmp:
                best_seq = tmp
                min_cmax = cmax_tmp
        current_seq = best_seq
    return current_seq, makespan(current_seq, tasks, machines_val)


def read_data(filename):
    file = open(filename, "r")

    tasks_val, machines_val = file.readline().split()
    tasks_val = int(tasks_val)
    machines_val = int(machines_val)

    tasks = np.zeros((tasks_val,machines_val))
    for i in range(tasks_val):
        tmp = file.readline().split()
        for j in range(machines_val):
            tasks[i][j] = int(tmp[j])

    print("Number of tasks: ", tasks_val)
    print("Number of machines: ", machines_val)
    print("Tasks: \n", tasks)
    file.close()
    return tasks_val, machines_val, tasks


if __name__ == "__main__":
    tasks_val, machines_val, tasks = read_data("data/flowshop_simann.txt")

    ##########
    # 1 - Annealing functions comparision
    # 2 - Number of operations comparision
    # 3 - Influence rejection the probability 1 on results
    # 4 - Influence rejection the probability when Cmax = CmaxOld
    # 5 - Influence Tstart and Tstop on results
    MODE = 1  # which mode should be executed
    ##########

    if MODE == 1:
        print("Classical")
        best_seq, best_cmax = sim_ann1(tasks_val, tasks, machines_val, 5000, 10)
        print("Best sequence: ", best_seq)
        print("Best Cmax: ", best_cmax)

        print("Midificated")
        best_seqm, best_cmaxm = sim_ann2(tasks_val, tasks, machines_val, 5000, 10, 1000)
        print("Best sequence: ", best_seq)
        print("Best Cmax: ", best_cmax)

    if MODE == 2:
        a_iter = [10, 100, 1000, 10000, 100000]
        cmax = 0
        for i in a_iter:
            for j in range(0,4):
                best_seq, best_cmax = sim_ann2(tasks_val, tasks, machines_val, 5000, 10, i)
                cmax = cmax + best_cmax
            cmax = cmax /4
            print(i, cmax)
            cmax = 0

    if MODE == 3:
        cmax = 0
        print("Probability with 1 ")
        for k in range(0,4):
            best_seq, best_cmax = sim_ann1(tasks_val, tasks, machines_val, 5000, 10)
            cmax = cmax + best_cmax
        cmax = cmax/4
        print (best_seq, cmax)

        cmax= 0
        print("Probability without 1 ")
        for k in range(0,4):
            best_seq, best_cmax = sim_ann3(tasks_val, tasks, machines_val, 5000, 10)
            cmax = cmax + best_cmax
        cmax = cmax/4
        print (best_seq, cmax)

    if MODE == 4:
        cmax = 0
        print("Probability with >=")
        for k in range(0,4):
            best_seq, best_cmax = sim_ann1(tasks_val, tasks, machines_val, 5000, 10)
            cmax = cmax + best_cmax
        cmax = cmax/4
        print (best_seq, cmax)

        cmax= 0
        print("Probability without == ")
        for k in range(0,4):
            best_seq, best_cmax = sim_ann4(tasks_val, tasks, machines_val, 5000, 10)
            cmax = cmax + best_cmax
        cmax = cmax/4
        print (best_seq, cmax)

    if MODE == 5:
        T_start = [5000, 10000]
        T_end = [1000]

        cmax = 0
        for i in T_start:
            for j in T_end:
                for k in range(0,4):
                    seq, c = sim_ann1(tasks_val, tasks, machines_val, i, j)
                    cmax = cmax + c
                cmax = cmax/4
                cmax = 0
                print("T_start: ", i, "T_stop:", j)
                print(seq, c)
