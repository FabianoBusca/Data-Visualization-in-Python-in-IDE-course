def verify_libraries():
    try:
        ### YOUR CODE HERE ###



        ######################
        print("All libraries installed successfully.")
        return True
    except ImportError:
        print("Some libraries are not installed.")
        return False
