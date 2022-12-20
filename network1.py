import networkx as nx
import matplotlib.pyplot as plt
def generate_er(n=8, r=2):
   
    return nx.erdos_renyi_graph(n, r, seed=42)

def plot_er(G, n):
    
    # Put the nodes in a circular shape
    pos = nx.circular_layout(G)
    #pos = nx.spring_layout(G, iterations=50, seed=42)
    nx.draw(G, pos, node_color=range(50), node_size=400, cmap=plt.cm.Blues)
    
    print(pos)
    plt.show()
    
# Generate the ER graphs
n=50
p=0
G_er = generate_er(n, p)
pos = nx.circular_layout(G_er)

plot_er(G_er, n)
xd=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
import numpy as np
for i in range(50):
    x=pos.get(i)
    xd[i]=x[0]

yd=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(50):
    y=pos.get(i)
    yd[i]=y[1]
    
xlog = np.log(xd)
ylog = np.log(yd)
plt.scatter(xlog, ylog)
plt.xlabel('Log(x)')
plt.ylabel('Log(y)')
plt.title('Log-Log Plot')

plt.show()


MIN, MAX = .01, 8.0
import pylab as pl

pl.figure()
pl.hist(yd, bins = 10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50))
pl.gca().set_xscale("log")
plt.xlabel('Log(y)')
plt.ylabel('bins')
plt.title('logarithmic binning Plot')
pl.show()


# getting data of the histogram
count, bins_count = np.histogram(yd, bins=10)
  
# finding the PDF of the histogram using count values
pdf = count / sum(count)
  
# using numpy np.cumsum to calculate the CDF
# We can also find using the PDF values by looping and adding
cdf = np.cumsum(pdf)
  
# plotting PDF and CDF
plt.figure()
plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="CDF")
plt.legend
plt.xlabel('Bins')
plt.ylabel('pdf,cdf')
plt.title('cumulative distribution')
plt.show()