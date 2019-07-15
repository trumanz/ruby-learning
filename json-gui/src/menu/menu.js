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