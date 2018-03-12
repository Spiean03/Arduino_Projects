# Python program to convert decimal number into binary, octal and hexadecimal number system

# Change this line for a different result
dec = 3443442
hexadecimal = hex(dec)

print "The decimal value of",dec,"is:"
print bin(dec),"in binary."
print oct(dec),"in octal."
print hex(dec),"in hexadecimal."

print "The decimal value of",hexadecimal,"is:"
print int(hexadecimal,16) #2 = binary, 8 = octal, 16= hexadecimal