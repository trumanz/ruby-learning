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
