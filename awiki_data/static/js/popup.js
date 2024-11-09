var oldname;
if ($("#error_traceback_details").text().split(':')[0]=='\nPageExistsError'){
	oldname= $("#error_traceback_details").text().split("'")[1].split("'")[0]
	$("#container").css('background-color','#fd8')
	$("#container").css('color','#a00')
$("#container").html(`<p>FAILED: Page already exists!</p><br><p id="rename-line" style="display:none;">New name: <input id="name" value="`+oldname+`"></input><button id="sub"> Rename!</button></P><br><br><p>Please choose from these options:</p><p><button id="continue">Ignore exception and continue</button>&nbsp;<button id="rewrite">Rewrite</button>&nbsp;<button id="rename">Rename new file</button>`)
	$("#continue").click(function(){location.replace(location.href+'?continue=true')})
	$("#rename").click(function(){$("#rename-line").show()})
	$("#sub").click(function(){location.replace(location.href+'?name='+$("#name").val())})
	$("#rewrite").click(function(){location.replace(location.href+'?rewrite=true')})



}
