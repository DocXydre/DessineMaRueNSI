import turtle
from random import randint

def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    Rouge = randint(0,255)
    Vert = randint(0,255)
    Bleu = randint(0,255)
    return (Rouge,Vert,Bleu)
