"""
Bir classdan istifadə edərək 2 metod yazın.
İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin 
( bu şəkildə olacaq: mylist=[1,2,3,4,5]) Daha sonra bir metod daha yazın. Bu metodda 
isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə 
həmin rəqəmlərin indexlərini qaytarın. Əgər belə
rəqəmlər yoxdursa -1 cavabı qaytarın. 

Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz.
"""

class Class:
    def Mylist(self):
        return [1, 2, 3, 4, 5, 6]

    def Hedef(self):
        hedef_reqem = 5
        mylist = self.Mylist()
        results = []  
        for i in range(len(mylist)):
            for j in range(i + 1, len(mylist)):
                if mylist[i] + mylist[j] == hedef_reqem:
                    results.append((i, j))  
        if results: 
            print(f"Indexleri uygun olaraq {results}olan ededlerin cemi {hedef_reqem}e beraberdir")
        else:
            print(-1)

netice = Class()
netice.Hedef()


