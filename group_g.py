f = open('data.txt','r')

k = f.read()

lan =  [k,'c++','java','python']

data_str = '\n'.join(lan)

k = open('data.txt', 'w')

k.write(data_str)