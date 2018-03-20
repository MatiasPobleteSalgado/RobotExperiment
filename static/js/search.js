function Search(appl){
	// Constructor
	var _this = this;
	this.app = appl;
	this.form = $("#searchForm");
	this.list = $("#resultList");

	this.responseHandler = function(data){
		data = JSON.parse(data);
		_this.list.empty();
		for(indx in data){
			_this.list.append(
				"<li class='list-group-item'><a href='" + data[indx] + "''>" + data[indx] + "</a></li>"
			);
		}
	}

	this.send = function(evnt){
		evnt.preventDefault();
		$.get(
			"search",
			_this.form.serialize(),
			_this.responseHandler
		);
	}

	// Return object
	this.form.on("submit", this.send);
	return this;
}

app.addComponent(Search);
