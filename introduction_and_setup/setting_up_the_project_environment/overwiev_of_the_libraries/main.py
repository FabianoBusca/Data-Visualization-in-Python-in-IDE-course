if __name__ == '__main__':
    try:
        import seaborn as sns
        print("Seaborn is installed")
    except ImportError:
        print("Seaborn is not installed")
