/*
 * This file is part of EvoAI.
 *
 * EvoAI is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * EvoAI is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with EvoAI.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright 2008-2010 Thijs Marinussen
 */
require("version.nut");

class EvoAI extends AIInfo {
	version_major = 26;
	function GetAuthor()        { return "Thijs Marinussen"; }
	function GetName()          { return "EvoAI"; }
	function GetShortName()     { return "EvAI"; }
	function GetDescription()   { return "AI with genetic algorithm"; }
	function GetVersion()       { return version_major << 24 | revision; }
	function MinVersionToLoad() { return 21; }
	function GetDate()          { return "2010-08-12"; }
	function CreateInstance()   { return "EvoAI"; }
	function GetAPIVersion()    { return "1.0"; }
	function GetSettings() {
		AddSetting({name = "use_busses", description = "Enable busses", easy_value = 1, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "use_trucks", description = "Enable trucks", easy_value = 1, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "use_planes", description = "Enable aircraft", easy_value = 1, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "use_trains", description = "Enable trains", easy_value = 1, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "build_statues", description = "Try to build statues as soon as the AI has enough money",  easy_value = 0, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "always_autorenew", description = "Always use autoreplace regardless of the breakdown setting", easy_value = 0, medium_value = 0, hard_value = 0, custom_value = 0, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "depot_near_station", description = "Build train depots near the loading station instead of near the dropoff station.", easy_value = 1, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "build_bus_dtrs", description = "Build drive-through stops for busses", easy_value = 1, medium_value = 1, hard_value = 1, custom_value = 1, flags = AICONFIG_BOOLEAN});
		AddSetting({name = "debug_signs", description = "Enable building debug signs", easy_value = 0, medium_value = 0, hard_value = 0, custom_value = 0, flags = AICONFIG_BOOLEAN});
		// AddSetting({name = "A_MIN_PASS_SMALL", description = "AIR MINIMUM PASS ACCEPTANCE", easy_value = 0, medium_value = 0, hard_value = 0, custom_value = 0, flags = AICONFIG_AI_DEVELOPER});
		// AddSetting({name = "debug_signs", description = "Enable building debug signs", easy_value = 0, medium_value = 0, hard_value = 0, custom_value = 0, flags = AICONFIG_BOOLEAN});
		// AddSetting({name = "debug_signs", description = "Enable building debug signs", easy_value = 0, medium_value = 0, hard_value = 0, custom_value = 0, flags = AICONFIG_BOOLEAN});
		// AddSetting({name = "debug_signs", description = "Enable building debug signs", easy_value = 0, medium_value = 0, hard_value = 0, custom_value = 0, flags = AICONFIG_BOOLEAN});
	}
};
//AIController.GetValue();

RegisterAI(EvoAI());
