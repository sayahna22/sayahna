def chck_pal1(str,low:int,high:int,a:set):
     low=0
     high=len(str)-1
     while(low<=high and str[low]==str[high]):
         #while(string[low]==string[high]):
         a.add(str[low:high+1])
         low=low+1
         high=high-1
def chck_pal(str,low:int,high:int,a:set):
     #low=0
     #high=len(str)-1
     while(low>=0 and high<len(str) and str[low]==str[high]):
         #while(string[low]==string[high]):
         a.add(str[low:high+1])
         low=low+1
         high=high+1
def pallin_sub(str):
     #a=[]
     a=set()
     for i in range(0,len(str)):
         chck_pal1(str,i,i,a)
         chck_pal(str,i,i,a)
         chck_pal1(str,i,i+1,a)
         chck_pal(str,i,i+1,a)
         
     print(a,end="")
if __name__ == '__main__':
     ch=str(input("Enter the string name:"))
     pallin_sub(ch)
