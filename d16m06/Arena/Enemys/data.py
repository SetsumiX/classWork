from d16m06.Arena.Enemys.class_enemy import Enemy
from d16m06.Arena.tools.cteate_params import GetPar

data = {
    "b_1": Enemy(
        power=GetPar.choice(),
        health=GetPar.choice(),
        agility=GetPar.choice(),
        damage=GetPar.param(),
        defense=GetPar.param(),
    ),
    "b_2": Enemy(
        power=GetPar.choice(),
        health=GetPar.choice(),
        agility=GetPar.choice(),
        damage=GetPar.param(),
        defense=GetPar.param(),
    ),
    "b_3": Enemy(
        power=GetPar.choice(),
        health=GetPar.choice(),
        agility=GetPar.choice(),
        damage=GetPar.param(),
        defense=GetPar.param(),
    ),
}