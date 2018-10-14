
function convert(){
    var text = document.getElementById("oriContent").value;
    var converter = new showdown.Converter();
    var html = converter.makeHtml(text);
    document.getElementById("result").innerHTML = html;
}
