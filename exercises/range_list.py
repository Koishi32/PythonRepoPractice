def solution(args):
    start =  args[0]
    formattedString=str(start)
    end = ""
    extra=""
    acc=0
    for a in args[1:]:
        if (start == (a-1)):
            acc+=1
            extra+=","+str(a)
            if(acc>1):
                end = "-"+str(a)
                extra=""
        else:
            formattedString+=extra+end+","+str(a)
            acc=0
            end= ""
            extra=""
        print("number: "+str(a)+" yielded: "+str(formattedString))
        start = a
    formattedString+=end
    return formattedString

def main():
   res =solution([-68, -66, -65, -62, -61, -58, -57, -56, -54, -52, -49, -48, -45, -44, -42, -40, -38, -35, -33, -32, -31, -30, -27, -25, -22, -20, -17, -15, -14, -13])
   print(res)

if __name__ == "__main__":
    main()
