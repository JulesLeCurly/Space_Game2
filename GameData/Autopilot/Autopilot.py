import GameData.Autopilot.Fonction_de_deplacement.balade_in_space
import GameData.Autopilot.Fonction_de_deplacement.in_space_go_etoile

balade_in_space = GameData.Autopilot.Fonction_de_deplacement.balade_in_space
in_space_go_etoile = GameData.Autopilot.Fonction_de_deplacement.in_space_go_etoile

class Autopilot():

    def main(self, etoile, r_y, r_x, x, y, z):
        self.state_fonction = "balade_in_space"
        if self.state_fonction == "balade_in_space":
            return balade_in_space.balade_in_space(r_y, r_x, x, y, z)
        
        elif self.state_fonction == "in_space_go_etoile":
            return in_space_go_etoile.in_space_go_etoile(etoile, r_y, r_x, x, y, z)