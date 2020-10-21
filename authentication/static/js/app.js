addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);
		function hideURLbar(){ window.scrollTo(0,1); }

$("input[type=file]").change(function () {
	var fieldVal = $(this).val();

	// Change the node's value by removing the fake path (Chrome)
	fieldVal = fieldVal.replace("C:\\fakepath\\", "");

	if (fieldVal != undefined || fieldVal != "") {
		$(this).next(".custom-file-label").attr('data-content', fieldVal);
		$(this).next(".custom-file-label").text(fieldVal);
	}
});