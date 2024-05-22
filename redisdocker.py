import redis

# Conectar ao Redis
def new_func():
    r = redis.Redis(host='localhost', port=6379, db=0)
    return r

r = new_func()

# Criar/Atualizar uma chave
r.set('foo', 'bar')

# Ler o valor de uma chave
value = r.get('foo')
print(value)  # Output: b'bar'
