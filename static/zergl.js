console.log("hello world!");

g_bgcolor = "black";
g_fontcolor = "green";

function cur_bgcolor()
{
	bgcolor = document.body.style.background;
	if (bgcolor == undefined || bgcolor == "")
	{
		bgcolor = "black";
	}

	return bgcolor;
}
window.onload = function()
{
	g_bgcolor = cur_bgcolor;
}

document.ondblclick=function ()
{
	bgcolor = cur_bgcolor();
	change_color = bgcolor == "black" ? "white" : "black";
	document.body.style.background = change_color;
};
