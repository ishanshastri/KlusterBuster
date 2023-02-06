import numpy as np
class Kluster:
    K: int
    Distance: callable
    #Difference: callable

    def __init__(self, Special_K, norm):#, diff):
        """
        Special_K: # of clusters ur looking to separate/breakfast
        norm (callable): distance function given ur input space
        """
        self.K = Special_K
        self.Distance = norm
        #self.Difference = diff

    #Public Methods
    def Kluster(data):
        """
        data is a list of 'points' in given input space; wrapper func.
        Return: dictionary mapping K-points to corresponding datapoints contained in each bin
        """

    #Private Methods
    #def min

    def _kluster(self, data, k_pts, iters):
        """
        recursive kluster algol; k_pts are initialized to random points from sample space
        """
        if iters==0:
            return k_pts

        v_addToBins = np.vectorize(self._addToBin, excluded=['k_pts'])
        v_addToBins(data, k_pts)
    
        #for k in k_pts:
        #    avg = np.array(k_pts[k]).mean()
        ##    k_pts[k] = avg
         #   self._changeMonKey(k_pts, k, avg)
        

        v_resetMonKeys = np.vectorize(self._resetMonKey, excluded=['k_pts'])
        keys = list(k_pts.keys())#np.array(k_pts.keys())
        v_resetMonKeys(keys, k_pts)
        #self._resetMonKey(10, k_pts)
        print(k_pts)
        #for d in data:
        #    bin = _getNearestBin(d, k_pts.keys())
        #    k_pts[bin].append(d)

    def _resetMonKey(self, key, k_pts):
        avg = np.array(k_pts[key]).mean()
        #key = avg
        self._changeMonKey(k_pts, key, avg)

    def _getNearestBin(self, point, bins):
        """
        Get closest bin from bins to the point
        """
        min = -1
        bin = None
        for p in bins:
            d = self.Distance(p, point)
            if min==-1 or min > d:
                min = d
                bin = p
        return bin
        
    def _addToBin(self, point, k_pts):
        bin = self._getNearestBin(point, k_pts.keys())
        k_pts[bin].append(point)

    def _changeMonKey(self, dict, old_key, mon_key):
        dict[mon_key] = dict[old_key]
        dict.pop(old_key)

ex = Kluster(3, lambda a, b:abs(a-b))#, lambda y:y)
print(ex.K)
print(ex.Distance(5, 4))
#ex._kluster(None, None)
bins = {0: [], 5: [], 10: []}
data = np.array([i for i in range(20)])
ex._kluster(data, bins, 9)