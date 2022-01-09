msg='welcome to Python 101: Strings'
  
print(msg.title())
one=(msg[18]) 
welcome=(msg[0:7]) 
ring=(msg[25:29])
to=(msg[8:11])
t=(msg[8])
y=(msg[12])
l=(msg[2])
e=(msg[6])
r=(msg[25])
print(one.title() +" " + welcome.title() +" " +ring.title() +" " +to.title()+" " +t.title()+y+l+e+r)

txt=(one.title() +" " + welcome.title() +" " +ring.title() +" " +to.title()+" " +t.title()+y+l+e+r)[::-1]
print(txt)
