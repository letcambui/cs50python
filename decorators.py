def announce(f): # aceita uma funcao como input (no caso, a funcao f) e devolve uma modificação dessa função como output
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

@announce #utilizaremos o anuncio decorativo aquis
def hello():
    print("Hello world.")

hello()

