$('#tbshow').click(function(){
	if($(this).text()=='Show full traceback'){	
		$(this).text('Hide traceback')
	}
	else{
	$(this).text('Show full traceback')
	};
	$('#tback').toggle(200)})
