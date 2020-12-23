import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
V2A_PATH = "d:/ymir work/ui/pattern/"
LINE_LABEL_X 	= 15
LINE_DATA_X 	= 90
LINE_STEP	= 0
SMALL_BUTTON_WIDTH 	= 45
MIDDLE_BUTTON_WIDTH 	= 65

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 415,
	"height" : 210,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 410,
			"height" : 205,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 1,
					"y" : 8,

					"width" : 400,

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : "Efsun Bot", 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "choose_button_01",
					"type" : "button",

					"x" : LINE_LABEL_X,
					"y" : 40,

					"text" : "1.Bonus",

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "bonus_1_text1",
					"type" : "text",

					"x" : LINE_LABEL_X+92,
					"y" : 44,

					"text" : "Bonus Oran:",
				},
				{
					"name" : "InputSlot_value_1",
					"type" : "slotbar",

					"x" : LINE_LABEL_X+150,
					"y" : 44,
					"width" : 29,
					"height" : 14,
				},
				{
					"name" : "bonus_value_1",
					"type" : "editline",

					"x" : LINE_LABEL_X+154,
					"y" : 44,

					"width" : 29,
					"height" : 18,

					"input_limit" : 4,
					"enable_codepage" : 0,

					"r" : 255.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
					"fontsize" : "MIDDLE",
					
					"text" : "0",
				},
				{
					"name" : "choose_button_02",
					"type" : "button",

					"x" : LINE_LABEL_X,
					"y" : 75,

					"text" : "2.Bonus",

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "bonus_2_text2",
					"type" : "text",

					"x" : LINE_LABEL_X+92,
					"y" : 79,

					"text" : "Bonus Oran:",
				},
				{
					"name" : "InputSlot_value_2",
					"type" : "slotbar",

					"x" : LINE_LABEL_X+150,
					"y" : 79,
					"width" : 29,
					"height" : 14,
				},
				{
					"name" : "bonus_value_2",
					"type" : "editline",

					"x" : LINE_LABEL_X+154,
					"y" : 79,

					"width" : 29,
					"height" : 18,

					"input_limit" : 4,
					"enable_codepage" : 0,

					"r" : 255.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
					"fontsize" : "MIDDLE",
					
					"text" : "0",
				},
				{
					"name" : "choose_button_03",
					"type" : "button",

					"x" : LINE_LABEL_X,
					"y" : 110,

					"text" : "3.Bonus",

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "bonus_3_text3",
					"type" : "text",

					"x" : LINE_LABEL_X+92,
					"y" : 114,

					"text" : "Bonus Oran:",
				},
				{
					"name" : "InputSlot_value_3",
					"type" : "slotbar",

					"x" : LINE_LABEL_X+150,
					"y" : 114,
					"width" : 29,
					"height" : 14,
				},
				{
					"name" : "bonus_value_3",
					"type" : "editline",

					"x" : LINE_LABEL_X+154,
					"y" : 114,

					"width" : 29,
					"height" : 18,

					"input_limit" : 4,
					"enable_codepage" : 0,

					"r" : 255.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
					"fontsize" : "MIDDLE",
					
					"text" : "0",
				},
				{
					"name" : "choose_button_04",
					"type" : "button",

					"x" : LINE_LABEL_X+180+21,
					"y" : 40,
#					"y" : 75,

					"text" : "4.Bonus",

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "bonus_4_text4",
					"type" : "text",

					"x" : LINE_LABEL_X+272+21,
					"y" : 44,

					"text" : "Bonus Oran:",
				},
				{
					"name" : "InputSlot_value_4",
					"type" : "slotbar",

					"x" : LINE_LABEL_X+330+21,
					"y" : 44,
					"width" : 29,
					"height" : 14,
				},
				{
					"name" : "bonus_value_4",
					"type" : "editline",

					"x" : LINE_LABEL_X+330+25,
					"y" : 44,

					"width" : 29,
					"height" : 18,

					"input_limit" : 4,
					"enable_codepage" : 0,

					"r" : 255.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
					"fontsize" : "MIDDLE",
					
					"text" : "0",
				},
				{
					"name" : "choose_button_05",
					"type" : "button",

					"x" : LINE_LABEL_X+180+21,
					"y" : 75,
#					"y" : 40,

					"text" : "5.Bonus",

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "bonus_5_text5",
					"type" : "text",

					"x" : LINE_LABEL_X+272+21,
					"y" : 79,

					"text" : "Bonus Oran:",
				},
				{
					"name" : "InputSlot_value_5",
					"type" : "slotbar",

					"x" : LINE_LABEL_X+330+21,
					"y" : 79,
					"width" : 29,
					"height" : 14,
				},
				{
					"name" : "bonus_value_5",
					"type" : "editline",

					"x" : LINE_LABEL_X+330+25,
					"y" : 79,

					"width" : 29,
					"height" : 18,

					"input_limit" : 4,
					"enable_codepage" : 0,

					"r" : 255.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
					"fontsize" : "MIDDLE",
					
					"text" : "0",
				},
				{
					"name" : "reset_bonusall",
					"type" : "button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1+80,
					"y" : 160,

					"text" : "Bonuslari sil",

					"default_image" : ROOT_PATH + "XLarge_Button_01.sub",
					"over_image" : ROOT_PATH + "XLarge_Button_02.sub",
					"down_image" : ROOT_PATH + "XLarge_Button_03.sub",
				},
				{
					"name" : "break_bonusswitch",
					"type" : "button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1+80,
					"y" : 130,

					"text" : "Kapat",

					"default_image" : ROOT_PATH + "XLarge_Button_01.sub",
					"over_image" : ROOT_PATH + "XLarge_Button_02.sub",
					"down_image" : ROOT_PATH + "XLarge_Button_03.sub",
				},
				{
					"name" : "start_switch_button",
					"type" : "button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1-122,
					"y" : 160,

					"text" : "Baslat",
					"text" : "Baslat",

					"default_image" : ROOT_PATH + "XLarge_Button_01.sub",
					"over_image" : ROOT_PATH + "XLarge_Button_02.sub",
					"down_image" : ROOT_PATH + "XLarge_Button_03.sub",
				},

			),
		},
	),
}
