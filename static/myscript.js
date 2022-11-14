
function time_show(){
	var t = new Date();
	$("#time_utc").html(t.toUTCString().substr(17,8));
	$("#time_bjt").html(t.toTimeString().substr(0,8));
	$("#date").html(t.toDateString().substr(0,10));
	}


$(document).ready(function() {
	time_show();
	setInterval(time_show, 1000);
});
