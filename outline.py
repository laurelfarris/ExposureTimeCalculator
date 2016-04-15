'''
This is an outline of sorts for the exposure time calculator.
It's in python syntax, but the main purpose is to show how every
individual function fits into the main code, what input they take,
what they return, and how those return values will eventually
calculate an exposure time.
'''


def exposure_time_calculater(?):
    '''
    User input: object magnitude
                desired S/N
                telescope
                instrument
                bandpass/wavelength
                moon phase
                airmass
    '''


    def background():
        ''' calculate background '''
        return background

    def atmospheric_transmission():
        ''' calculate atmospheric transmisison (a) '''
        return a

    def system_transmission():
        ''' calculate total system transmisison (q) '''

        def telescope_transmission():
            ''' calculate telescope transmisison '''
            return telescope_q

        def instrument_transmission():
            ''' calculate instrument transmisison '''
            return instrument_q

        def detector_transmission():
            ''' calculate detector transmisison '''
            return detector_q


        return q


    return exposure_time


exposure_time = exposure_time_calculater()

