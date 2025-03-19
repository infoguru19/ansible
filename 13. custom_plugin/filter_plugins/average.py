def average(list):
    '''Return the average of a list of numbers'''
    return sum(list) / float(len(list))

class FilterModule(object):
    ''' Custom ansible filters '''
    def filters(self):
        return {
            'average': average
        }