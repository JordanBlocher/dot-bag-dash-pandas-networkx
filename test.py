from nxn import * 
import nxn as nxn
from params import make_params
from sim import *
import networkx as nx
import pandas as pd
import numpy as np
import random
import time
from termcolor import colored
from tests import *

values = pd.read_csv('./params/params.dat')
f = open('./params/params.dat','w')
f.write(values.to_csv(index=False).strip())
f.close()

params=make_params()

sim = Sim(make_params)
rnum=1
while True:
    print("\n---------------------------------ROUND", rnum,'----------------------------------\n')
    sim.do_pandas()
    rnum+=1
