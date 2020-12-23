import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
V2A_PATH = "d:/ymir work/ui/pattern/"
LINE_LABEL_X 	= 20
LINE_DATA_X 	= 90
LINE_STEP	= 0
SMALL_BUTTON_WIDTH 	= 45
MIDDLE_BUTTON_WIDTH 	= 65

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 170,
	"height" : 680,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 165,
			"height" : 675,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 8,

					"width" : 160,

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : "Efsun Bot", 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "ChooseBonus0",
					"type" : "text",

					"x" : LINE_LABEL_X-5,
					"y" : 39,
					"text_vertical_align" : "center",
					
					"r" : 40.0,
					"g" : 100.0,
					"b" : 255.0,
					"a" : 1.0,

					"text" : "Bonus:",
				},
				{
					"name" : "Bonus0_List",
					"type" : "listbox",

					"x" : LINE_LABEL_X-5,
					"y" : 48,
					"width" : 115,
					"height" : 622,

					"item_align" : 0,
				},
				{
					"name" : "Ok_button",
					"type" : "button",

					"x" : LINE_LABEL_X-9+8,
					"y" : 645,

					"text" : "OK",

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "stop_button",
					"type" : "button",

					"x" : LINE_LABEL_X+MIDDLE_BUTTON_WIDTH*1-9+8,
					"y" : 645,

					"text" : "Kapat",

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
			),
		},
	),
}
