# Python program to convert decimal number into binary, octal and hexadecimal number system
# This code is for the students in PHYS339 to explain and send/recieve values in the right format to/from Arduino.
'''
Numbers in C:
    char: can be used to store a single character, eg 'a', the digit character '6' or a semicolon ','
    double: is equal to float (but with roughly twice the precision): 1.67, 3.141, ...
    _Bool: is used to store only the value 0 or 1: on/off, True/False
    int: integer constants 158, -10,0
    
Decimal-, Binary-, Octal- and Hexadecimal annotation:
    A decimal number, eg. 3442, can be annotated in different notations:
    Binary is annotated with a 0b in front: 0b110101110010
    Octal is annotated with 0: 06562
        2x8^0+6*8^1+5*8^2+6*8^3 = 3442
    Hexadecimal is annotated with a 0x the numbers 0-9 represent values from 0-9 and a-f represent numbers from 10-15: 0xd72
        2*16^0+7*16^1+13*16^2 = 3442    
    ==> use the code below to print decimal value in other notation
    
Example to print numbers, char, _Bool:
  #include <stdio.h>
  int main (void){
      int       rgbColor = 0xFFEF0D
      int       integerVar = 100;
      float     floatingVar = 331.79;
      double    doubleVar = 8.44e+11;
      char      charVar = 'W';
      _Bool     boolVar = 0;
      
      printf('Color is %#x\n', rgbColor); # prints value with '0x'
      printf('Color is %X\n', rgbColor); # prints value without '0x'
      printf ("integerVar = %i\n", integerVar);
      printf ("floatingVar = %f\n", floatingVar);
      printf ("doubleVar = %e\n", doubleVar);
      printf ("doubleVar = %g\n", doubleVar);
      printf ("charVar = %c\n", charVar);
      printf ("boolVar = %i\n", boolVar);
      return 0;
  }
  
Type Specifiers: long, long long, short, unsigned, signed:
  long int factorial; declares the variable factorial to be a long integer variable. Int and long int normally have the same
                      range up to 32bits (2^31-1 = 2'147'483'647), but for some systems, it needs to be declared. Thus a constant
                      value can be formed by optionally extend by either use "long" or by using a letter 'L' or 'l' at the end:
  long  int numberOfPoints = 131071100L;    declares it with an initial value ov 131'071'100
                      %li; used for decimal format
                      %lo; octal format
                      %lx; hexadecimal format
  long long maxAllowedStorage;  extend accuracy to be at least 64 bit wide (2^63-1 = 9.22337e18)
                      %lli; print value
  same for double declaration:  long double USdeficit = 1.32e7L;  
                      %Lf; displays long double
                      %Le; same value, scientific annotation
                      %Lg; machine chooses format by itself
  small: used to declare small values (16bits = 2^15-1 = 32'767), conserving memory space
                      %hi; decimal
                      %ho; octal
                      %hx; hexadecimal
  unsigned: only positive numbers. Either use "unsigned" or a "U" at the end
                      0x00FFU;  unsigned hexadecimal
                      0x00FFUL; unsigned long hexadecimal

To read out or send numbers in the right format, either use the code below, or easier, use the serial package and use .decode(), .encode() command.
'''

# Change this line for a different result
dec = 3443442
hexadecimal = hex(dec)

print "The decimal value of",dec,"is:"
print bin(dec),"in binary."
print oct(dec),"in octal."
print hex(dec),"in hexadecimal."

print "The decimal value of",hexadecimal,"is:"
print int(hexadecimal,16) #2 = binary, 8 = octal, 16= hexadecimal
