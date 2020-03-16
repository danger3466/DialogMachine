class DialogMachine():
    DIALOG = ['echo']
    
    def __init__(self):
        self.__next_hop = 0
    
    @property
    def next_hop(self):
        return self.__next_hop

    @next_hop.setter
    def next_hop(self, value):
        if isinstance(value, str):
            value = self.DIALOG.index(value)

        if value >= len(self.DIALOG):
            self.__next_hop = 0
        else:
            self.__next_hop = value

    def response(self, request):
        function = getattr(self, self.DIALOG[self.next_hop])
        return function(request)

    def echo(self, request):
        return request

