#Name: Hena Kharwa
#Aim: Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#ID: 20CE043
#Github link: https://github.com/20CE043/Practical-2-3.e.git
def Intersection(A,B,C):
    s1 = set(A)
    s2 = set(B)
    s3 = set(C)
    print('List = ',A)
    print('Tuple = ',B)
    print('Dictionary = ',C)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = set(result_set)
    print('common of members of list, tuple & dictionary =',final_list)

    if __name__=="__main__":
        list1=[1,2,"ABC",3.4]
        tuple1=(12,20,"ABC",3.4)
        dict1={"ABC",1,3.4,"PQR"}
        Intersection(list1,tuple1,dict1)
        
    