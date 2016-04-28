
#integration function that integrates the flux from Caitlin's BB function

def int(wave,objflux):
    #wave --> file with wavelengths in them. objflux --> file with fluxes at those wavelengths
    wavefile = open(wave,'r') #read in the wave file
    wavelines = wavefile.readlines()
    fluxfile = open(objflux,'r') #read in the flux file
    fluxlines = fluxfile.readlines()
    delt_lamb = float(wavelines[2]) - float(wavelines[1])
    m = 0
    for line in fluxfile:
        m += line*delt_lamb
    return m

#issue with not looping through lines in the line??


