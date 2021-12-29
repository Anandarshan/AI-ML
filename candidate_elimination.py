import pandas as pd
data=pd.read_csv("book.csv")
size=len(data.iloc[0,:])




specific=[]
general=[]
specific.append([0]*len(data.iloc[0,1:size-1]))
general.append(['?']*len(data.iloc[0,1:size-1]))
#check for the last column to be either "YES" or "NO" or "Y" or"N"
#if the first is no then dont append the specific to it as such
#specific.append(list(data.iloc[0,1:size-1]))
for i in range(len(data)):
    if(data.iloc[i,size-1]=='No'):
        break
    if(data.iloc[i,size-1]=='Yes'):
        general.append(['?']*len(data.iloc[0,1:size-1]))
        
print(specific)
print(general)




#generate specific first da:
for i in range(1,len(data)):
    if(data.iloc[i,size-1]=='Yes'):
        try:
            present_list=specific[len(specific)-1]
            comparision_list=list(data.iloc[i,1:size-1])
            lis=[]
            for i in range(len(present_list)):
                if(present_list[i]!=comparision_list[i]):
                    lis.append('?')
                else:
                    lis.append(present_list[i])
            specific.append(lis)
        except:
            pass
    elif(data.iloc[i,size-1]=='No'):
        try:
            specific.append(specific[len(specific)-1])
        except:
            pass
print(specific)



#generate general things da
#get index from where the problem starts actually
index_value=[i for i in range(len(data)) if(data.iloc[i,size-1]=='No')]
the_generalisation=0
for i in range(index_value[0],len(data)):
    if(the_generalisation==1):
        present_list=specific[i+1]
        comparision_list=general[len(general)-1]
        lis=[]
        for i in range(len(comparision_list)):
            collecting_elements=list(set(comparision_list[i]))
            collecting_elements.remove('?')
            if(collecting_elements[0] in present_list):
                lis.append(comparision_list[i])
            else:
                pass
        general.append(lis)
            
    else:        
        present_list=specific[i]
        comparision_list=data.iloc[i,1:size-1]
        change=[present_list[i] for i in range(len(present_list)) if(present_list[i]!=comparision_list[i])]
        if('?' in change):
            change.remove('?')
        combination_all=[]
        for i in range(len(change)):
            lis=[]
            index_value=present_list.index(change[i])
            for j in range(len(present_list)):
                if(index_value==j):
                    lis.append(change[i])
                else:
                    lis.append('?')
            combination_all.append(lis)
        general.append(combination_all)
        the_generalisation=1
for i in range(len(general)):
    print(general[i])

        
        
        
        
collections=[]
for i in range(len(data.iloc[0,:])):
    collections.append(list(set(data.iloc[:,i])))
collections=collections[1:len(collections)-1]
saved_=collections
collections





the_first_list=["Some","Small","No","Affordable","One","No"]
for i in range(len(the_first_list[:len(the_first_list)-1])):
    collections[i].remove(the_first_list[i])
mega=[]
for i in range(len(collections)):
    elements=collections[i]
    for j in range(len(elements)):
        the_list=['?']*(len(data.iloc[0,:])-2)
        the_list[i]=elements[j]
        mega.append(the_list)
print(mega)
        
            



