def start_debugger():
    if os.getenv("DEBUGGER") is not None:
        import debugpy
        debugpy.listen(int(os.environ.get('DEBUG_PORT')))
        debugpy.wait_for_client()
