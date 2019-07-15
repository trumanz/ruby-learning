var Editor = function(schema, container) {
    this.schema = schema;
    this.container = container;

    this.init();
};

Editor.prototype = {
    constructor : Editor,
    init : function() {
    	 var jtree_div = createPreDiv(this.schema);
    	 this.container.appendChild(jtree_div);
    	 
    	 
    },
    
    createPreDiv : function(schema) {
        var txt_div = document.createElement("div");
        var pre_div = document.createElement("pre");
        pre_div.innerHTML = JSON.stringify(schema, null, "   ");
        txt_div.appendChild(pre_div);
        return txt_div;
    }

 
}; 