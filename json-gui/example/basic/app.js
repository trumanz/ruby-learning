

var getSchema = function() {
    var schema = null;
    $.ajax({
        url : 'person.json',
        async : false,
        dataType : 'json',
        success : function(json) {
            schema = json;
        }
    });
    console.log(schema);
    return schema;
};


 
var createPreDiv = function(schema) {
    var txt_div = document.createElement("div");
    var pre_div = document.createElement("pre");
    pre_div.innerHTML = JSON.stringify(schema, null, "   ");
    txt_div.appendChild(pre_div);
    return txt_div;
};

$(document).ready(function() {

    var panel = $("#placeholder");
    console.log(panel);
    console.log(panel.get(0));
    var schema = getSchema();
 
    var json_gui = new JSONGUI(panel.get(0), schema);
    

    return;

});

