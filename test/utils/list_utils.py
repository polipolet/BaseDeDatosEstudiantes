

class ListUtils:

    def lista_a_String(lista):
        result = "Lista<"
        i = 0
        for object in lista:
            if i!=0:
                result +=","
            result += str(object)
            i += 1
        result += ">"
        return result