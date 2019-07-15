/*! JSON GUI v0.0.1 - JSON Schema -> HTML GUI
 * By Truman Zhou 
 * Date: 2016-05-13
 */
var JSONGUI = function(element, schema) {
	if (!(element instanceof Element)) {
		throw new Error("element should be an instance of Element");
	}
	this.element = element;
	this.schema = schema;
	this.init();
	
};

JSONGUI.prototype = {
	constructor : JSONGUI,
	init : function() {
		console.log("this called");
		
		var panel = document.createElement('div');
		panel.className = ".container-fluid";
		
		{
			var menu_container = document.createElement('div');
			menu_container.id = "menu_container";
			menu_container.className = "col-sm-3 col-md-2 bs-docs-sidebar";
			panel.appendChild(menu_container);
			self.menu = new Menu(this.schema, menu_container);
		}
		{
			var editor_container = document.createElement('div');
	 		editor_container.id = "editor_container";
	 		editor_container.className = "col-sm-6 col-md-8 bs-docs-sidebar";
	 		panel.appendChild(editor_container);
	 		self.editor = new Editor(this.schema, editor_container);
		}
 
 
		this.element.appendChild(panel);
		
	}

};

var Menu = function(schema, container) {
    this.schema = schema;
    this.container = container;

    this.init();
};

Menu.prototype = {
    constructor : Menu,
    init : function() {
        this.container.appendChild(this.createJtreeMenu(this.schema));

    },

    createJtreeMenu : function(schema) {
        var jtree_div = document.createElement("div");
        var jtree_json = craeteJtreeJson("Root", schema);

        var jstree = $(jtree_div).jstree({
            "core" : {
                "themes" : {
                    "stripes" : true
                },
                "data" : jtree_json
            },

            "plugins" : ["contextmenu"],
            "contextmenu" : {
                items : this.customMenu
            }

            // "plugins" : ["contextmenu", "search", "state", "types", "wholerow"]

        });

        $(jtree_div).on("changed.jstree", function(e, data) {
             console.log(e);
            console.log(data)
        });

        var ref = $(jtree_div).jstree(true);

        console.log(ref.get_json());

        var sel = ref.create_node(ref, {
            "text" : "created"
        });
        if (sel) {
            ref.edit(sel);
        }

        $(jtree_div).on('ready.jstree', function() {
            $(jtree_div).jstree("open_all");
        });
        // jstree.create_node(jstree, {"type":"file"});

        return jtree_div;
    },
    
    customMenu : function(node) {
        //var tree = $("#tree").jstree(true);
        return {
            "Create": {
                "separator_before": false,
                "separator_after": false,
                "label": "Create",
                "action": function (obj) { 
                    $node = node.create_node($node);
                    node.edit($node);
                }
            },
            "Rename": {
                "separator_before": false,
                "separator_after": false,
                "label": "Rename",
                "action": function (obj) { 
                    node.edit($node);
                }
            },                         
            "Remove": {
                "separator_before": false,
                "separator_after": false,
                "label": "Remove",
                "action": function (obj) { 
                    node.delete_node($node);
                }
            }
        };
    }


}; 
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
var craeteJtreeJson = function(name, schema) {
    var node = null;
    if (schema.type == "object") {
        console.log(schema);
        var children_nodes = [];
        for (var key in schema.properties) {
            var kid_schema = schema.properties[key];
            children_nodes.push(craeteJtreeJson(key, kid_schema));
        }
        node = {
            "text" : schema.title ? schema.title : schema.id,
            "children" : children_nodes,
            "extral_schema" : schema,
        };
    } else {
        node = {
            "text" : schema.title ? schema.title : name,
            "extral_schema" : schema
        };
    }
    return node;
};

//# sourceMappingURL=jsongui.js.map