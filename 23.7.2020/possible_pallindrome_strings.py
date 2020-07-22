def chck_pal(string:str,low:int,high:int,a:set):
     low=0
     high=len(string)-1
     while(low<=high):
         if(string[low]==string[high]):
             a.add(string[low:high+1])
             low=low+1
             high=high-1
def pallin_sub(string):
     #a=[]
     a=set()
     for i in range(len(string)):
         chck_pal(string,i,i,a)
         chck_pal(string,i,i+1,a)
     print(a,end="")
if __name__ == '__main__':
     string=str(input("Enter the string name:"))
     pallin_sub(string)
