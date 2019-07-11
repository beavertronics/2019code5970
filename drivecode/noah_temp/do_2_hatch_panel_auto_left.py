# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command.commandgroup import CommandGroup

from do_hatch_panel_intake import Do_Hatch_Panel_Intake
from do_hatch_panel_release import Do_Hatch_Panel_Release
from do_hab_to_cargo_ship import Do_HAB_To_Cargo_Ship
from do_cargo_ship_to_wall import Do_Cargo_Ship_To_Wall
from do_wall_to_loading_station import Do_Wall_To_Loading_Station
from do_loading_station_to_wall import Do_Loading_Station_To_Wall
from do_wall_to_cargo_ship import Do_Wall_To_Cargo_Ship


class Do_2_Hatch_Panel_Auto_Left(CommandGroup):
	def __init__(self):
		super().__init__()

		self.addSequential(Do_HAB_To_Cargo_Ship)
		self.addSequential(Do_Hatch_Panel_Release)
		self.addSequential(Do_Cargo_Ship_To_Wall)
		self.addSequential(Do_Wall_To_Loading_Station)
		self.addSequential(Do_Hatch_Panel_Intake)
		self.addSequential(Do_Loading_Station_To_Wall)
		self.addSequential(Do_Wall_To_Cargo_Ship)
		self.addSequential(Do_Hatch_Panel_Release)
