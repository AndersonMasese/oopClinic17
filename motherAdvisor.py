"""
This program demonstrates the power and use of oop, encapsulation and inheritance
"""

option=raw_input("PLEASE CHOOSE OPTIONS\n\n1:Get health Advisor and information\n2:Get infant advisor\n3:get available doctors list\n4:Get emergency numbers and health facilities\n5:Get common disease characteristics")
if(option==1){
    myHealthAdvisor()


}
elif(option==2){
    mother.infantAdvisor()

}
elif(option==3){
    mother.availableDoctors()

}
elif(option==4){
    generalInfoAdvisor.generalInfoAccessor()

}

else:
    {
        print(Enter a valid choice option)
    }
class mother:
    """def __init__(self):
        healthAdvisor
        infantAdvisor
        mortalityAdvisor
        homeCareAdvisor"""

    def infantAdvisor(self):
        print("A:infants should only drink mother's milk\nInfants should be given 100% attention")

    def availableDoctors(self):
        dataHolderDictionary={'Moses':'0700555698','Jackline':'0720987567'}
        for key in dataHolderDictionary:
            print(key)
        #demonstrating the concept of polymorphism
        #python can very easily infer that dataHolderDictionary is actually a dictionary without us having to state so explicitly
        #dataHolderDictionary could be a list etc but it is a dictionary in this particular case.
class infantAdvisor(mother):#class infantAdvisor inherits from motherAdvisor and accesses mother's method infantAdvisor
    def __init__(self):

class generalInfoAdvisor:
    def __generalInfo(self):
        #demonstrating the concept of public and private data encapsulation in python
        print("This is the list of Available Health facilities:\n1:Tenwek Hospital\n2:Kenyatta Hospital")

    def generalInfoAccessor(self):
        generalInfo()
        #this method will access the private method __generalInfo before it's called from the program driver








def myHealthAdvisor():
    print("Welcome to the Health Advisor Expert.\nA:Avoid Alcohol at all costs when you are pregnant.\nB:Avoid Using over the counter drugs when pg"+
    "If you have a fever when pregnant, consult your doctor immediately.C: Do not use abortion inducing drugs without the help of a qualified physician")


    