def test_import():
    try:
        from ua2nx import urbanaccess_to_nx
    except:
        raise ImportError("Could not import function `urbanaccess_to_nx` from module `ua2nx`.")

def test_urbanaccess_to_nx_default_settings():
    from ua2nx import urbanaccess_to_nx
    import urbanaccess as ua

    # Load test data
    uaG = ua.network.load_network(filename='test_net.h5', dir='.')

    # Test converting to NetworkX graph
    nxG = urbanaccess_to_nx(uaG)
    print("Successfully converted the UrbanAccess Graph into NetworkX MultiDiGraph with default settings.")
    del uaG, nxG

def test_urbanaccess_to_nx_minimize():
    from ua2nx import urbanaccess_to_nx
    import urbanaccess as ua

    # Load test data
    uaG = ua.network.load_network(filename='test_net.h5', dir='.')

    # Test converting to NetworkX graph
    nxG = urbanaccess_to_nx(uaG, minimize=True)
    print("Successfully converted the UrbanAccess Graph into NetworkX MultiDiGraph with minimize on.")
    del uaG, nxG


def test_urbanaccess_to_nx_integer_ids():
    from ua2nx import urbanaccess_to_nx
    import urbanaccess as ua

    # Load test data
    uaG = ua.network.load_network(filename='test_net.h5', dir='.')

    # Test converting to NetworkX graph
    nxG = urbanaccess_to_nx(uaG, use_integer_nodeids=True)
    print("Successfully converted the UrbanAccess Graph into NetworkX MultiDiGraph with integer ids.")
    del uaG, nxG


def test_urbanaccess_to_nx_minimize_and_integer_ids():
    from ua2nx import urbanaccess_to_nx
    import urbanaccess as ua

    # Load test data
    uaG = ua.network.load_network(filename='test_net.h5', dir='.')

    # Test converting to NetworkX graph
    nxG = urbanaccess_to_nx(uaG,  minimize=True, use_integer_nodeids=True)
    print("Successfully converted the UrbanAccess Graph into NetworkX MultiDiGraph with minimize on and integer ids.")
    del uaG, nxG

def test_urbanaccess_to_nx_optimization():
    from ua2nx import urbanaccess_to_nx
    import urbanaccess as ua

    # Load test data
    uaG = ua.network.load_network(filename='test_net.h5', dir='.')

    # Test converting to NetworkX graph
    nxG = urbanaccess_to_nx(uaG, optimize='min')
    print("Successfully converted the UrbanAccess Graph into NetworkX MultiDiGraph with optimizing the graph with 'min'.")
    del uaG, nxG

def run_tests():
    test_import()
    test_urbanaccess_to_nx_default_settings()
    test_urbanaccess_to_nx_minimize()
    test_urbanaccess_to_nx_integer_ids()
    test_urbanaccess_to_nx_minimize_and_integer_ids()
    test_urbanaccess_to_nx_optimization()

if __name__ == "__main__":
    run_tests()