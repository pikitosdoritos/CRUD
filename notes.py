import os
import msvcrt

def getch(prompt):
    print(prompt)
    return msvcrt.getch().decode('utf-8')

def clear_screen():
    os.system('cls')
    
def main ():
    print("\nНотатки")
    list = []
    x = 0

    while True:
        clear_screen()
        entry = getch("\nНатисни 1 для того, щоб створити нову нотатку \nНатисни 2 для того, щоб переглянути наявні нотатки \nНатисни 3 для редагування \nНатисни 4 для того, щоб видалити нотатку \nНатисни 5 для виходу\n")  
        if entry == '1':
            list.append(input("\nЗапишіть вашу нотатку: \n"))

        elif entry == '2':
            for index, term in enumerate(list):
                print(index, term)
            input("Натисни 'Enter', щоб продовжити:")
    
        elif entry == '3':
            i = int(getch("Введіть номер нотатки для її редагування"))
            if 0 <= i < len(list):
                print(list[i])
                x = input("Напиши нове значення для цієї нотатки\n")
                list[i] = x    
            else: 
                input("Неправильний індекс, для продовження натисни 'Enter'")   

        elif entry == '4':
            i = int(getch("Введіть номер нотатки, яку хочете видалити\n"))    
            if 0 <= i < len(list):
                print(list[i])
                answer = input("Ви точно хочете видалити цю нотатку? Для того щоб видалити напиши 'Yes' для відміни 'No' ")
                if answer.lower() == 'yes':
                    del list[i]
                
        elif entry == '5':
            print('Вихід')
            exit()


        else:
            print("ПОМИЛКА!")
        
if __name__ == "__main__":
    main()
            