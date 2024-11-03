def verify_libraries():
    """
    Verify that matplotlib and pandas are installed successfully.
    :return: True if all libraries are installed successfully, False otherwise.
    """
    try:
        ### YOUR CODE HERE ###



        ######################
        print("All libraries installed successfully.")
        return True
    except ImportError:
        print("Some libraries are not installed.")
        return False
