def combat(health, damage):
    health -= damage
    if health < 0:
        return 0
    return health

print(combat(10, 11))

'''cleverest answer by mmalkavian'''
def combat(health, damage):
    return max(0, health - damage)

print(combat(10, 11))

