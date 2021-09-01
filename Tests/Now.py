from datetime import datetime

today = datetime.now()

def timestamp():
    now = today.strftime("%B %d, %Y   %H:%M:%S")
    print('{0:>40}'.format(now))
    
def name():
    now = today.strftimes('%H:%M:%S')