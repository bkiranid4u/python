class Bag:
    # Constructs an empty bag 
    def __init__( self ) :
        self._theItems = list()

    # Returns number of items in the bag 
    def __len__( self ) :
        return len(self._theItems)
    
    # Check if the item present in the bag 
    def __contains__( self, item ) :
        return item in self._theItems
    
    # Adds new itme to the bag 
    def add( self, item ) :
        self._theItems.append( item )
    
    # Removes the item from the bag 
    def remove( self, item ) :
        assert item in self._theItems, 'The item should be in bag'
        indx = self._theItems.index(item)
        return self._theItems.pop(indx)

    # Returns the iterator 
    def __iter__( self ):
        return _BagIterator( self._theItems )

class _BagIterator :
    def __init__( self, theList) : 
        self._bagItems = theList
        self._currentItem = 0
    
    def __iter__( self ) : 
        return self
    
    def __next__( self ) :
        if self._currentItem < len( self._bagItems ) :
            item = self._bagItems( self._currentItem )
            self._currentItem += 1
            return item
        else :
            raise StopIteration()