# Reader

class Reader(object):
    @staticmethod
    def ox(message):
        response = input(message).lower()
        while not (response == 'o' or response == 'x'):
            response = input(message).lower()
        return response == 'o'
    
    @staticmethod
    def get_number(message,low,high):
        response = input(message)
        while not (response.isdigit() and low <= int(response) <= high):
            response = input(message)
        return int(response)

