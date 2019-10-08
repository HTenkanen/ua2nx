import time
import networkx as nx
import pandas as pd

def parse_nx_node(row, attr, idcol):
    """Parses nodes into nx-format"""
    attr = row[attr].copy()
    return (row[idcol], attr.to_dict())

def parse_nx_edge(row, attr_cols, fr, to):
    """Parses edges into nx-format"""
    idx = row.name
    attr = row[attr_cols].copy().to_dict()
    return (row[fr], row[to], idx, attr)


def optimize_graph(edges, aggr_type, fr='from_int', to='to_int', weight_col='weight'):
    """
    Optimize the graph in terms of keeping only e.g. 'min' or 'max' (fastest / slowest) edges between nodes.
    This process can dramatically decrease the size of the graph.

    Parameters
    ----------

    edges : pd.DataFrame
        Pandas DataFrame containing the edge information.
    aggr_type : str
        Aggregation type. Possible values are: 'min', 'max', 'mean', 'median'

    """
    # Group and aggregate edges by from and to -nodes using selected aggregation method
    optimized = edges.groupby([fr, to])[weight_col].agg(aggr_type).reset_index() \
        .merge(edges, on=[fr, to]).rename(columns={weight_col + '_x': weight_col}) \
        .drop_duplicates([fr, to]) \
        .drop(weight_col + '_y', axis=1)
    return optimized


def urbanaccess_to_nx(ua_G,
                      edge_attr=['from', 'to', 'from_int', 'to_int', 'weight', 'net_type', 'route_type',
                                 'sequence', 'unique_agency_id', 'unique_route_id',
                                 'unique_trip_id'],
                      crs={'init': 'epsg:4326'},
                      minimize=False,
                      use_integer_nodeids=True,
                      optimize=None,
                      weight_col='weight'
                      ):
    """
    Converts the input UrbanAccess graph to NetworkX MultiDiGraph.

    Parameters
    ----------

    ua_G : <urbanaccess.network.urbanaccess_network>
        UrbanAccess graph that should contain GTFS data as well as walking network, stored in net_edges & net_nodes.
    edge_attr : list
        Edge attributes that will be included in the final NetworkX graph. The necessary ones are 'from', 'to', and 'weight'.
    crs : CRS dictionary.
        Coordinate Reference System of the input data. GTFS and OSM are in WGS84 (epsg:4326) by default.
    minimize : <boolean> (default: False)
        If `minimize=True`, the tool will include only necessary attributes when creating the graph.
    use_integer_nodeids: Boolean (default: True)
        If `use_integer_nodeids=True`, the tool will build the graph using integer numbers as the nodeids.
    optimize : str (default: None)
        It is possible to optimize the network by including e.g. only fastest ('min') or longest ('max') journey legs between
        stops that might vary at different times of the day due schedule changes. Possible aggregation methods are: None, 'min', 'max', 'mean', 'median'.
    weight_col : str
        Name of the column that contains the cost information.

    Assumptions
    -----------
    The function assumes that the UrbanAccess graph is "full", i.e. the transit and walk networks have been built and integrated.
    To check this, you should have data inside DataFrames under `ua.network.ua_network.net_edges`, `ua.network.ua_network.net_nodes`,
    as well as in `ua.network.ua_network.net_connector_edges` (connects stops to walking network).
    """

    # Perform some basic sanity checks
    assert isinstance(ua_G.net_nodes, pd.DataFrame), "UrbanAccess network does not contain valid `net_nodes` DataFrame."
    assert isinstance(ua_G.net_edges, pd.DataFrame), "UrbanAccess network does not contain valid `net_edges` DataFrame."
    assert len(ua_G.net_nodes) > 0, "Could not find any nodes from UrbanAccess network."
    assert len(ua_G.net_edges) > 0, "Could not find any edges from UrbanAccess network."

    print("Converting to NetworkX graph ..")
    log_start = time.time()
    # Connected graph items
    nodes = ua_G.net_nodes
    edges = ua_G.net_edges
    graph = nx.MultiDiGraph()

    # Reset index for nodes to get the integer version of the node_id
    nodes = nodes.reset_index()

    if use_integer_nodeids:
        fr = 'from_int'
        to = 'to_int'
        nodeid = 'id_int'
    else:
        fr = 'from'
        to = 'to'
        nodeid = 'id'

    if minimize:
        exp_edge_attr = [fr, to, nodeid, weight_col]
        exp_node_attr = [nodeid, 'x', 'y']
    else:
        exp_edge_attr = edge_attr
        exp_node_attr = list(nodes.columns)

    if optimize is not None:
        assert optimize in ['min', 'max', 'mean', 'median'], "Possible optimization methods are: 'min', 'max', 'mean', 'median'. Got %s." % optimize
        edges = optimize_graph(edges=edges, aggr_type=optimize, weight_col=weight_col)

    # Convert nodes
    start = time.time()
    nodes['nx_node'] = nodes.apply(parse_nx_node, attr=exp_node_attr, idcol=nodeid, axis=1)
    print("Converted nodes in %s minutes." % (round((time.time() - start) / 60, 1)))

    # Convert edges
    start = time.time()
    edges['nx_edge'] = edges.apply(parse_nx_edge, attr_cols=exp_edge_attr, fr=fr, to=to, axis=1)
    print("Converted edges in %s minutes." % (round((time.time() - start) / 60, 1)))

    # Create the Nx Graph
    graph.add_nodes_from(nodes['nx_node'].to_list())
    graph.add_edges_from(edges['nx_edge'].to_list())

    # Add metadata so that the graph works directly e.g. with OSMnx functions
    graph.graph['crs'] = crs
    graph.graph['name'] = edges['unique_agency_id'].unique()[0]
    print("Created NetworkX graph in %s minutes with %s nodes and %s edges." % (
    round((time.time() - log_start) / 60, 1), len(nodes), len(edges)))
    return graph