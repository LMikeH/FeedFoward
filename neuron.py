import numpy as numpy
from enum import enum
import random

class neurotype(Enum):
    inp = "inp"
    hidden = 'hidden'
    output = 'output'

class connection():
    def __init__(self,parent_neuron,child_neuron,active=True):
        self.parent_neuron = parent_neuron
        self.child_neuron = child_neuron
        self.w = random.random()
        self.b = .2
        self.active = active

        if self.active == False:
            self.w, self.b = 0, 0

class neuron():
    def __init__(self,neurotype,inp=0):
        self.parent_connections = []
        self.child_connections = []
        self.input = inp
        self.neurotype = neurotype

    def addChild(self,child):
        newcon = connection(self,child)
        child.parent_connections.append(newcon)
        self.child_connections.append(newcon)

    def addParent(self,parent):
        newcon = connection(parent,self)
        parent.child_connections.append(newcon)
        self.parent_connections.append(newcon)

    def activate(self):
        if self.neurotype == neurotype.inp:
            return self.input
        else:
            out = 0
            for i in self.parent_connections:
                out += i.w*i.parent_neuron.activate() - i.b
            return np.tanh(out)

    