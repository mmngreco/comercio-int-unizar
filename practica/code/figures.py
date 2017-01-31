import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib
# In[93]:

get_ipython().magic('matplotlib inline')
# sólo dos decimasl
_ = get_ipython().magic('precision 2')


# In[94]:

# load libraries and set plot parameters
from IPython.display import set_matplotlib_formats

# formato tablas

def notacion_esp(x):
    x = "{:,.2f}".format(float(x))
    if len(x.split(".")) == 2:
        x = ",".join([x.split(".")[0].replace(",", "."),
                      x.split(".")[1]])
    else:
        x
    return x

# tablas formato latex
# pd.set_option('display.notebook_repr_html', True)
# def _repr_latex_(self):
#     return "\centering{%s}" % self.to_latex()
# pd.DataFrame._repr_latex_ = _repr_latex_  # monkey patch pandas DataFrame
pd.set_option('display.float_format', notacion_esp)
pd.set_option('display.max_rows', 500)     # muestra 500 líneas cómo máximo
pd.set_option('display.max_columns', 100)  # muestra 100 columnas como máximo
pd.set_option('display.max_colwidth', 150) # muestra 150 caracteres cómo maxímo en una celda

# formato de los gráficos
plt.style.use(['seaborn-white', 'seaborn-paper'])
matplotlib.rc("font", family="Times New Roman", size=15)

set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 75

plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = 10, 6
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 14

# plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "Times New Roman"
plt.rcParams['font.serif'] = "cm"
