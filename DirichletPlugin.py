from scipy.stats import dirichlet
import numpy

import PyIO
import PyPluMA

class DirichletPlugin:
    def input(self, inputfile):
       self.parameters = PyIO.readParameters(inputfile)
       quantilefile = open(PyPluMA.prefix()+self.parameters["quantiles"], 'r')
       tmplist = []
       for line in quantilefile:
           tmplist.append(float(line.strip()))
       self.quantiles = numpy.array(tmplist)
       alphafile = open(PyPluMA.prefix()+self.parameters["alphas"], 'r')
       tmplist = []
       for line in alphafile:
           tmplist.append(float(line.strip()))
       self.alpha = numpy.array(tmplist)

    def run(self):
       self.pdf = dirichlet.pdf(self.quantiles, self.alpha)

    def output(self, outputfile):
       print(self.pdf)

            
            
#quantiles = numpy.array([0.2, 0.2, 0.6])  # specify quantiles

#alpha = numpy.array([0.4, 5, 15])  # specify concentration parameters

#print(dirichlet.pdf(quantiles, alpha))
