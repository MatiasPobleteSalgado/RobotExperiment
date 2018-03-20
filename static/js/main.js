function APP(dom) {
	// Object self reference
	var _this = this;
	
	this.__init = function(){
		for(c in _this.components){
			console.log(typeof(_this.components[c]))
			_this.components[c] = new _this.components[c](_this);
		}
	}

	this.addComponent = function(comp, name){
		this.components["name"] = comp; //(_this);
	}

	// Constructor
	this.components = {};
	$(dom).ready(this.__init);

	// Object return
	return this;
}

app = new APP(document);