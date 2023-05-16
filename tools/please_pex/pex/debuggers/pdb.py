def start_debugger():
    if os.getenv("DEBUGGER") is not None:
        import pdb
        pdb.set_trace()
