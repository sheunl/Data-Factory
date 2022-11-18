class FileGenerator:
    
    def print_out(var, filename):
        file = open(filename,'w')
        file.write(var)
        file.close()