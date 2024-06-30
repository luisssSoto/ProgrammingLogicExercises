"""int32 To IPV4"""
def int32_to_ip(int32):
    ipv4_address = ''
    for i in range(3, 0, -1):
        # addresses allowed in this octet
        octet = int32 // 256 ** i
        # address that still are missing
        int32 %= 256 ** i
        ipv4_address += str(octet) + '.'
    ipv4_address += str(int32)
    return ipv4_address

'''2149583361 ==> "128.32.10.1"'''
test1 = 2149583361
print(int32_to_ip(test1))
print(test1 % 256 ** 3)

''''Explanation there are 8 octets, every octet == to 8 bits, and at the same time
is a byte, every octet has different amount of addreses in the next order'''
print(f'Each address in the first octet has: {256 ** 3} adresses because is the result of 256 ** 3')
print(f'Each address in the second octet has: {256 ** 2} adresses because is the result of 256 ** 2')
print(f'Each address in the thirth octet has: {256 ** 1} adresses because is the result of 256 ** 1')
print(f'Each address in the fourth octet has: {256 ** 0} adresses because is the result of 256 ** 0')

'''So if you want to know how many address exist in any direction you need to follow
the next rule octet * 256 ** (3, 2, 1, 0) depends where octet you are'''
address = '128.32.10.1'
amount_addresses = 0
addresses_list = address.split('.')
print(addresses_list)
count = 0
for i in range(3, -1, -1):
    amount_addresses += int(addresses_list[count]) * 256 ** i
    count += 1
    print(f'octet{count}: {amount_addresses}')

'''Cleverest solutions by Unnamed'''
from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))

