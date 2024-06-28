"""Sort Santa's Reindeer"""
def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key= lambda s: s.split()[1])
    
test = [
  "Dasher Tonoyan", 
  "Dancer Moore", 
  "Prancer Chua", 
  "Vixen Hall", 
  "Comet Karavani",        
  "Cupid Foroutan", 
  "Donder Jonker", 
  "Blitzen Claus"
]
test1 = ['Kenjiro Mori', 'Susumu Mori', 'Akira Mori']
print(sort_reindeer(test1))

print(sorted(test1, key= lambda full_name: full_name.split()[0]))