class Test:
    def __init__(self, name, age, sur_name):
        self.name = name
        self.age = age
        self.sur_name = sur_name


test = Test("My_name", 15, 'My_surname')

tst = test.__dict__
a = ''
for i in tst:
    a += (str(i) + ' ' + str(tst[i])+ '\n')

a = a[:-1]
print(a)
def print_at(n):
    print(n)
print[print_at(i) for i in range(0, 10)]
st = f"<h1>Привет! Я {name}, и мне {age}</h1> &#013 <p>Случайное число {randint(0,100)}</p> &#013 <p1>\n{delattrs(watch1)}</p2>"
HttpResponse(content=str("Привет! Я {name}, и мне {age}".format(name = "Черненков Артемий", age = 17), 'Случайное число: ', randint(0,100), detatrs(watch1)))