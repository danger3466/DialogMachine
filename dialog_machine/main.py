class DialogMachine():
    """
    Класс реализующий диалог или квест в режиме вопрос-ответ.

    Пример:
    ::

        from dialog_machine.main import DialogMachine

        class Dialog(DialogMachine):
            DIALOG = ['hello', 'echo', 'bay']

            def hello(self, name):
                self.next_hop += 1
                return 'Hello, ' + name

            def bay(self, none):
                self.next_hop = 'hello'
                return 'Bay'

        dialog = Dialog()
        print(dialog.response('Miki'))
        print(dialog.response('knok-knok'))
        dialog.next_hop = 'echo'
        print(dialog.response('knok-knok'))
        dialog.next_hop += 1
        print(dialog.response(None))

    ::

        Hello, Miki
        knok-knok
        knok-knok
        Bay
    """

    DIALOG = ['echo']
    """
    В этой константе хранится список методов, которые вызываются методом response.
    
    Метод должен иметь 1 параметр, не считая self.
    
    Пример:
    
    ::
    
        def echo(self, request):
            return request

    """
    
    def __init__(self):
        self.__next_hop = 0
    
    @property
    def next_hop(self):
        """
        Хранит номер индекса константы `DIALOG`, метод с этим именем будет вызван методом `response`.

        Варианты использования:

        ::

            self.DIALOG = [
                'my_method',
                'echo',
                'other_metod'
            ]
            self.next_hop = 0 # Первый элемент из константы DIALOG
            self.next_hop = 'echo' # По имяни метода из константы DIALOG
            print(self.next_hop) # 1


        """
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
        """
        Вызывает метод из константы `DIALOG` и возвращает результат её его.

        :param request: Запрос, который будет передан методу из констаны `DIALOG`.
        :return: Результат выполнения метода вызваного из `DIALOG`
        """
        function = getattr(self, self.DIALOG[self.next_hop])
        return function(request)

    def echo(self, request):
        """
        Метод отвечающий эхом. Создан как простой пример и для отладки.

        :param request: Запрос
        :return: Возвращает то что получил на вход
        """
        return request

