# Global variable
global_variable = 10

def function_with_local_variable():
    # Local variable
    local_variable = 5
    print("Inside function_with_local_variable:")
    print("Local variable:", local_variable)
    print("Global variable:", global_variable)  # Accessing global variable is allowed

# Function with global variable
def function_with_global_variable():
    print("Inside function_with_global_variable:")
    print("Global variable:", global_variable)
    # Modifying global variable within the function
    global global_variable
    global_variable = 20
    print("Modified global variable:", global_variable)

# Calling the functions
function_with_local_variable()
function_with_global_variable()

# Accessing global variable outside functions
print("Outside functions:")
print("Global variable:", global_variable)
# Uncommenting the line below will result in an error since local_variable is not defined in this scope
# print("Local variable:", local_variable)
