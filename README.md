# ua2nx

A simple conversion tool that converts [UrbanAccess](https://github.com/UDST/urbanaccess) public transport network into [NetworkX](https://networkx.github.io/documentation/networkx-2.3/index.html) MultiDiGraph.
After the conversion, you can use all the basic network analysis methods provided by NetworkX.  

## Installation

You can install the module with pip:

`$ pip install ua2nx` 

## Usage

Basic usage is as simple as: 

```python
from ua2nx import urbanaccess_to_nx
import urbanaccess as ua

# Load precalculated UrbanAccess graph that was saved into H5
uaG = ua.network.load_network(filename='test_net.h5', dir='.')

# Convert to NetworkX MultiDiGraph
nxG = urbanaccess_to_nx(uaG)
```

Read the documentation of [UrbanAccess](https://udst.github.io/urbanaccess/index.html) to learn how to work with GTFS data and Urbanaccess.
