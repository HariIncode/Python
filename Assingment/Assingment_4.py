class Stringstring_object :

    def __init__(self,input_string):
        self.input_string = input_string

    def reverse_string(self):       
        reversed = self.input_string[::-1]
        return reversed

    def count_vowels(self):
        vowel_count = 0
        for char in self.input_string:

            match char:
                case 'a' | 'e' | 'i' | 'o' | 'u':
                    vowel_count += 1
                case 'A' | 'E' | 'I' | 'O' | 'U':
                    vowel_count += 1
                case _:
                    continue

        return vowel_count
    
    def replace_characters(self,*args):
        try:
            swap = self.input_string.replace(args[0],args[1])
            return swap
        except IndexError :
            print("Minimum two arguments must be passed !")

    def remove_character(self,key,replace=""):
        altered_string = self.input_string.replace(key,replace)
        return altered_string




string_object = Stringstring_object("Hello World")

output_string = string_object.count_vowels()
print("No of Vowels in the given String :",output_string)

rev_result = string_object.reverse_string()
print("Reversed String :",rev_result) 

char_1 = string_object.replace_characters("H","Z")
print(char_1)  

remove = string_object.remove_character("W")
print(remove)