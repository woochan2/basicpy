'''
inventory = {}


def add_item(item,amount,inven):

    if check_item(item,inven):
        inventory[item] += amount
        print(item+"의 수량은 "+str(inven[item])+"입니다.")

    else:
        inven[item] = amount
        print(item+"이 추가되었습니다.")


def remove_item(item,inven):
    if check_item(item,inven):
        inven[item] = 0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")

def consume_item(item):
    if check_item(item):
        inventory[item]=1
        print(item+"를(을) 사용합니다.")
        inventory[item]=0
    else:
        print(item+"의 수량이 부족합니다.")
    
        

def check_item(item, inven):
    return item in inven

def print_menu():
    print("0. 끝내기")
    print("1. 아이템 추가")
    print("2. 아이템 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")
    
while True:
    print_menu()
    option = int(input("메뉴 번호를 입력하세요)"))
    if option == 0:
        print("종료합니다.")
        break
    elif option == 1:
        new_item = input("아이템을 입력하세요.)")
        amount=int(input("수량 입력하세요"))
        add_item(new_item,amount,inventory)
    elif option == 2:
        eliminated_item = input("아이템을 입력하세요.)")
        remove_item(eliminated_item,inventory)
    elif option == 3:
        print(inventory)
    elif option == 4:
        use_item = input("아이템을 입력하세요.)")
        consume_item(use_item)  
    else:
        print("잘못된 번호를 입력하셨습니다.")


'''


character={}
select_character=None
def new_character(name,character):
    if name in t_character:
        print("이미 존재하는 캐릭터의 이름입니다.")
    else:
        inventory={}
        t_character[name]=inventory

def check_character(name,t_character):
    return name in t_character

def print_characterMenu():
    print("0.끝내기")
    print("1.캐릭터 추가")
    print("2.캐릭터 이름 출력")
    print("3.캐릭터 선택")
    print("4.캐릭터 인벤토리 조작")
while True:
    print_characterMenu()
    option=input("메뉴를 선택하세요 ")
    if option == 0:
        print("종료되었습니다")
        break
    elif option == 1:
        name = input("캐릭터 이름 입력")
        new_character(name,character)
    elif option == 2:
        i=1
        print("#############")
        for name in character.keys():
            print(str(i)+", "+name)
            i+=1
        print("#############")

    elif option == 3:
        temp_name = input("캐릭터 이름 입력")
        if check_character(temp_name, character):
            select_character = temp_name
        else :
            print(temp_name+ "은 존재 하지 않는 캐릭터 입니다.")
        
        
            


    
