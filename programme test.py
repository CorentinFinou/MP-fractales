import interface
import sierpinski
import vonkoch
import carré
import dragon


interface.init()
interface.add(sierpinski.sierpinski,"Sierpinski")
interface.add(vonkoch.vonKoch,"Vonkoch")
interface.add(vonkoch.flocon,"Flocon de Vonkoch")
interface.add(carré.imbrique,"Imbriqué")
interface.add(dragon.dragoncurve,"Dragon")

interface.start()
#interface.interface(sierpinski.sierpinski) #ajoutte 