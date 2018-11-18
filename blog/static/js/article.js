function convert(){
    var text = document.getElementById("oriContent").value;
    var converter = new showdown.Converter();
    var html = converter.makeHtml(text);
    document.getElementById("result").innerHTML = html;
}


function ajaxSubmitForm() {
     $("#article").ajaxSubmit({
         url: "/add_article",
         type: "POST",
         success: function (resp) {
             if(resp == "ok"){
                 alert("成功");
             }else{
                 alert(resp)
             }

         },
         error:function(XMLHttpRequest, textStatus, errorThrown){
            alert(XMLHttpRequest.status+errorThrown);
         },
     })
 }
