import random
 
mots = []
with open("mots.txt", "r") as f:
    for line in f:
        mots.append(line.split("\n")[0].upper())
    f.close()
 
numbers = "1234567890"
 
def ask_str(message: str, lenght: int):
    run = True
    while run:
        try_number = True
        check: str = str(input(message)).strip().upper()
        if len(check) == lenght:
            for e in check:
                if e in numbers:
                    try_number = False
            if try_number:
                break
            else:
                print("veuillez rentrer une chaine de caractères svp")
        else:
            print(f'veuillez rentrer une chaine de {lenght} caractère')
 
    return check
 
 
 
def print_green(s):
        return f"\033[32;99m{s}\033[m"
 
def print_red(s):
        return f"\033[31;99m{s}\033[m"
 
def print_yellow(s):
        return f"\033[33;99m{s}\033[m"
 
def suppos_color(supposition_color, supposition):
    lst = []
    for i in range(len(supposition)):
        if supposition_color[i] == 0:
            lst.append(print_green(supposition[i]))
        if supposition_color[i] == 1:
            lst.append(print_yellow(supposition[i]))
        if supposition_color[i] == 2:
            lst.append(print_red(supposition[i]))
    return lst
 
 
 
 
def display_grid(grid):
    for line in grid:
        print(" ".join(line))
 
 
def random_word():
    return random.choice(mots)
 
def créer_dic(secret_word):
    dic = {}
    for i in range(len(secret_word)):
        incremente_dic(dic, secret_word[i])
    return dic
 
 
def incremente_dic(dic,key):
    try:
        dic[key] += 1
    except KeyError:
        dic[key] = 1
 
 
def play_wordle():
    tour = -1
    secret_word = random_word()
    grid = [["_" for _ in range(len(secret_word))] for _ in range(5)]
    run = True
 
 
 
    print("Bienvenue sur le worlde !")
    print("Le mot à deviner contient", len(secret_word), "lettres.")
    display_grid(grid)
    print(secret_word)
 
 
 
    dic = créer_dic(secret_word)
 
 
    while run:
        tour += 1
 
        supposition = ask_str("Devinez une lettre ou le mot complet : ", len(secret_word))
 
 
        supposition_color = [0] * len(secret_word)
 
 
        if supposition == secret_word:
            print("Félicitations, vous avez deviné le mot ! Le mot était:", secret_word)
            run = False
            break
        elif len(supposition) != len(secret_word):
            print(f"Veuillez entrer un mot de {len(secret_word)} lettres")
        else:
            for i in range(len(supposition)):
                print(dic)
                if supposition[i] == secret_word[i]:
                    supposition_color[i] = 0
                elif supposition[i] in secret_word:
                    if str(supposition[i]) in dic:
                        dic[supposition[i]] -= 1
                    if dic[supposition[i]] >= 0:
                        supposition_color[i] = 1
                    else:
                        supposition_color[i] = 2
                else:
                    supposition_color[i] = 2
 
 
        grid[tour] = suppos_color(supposition_color, supposition)
        display_grid(grid)
        dic = créer_dic(secret_word)
 
 
        if tour == 5:
            print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était:", secret_word)
            run = False
 
 
 
 
play_wordle()