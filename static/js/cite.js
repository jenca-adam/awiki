var page=window.location.href.split('/').at(-1);
console.log(page);

$('body').append('<div id="lightbox-wrapper" style="display:grid;visibility:hidden;position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(5,5,5,0.5);align-items:center;justify-content:center;"></div>')
$("#lightbox-wrapper").append('<div id="lightbox" style="width:800px;height:600px;background:white;border:medium groove black;padding:50px;padding-left:50px;box-shadow:rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;"><p id="lightbox-message">Please wait while Awiki loads BibTex...</p><textarea rows="9" cols="50" id="bib" readonly></textarea><p><button id="close">Close</button></p></div>')

function cite(){
	$("#lightbox-wrapper").css('visibility','visible');

	$("#bib").load('/cite/'+page,function(response,stat,xhr){if(stat!=='error'){$('#bib').show();$("#lightbox-message").text('BibTex copied!');navigator.clipboard.writeText($("#bib").val())}else{$('#lightbox-message').css({'font-weight':'bolder','color':'red'});$('#bib').hide(0);$("#lightbox-message").text('An error occured:'+xhr.status+' '+xhr.statusText)}})
	}
$("#close").click(function(){$("#lightbox-wrapper").css('visibility','hidden');})
$("#cite").click(cite)

