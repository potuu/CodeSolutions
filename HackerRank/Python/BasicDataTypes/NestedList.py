if __name__ == '__main__':
    liste = []
    sozluk = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        liste.append(score)
        
        if score in sozluk:
            sozluk[score].append(name)
        else:
            sozluk[score]=[name]
        
    print ("\n".join(sorted((sozluk[(sorted(set(liste)))[1]]))))
