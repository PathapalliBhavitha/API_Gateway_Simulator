memory_store = []

def save_log(data):

    memory_store.append(data)

    return {
        "message": "Log saved",
        "total_logs": len(memory_store)
    }

def get_logs():

    return memory_store