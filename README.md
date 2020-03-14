# DialogMachine
## Install
```shell script
pip install git+git://github.com/danger3466/DialogMachine.git
```
or add in requirements.txt:
```
wheel
git+git://github.com/danger3466/DialogMachine.git
```
and run:
```shell script
pip install -r requirements.txt
```
## Usage
```python
from dialog_machine.main import DialogMachine

class Dialog(DialogMachine):
    DIALOG = ['hello', 'echo', 'bay']
    
    def hello(self, name):
        self.next_hop += 1
        return 'Hello, ' + name

    def bay(self, none):
        self.next_hop = 'hello'
        return 'Bay'


test = Dialog()
print(test.response('Miki'))
print(test.response('knok-knok'))
test.next_hop = 'echo'
print(test.response('knok-knok'))
print(test.response(None))

print(test.response('Miki'))
```
