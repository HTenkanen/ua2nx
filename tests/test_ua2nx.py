def test_import():
    try:
        from ua2nx import urbanaccess_to_nx
    except:
        raise ImportError("Could not import function `urbanaccess_to_nx` from module `ua2nx`.")

def test_urbanaccess_to_nx():
    from ua2nx import urbanaccess_to_nx
    import urbanaccess as ua

    # Load test data
    uaG = ua.network.load_network(filename='test_net.h5', dir='.')

    # Test converting to NetworkX graph
    nxG = urbanaccess_to_nx(uaG)
    print("Successfully converted the UrbanAccess Graph into NetworkX MultiDiGraph.")

def run_tests():
    test_import()
    test_urbanaccess_to_nx()

if __name__ == "__main__":
    run_tests()