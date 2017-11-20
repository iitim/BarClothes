$(".upload-image-input").change(function() {
    //alert(  $(this).val() );
    $(this).parent(".upload-image").hide();
    $(this).parents().eq(2).find(".upload-image-confirmation").show();
    $("#upload-image-filepath").text($(this).val().replace(/C:\\fakepath\\/i, ''));
  });
  
$(".upload-image-cancel").click(function() {
    $(this).parents().eq(2).find(".upload-image").show();               
    $(this).parent(".upload-image-confirmation").hide();
    
    $("#upload-image-filepath").text('');
});