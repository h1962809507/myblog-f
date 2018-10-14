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
         success: function () {
             alert("成功");
         },
         error: function(){
            alert('失败！');
        },
     })
 }
