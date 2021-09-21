"""
For each class below, follow the instructions below to complete building the patient classes
"""

from abc import ABC, abstractmethod



"""
Patient class
Parent class for all classes shown below. 
"""
class Patient:

    """
    Patient instantiation method
    """
    def __init__(self, name, age, sex):

        ### TODO: #################################################
        # 1.    Replace the "raise NotImplemented" line           #
        # 2.    Make instance variables called                    #
        #       self.name, self.age, and self.sex                 #
        #       that will hold values from the method argument    #
        ###########################################################

        raise NotImplemented

    """
    Abstract method that will be overridden by children classes
    """
    @abstractmethod
    def print_bio(self):
        pass



"""
Minor class
Minor is-a Patient
"""
class Minor(Patient):

    """
    Minor instantiation method
    """
    def __init__(self, name, age, sex, grade=0):

        ### TODO: #################################################
        # 1.    Replace the "raise NotImplemented" line           #
        # 2.    Call the Patient constructor with super()         #
        # 3.    Make an instance variable called self.grade       #
        #       that will hold the grade-school year of a minor.  #
        #       If the minor is too young to be in school, grade  #
        #       will be defaulted to 0.                           #
        ###########################################################

        raise NotImplemented

    """
    Overriding print_bio
    """
    def print_bio(self):

        ### TODO: #######################################################################################
        # 1.    Replace the "raise NotImplemented" line                                                 #
        # 2.    Return a String with the format:                                                        #
        #       "<<self.sex>> minor named <<self.name>> of <<self.age>> years, in grade <<self.grade>>  #
        #       E.G. "Male minor named Bart Simpson of age 10 years, in grade 4"                        #
        #################################################################################################

        raise NotImplemented



"""
Infant class
Infant is-a Minor is-a Patient
"""
class Infant(Minor):

    """
    Infant instantiation method
    """

    def __init__(self, name, age, sex, weight):

        ### TODO: ###################################################
        # 1.    Replace the "raise NotImplemented" line             #
        # 2.    Call the Patient constructor with super()           #
        # 3.    Make an instance variable called self.weight        #
        #       that will hold the grade-school year of an infant.  #
        #############################################################

        raise NotImplemented

    """
    Overriding print_bio
    """
    def print_bio(self):

        ### TODO: ###########################################################################
        # 1.    Replace the "raise NotImplemented" line                                     #
        # 2.    Return a String with the format:                                            #
        #       "<<self.sex>> infant named <<self.name>> weighing <<self.weight>> pounds"   #
        #####################################################################################

        raise NotImplemented



"""
Adult class
Adult is-a Patient
"""
class Adult(Patient):

    """
    Adult instantiation method
    """
    def __init__(self, name, age, sex, hours_exercise):

        ### TODO: ###########################################################
        # 1.    Replace the "raise NotImplemented" line                     #
        # 2.    Call the Patient constructor with super()                   #
        # 3.    Make an instance variable called self.hours_exercise        #
        #       that will hold how many hours per week the adult exercises. #
        #####################################################################

        raise NotImplemented

    """
    Overriding print_bio
    """
    def print_bio(self):

        ### TODO: ###########################################################################
        # 1.    Replace the "raise NotImplemented" line                                     #
        # 2.    Return a String with the format:                                            #
        #       "<<self.sex>> adult named <<self.name>> of <<self.age>> years,              #
        #       exercising <<self.hours_exercise>> hours per week"                          #
        #####################################################################################

        raise NotImplemented



"""
Senior class
Senior is-a Adult is-a Patient
"""
class Senior(Adult):

    """
    Senior instantiation method
    """
    def __init__(self, name, age, sex, hours_sleep):

        ### TODO: ###########################################################
        # 1.    Replace the "raise NotImplemented" line                     #
        # 2.    Call the Patient constructor with super()                   #
        # 3.    Make an instance variable called self.hours_sleep           #
        #       that will hold how many hours per night the patient sleeps. #
        #####################################################################

        raise NotImplemented

    """
    Overriding print_bio
    """
    def print_bio(self):

        ### TODO: ###########################################################################
        # 1.    Replace the "raise NotImplemented" line                                     #
        # 2.    Return a String with the format:                                            #
        #       "<<self.sex>> senior named <<self.name>> of <<self.age>> years,             #
        #       sleeping <<self.hours_sleep>> hours per night"                              #
        #####################################################################################

        raise NotImplemented



#####################################################################################################
################################ Test out your classes below ########################################
#####################################################################################################

patient_list = []

patient_list.append(Minor("Bart Simpson", 10, "Male", 4))
patient_list.append(Infant("Boss Baby", 0, "Male", 8))
patient_list.append(Adult("Hank Hill", 45, "Male", 5))
patient_list.append(Senior("Eustace Bagge", 72, "Male", 0))

# Testing the print_bio function
for patient in patient_list:
    patient.print_bio()