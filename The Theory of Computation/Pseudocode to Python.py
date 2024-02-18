#Number 0
#WHILE (Number < 1) OR (Number > 10)
#   OUTPUT "Enter a positive whole number:
#   INPUT Number
#   IF Number > 10 THEN
#       OUTPUT "Number too large."
#   ELSE
#       IF Number < 1 THEN
#           OUTPUT "Not a positive number."
#       ENDIF
#   ENDIF
#ENDWHILE
#
#C← 1
#FOR k <- 0 TO Number -1
#   OUTPUT C
#       c ← (c * (Number - 1 - k)) DIV (k + 1)
#ENDFOR

number=0
while (int(number)<1) or (int(number)>10):
    print("Enter a positive number")
    number=input("Enter a positive number: ")
    if int(number)>10:
        print("Number is too large")
    else:
        if int(number)<1:
            print("Number is too small")
