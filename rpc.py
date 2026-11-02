# call_id,client_name,method_name,param_value,timestamp
# 101,Client_A,processData,450,10:00:01
# 102,Client_B,processData,600,10:00:02
# 103,Client_C,processData,300,10:00:03
# 104,Client_D,processData,750,10:00:04


import csv

# Server-side remote function
def processData(value):
    print("[SERVER EXECUTION] Processing parameter:", value)

    result = int(value) * 2

    return result


# RPC Dispatcher
def rpc_dispatcher(method_name, param_value):

    if method_name == "processData":
        result = processData(param_value)
        return result

    else:
        return "Method not found"


# Client reads CSV and invokes server
with open("rpc_calls_17.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print("\n[DISPATCH] Client invoking method")
        print("Call ID:", row["call_id"])
        print("Client:", row["client_name"])
        print("Method:", row["method_name"])

        # Marshalling arguments
        param = row["param_value"]
        print("[MARSHALLING] Packing argument:", param)

        # Server execution through dispatcher
        result = rpc_dispatcher(
            row["method_name"], param
        )

        # Return result to client
        print("[RETURN] Result:", result)


# op:

# [DISPATCH] Client invoking method
# Call ID: 101
# Client: Client_A
# Method: processData
# [MARSHALLING] Packing argument: 450
# [SERVER EXECUTION] Processing parameter: 450
# [RETURN] Result: 900

# [DISPATCH] Client invoking method
# Call ID: 102
# Client: Client_B
# Method: processData
# [MARSHALLING] Packing argument: 600
# [SERVER EXECUTION] Processing parameter: 600
# [RETURN] Result: 1200