import numpy as np
class Kluster:
    K: int
    Distance: callable
    #Difference: callable
    Klusters = {}

    def __init__(self, Special_K, norm):#, diff):
        """
        Special_K: # of clusters ur looking to separate/breakfast
        norm (callable): distance function given ur input space
        """
        self.K = Special_K
        self.Distance = norm
        #self.Difference = diff

    #Public Methods
    def Kluster(self, data, k = -1, iters=-1, cond=None):
        """
        data is a list of 'points' in given input space; wrapper func.
        Return: dictionary mapping K-points to corresponding datapoints contained in each bin
        """
        if k==-1:
            k=self.K
        
        #if iters==-1:


        #Generate starting sample
        k_pts = self._genSeed(data, k)

        #call func
        return self._kluster(data, k_pts, iters)

    #Private Methods
    #def min
    def _genSeed(self, data, k):
        #STUB: TODO
        bins = {0: [], 5: [], 10: []}
        return bins

    def _kluster(self, data, k_pts, iters):
        """
        recursive kluster algol; k_pts are initialized to random points from sample space
        """
        if iters==0:
            return k_pts
            self.Klusters = k_pts

        v_addToBins = np.vectorize(self._addToBin, otypes=[float], excluded=['k_pts'])
        v_addToBins(data, k_pts)
    
        v_resetMonKeys = np.vectorize(self._resetMonKey, excluded=['k_pts'])
        keys = list(k_pts.keys())#np.array(k_pts.keys())
        #v_resetMonKeys(keys, k_pts)
        wipe = True
        if iters==1:
            wipe = False
        self._resetKeys(k_pts, wipe)

        #recurse to next iteration
        keys = list(k_pts.keys())

        return self._kluster(data, k_pts, (iters-1))
        #dict(zip(list(), [[]]*len(keys)))

    def _resetMonKey(self, key, k_pts, wipe=True):
        avg = np.array(k_pts[key]).mean()
        #key = avg
        self._changeMonKey(k_pts, key, avg)
        if wipe==True:
            k_pts[avg] = []
        

    def _resetKeys(self, k_pts, wipe=True):
        keys = list(k_pts.keys())
        for k in keys:
            avg = np.array(k_pts[k]).mean()
            self._changeMonKey(k_pts, k, avg)
            if wipe==True:
                k_pts[avg] = []


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
        if old_key == mon_key:
            return
        dict[mon_key] = dict[old_key]
        dict.pop(old_key)

#Test
ex = Kluster(3, lambda a, b:abs(a-b))#K=3
bins = {0: [], 5: [], 10: []}
data = np.array([i for i in range(20)])
#print(ex._kluster(data, bins, 9))
print(ex.Kluster(data, 3, 9))
#print(ex.Klusters)