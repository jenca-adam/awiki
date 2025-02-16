function getLastUrlSegment(url) {
  return new URL(url).pathname.split('/').filter(Boolean).pop();
}
function loadTagList(){
	$.get("/api/get-taglist", function(result){
		$("#tags-top").html('');
		$(result.split(",")).each(function(){
			var tagName=this;
			$("#tags-top").append(`<span class="tag"><a class="tag-link" href="/my_search?tags=`+tagName+`">`+tagName+`</a></span>`);
		});
	})
}
function submitTags(){
	var pageName = getLastUrlSegment(location.href);
	var tags = $("#metadata-tags-tags .tag-link").map(function(){return $(this).text()}).get().join(",");
	$.get("/api/set-tags/"+pageName+"?tags="+tags, function(result){console.log(result)});
	setTimeout(loadTagList,500);
  
}
$("#addtag-form").submit(function(){var tagName = $("#addtag-tag").val();$("#addtag-tag").val(null);
	$("#metadata-tags-tags").append(`<span class="tag"><a class="tag-link" href="/my_search?tags=`+tagName+`">`+tagName+`</a><span class="tag-remove">×</span></span>`);return false;})

$("#metadata-tags-edit").click(function(){$(".tag-remove").show(); $("#metadata-tags-tags .tag-link").attr("disabled","disabled"); $("#addtag-form").show();$("#metadata-tags-edit").hide();$("#metadata-tags-confirm").show()});
$("#metadata-tags-confirm").click(function(){$(".tag-remove").hide(); $("#metadata-tags-tags .tag-link").removeAttr("disabled"), $("#addtag-form").hide(); $("#metadata-tags-edit").show();
$("#metadata-tags-confirm").hide(); submitTags()})
$("#metadata-tags-tags").on("click", ".tag-remove", function(){$(this).parent().remove()});
